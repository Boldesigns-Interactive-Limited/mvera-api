import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, \
                                                      PermissionsMixin

class AbstractBase(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)
  updated = models.DateTimeField(db_index=True, auto_now=True)
  is_active = models.BooleanField(default=True)
  created_by = models.UUIDField(null=True, blank=True),
  updated_by = models.UUIDField(null=True, blank=True)

  class Meta:
    abstract = True

class UserManager(BaseUserManager):

  def create_user(self, email, password=None, **extra_fields):
    """ Creates and saves a User with a given email and password """

    if not email:
      raise ValueError('Users must have an email address')

    email = self.normalize_email(email)
    user = self.model(email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self.db)

    return user

  def create_superuser(self, email, password):
    """ Creates a new super user """
    user = self.create_user(email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self.db)

    return user


class User(AbstractBase, AbstractUser, PermissionsMixin):
  """ Custom user model that supports using email instead of username """
  email = models.EmailField(verbose_name='email_address', max_length=255, unique=True, null=False, blank=False)
  first_name = models.CharField(max_length=255, null=False, blank=False)
  last_name = models.CharField(max_length=255,  null=False, blank=False)
  other_names = models.CharField(max_length=255, null=True, blank=True)
  phone = models.CharField(max_length=255, blank=False, unique=True)
  national_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  objects = UserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'
    ordering = ('-created',)
