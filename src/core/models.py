import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, \
                                                      PermissionsMixin

from config.settings import AUTH_USER_MODEL

USER_TYPE = (
  ('TENANT', 'TENANT'),
  ('MANAGER', 'MANAGER')
)

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

  def _create_user(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
    """ Creates and saves a User with a given email and password """

    if not email:
      raise ValueError('Users must have an email address')

    user = self.model(email=self.normalize_email(email), is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    """Creates a normal user"""
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    """ Creates a new super user """
    return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBase, AbstractUser, PermissionsMixin):
  """ Custom user model that supports using email instead of username """
  email = models.EmailField(verbose_name='email_address', max_length=255, unique=True, null=False, blank=False)
  first_name = models.CharField(max_length=255, null=False, blank=False)
  last_name = models.CharField(max_length=255,  null=False, blank=False)
  other_names = models.CharField(max_length=255, null=True, blank=True)
  phone = models.CharField(max_length=255, blank=False, unique=True)
  national_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
  photo = models.URLField(null=True, blank=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  objects = UserManager()

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'
    ordering = ('-created',)


class AccessToken(AbstractBase):
  token = models.CharField(max_length=255, null=True, blank=True)
  expires_in = models.IntegerField(null=True, blank=True)

class Profile(AbstractBase):
  user = models.OneToOneField(User, related_name='user_profile', on_delete=models.PROTECT)
  type = models.CharField(choices=USER_TYPE, max_length=21, default='TENANT')
  national_id = models.CharField(max_length=21, blank=True, null=True)

  class Meta:
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    ordering = ('-created',)

class Company(AbstractBase):
  name = models.CharField(max_length=255, blank=True, null=True)
  email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
  phone = models.CharField(max_length=21, blank=True, null=True)
  physical_address = models.CharField(max_length=255, blank=True, null=True)

  class Meta:
    verbose_name = 'Company'
    verbose_name_plural = 'Companies'
    ordering = ('-created',)

  def __str__(self):
    return self.name


class Estate(AbstractBase):
  company = models.ForeignKey(Company, related_name='estate_owner', blank=False, null=False, on_delete = models.PROTECT)
  name = models.CharField(max_length=21, blank=False, null=False)

  class Meta:
    verbose_name = 'Estate'
    verbose_name_plural = 'Estates'
    ordering = ('-created',)

  def __str__(self):
    return self.name
    

class Block(AbstractBase):
  company = models.ForeignKey(Company, related_name='block_company', null=True, blank=True, on_delete=models.PROTECT)
  estate = models.ForeignKey(Estate, related_name='block_estate', null=True, blank=True, on_delete=models.PROTECT)
  plot_no = models.CharField(max_length=255, blank=True, null=True)
  name = models.CharField(max_length=255, null=True)

  class Meta:
    verbose_name = 'Block'
    verbose_name_plural = 'Blocks'
    ordering = ('-created',)

class Unit(AbstractBase):
  block = models.ForeignKey(Block, related_name='unit_block', null=True, blank=True, on_delete=models.PROTECT)
  number = models.CharField(max_length=21, blank=False, null=False)
  
  class Meta:
    unique_together = (('block', 'number'))
    verbose_name = 'Unit'
    verbose_name_plural = 'Units'
    ordering = ('-created',)

class Lease(AbstractBase):
  unit = models.ForeignKey(Unit, related_name='unit_lease', null=True, blank=True, on_delete=models.PROTECT)
  start = models.DateTimeField(null=True, blank=True)
  end = models.DateTimeField(null=True, blank=True)

class Category(AbstractBase):
  name = models.CharField(max_length=255, blank=False, null=False)
  description = models.TextField(blank=True, null=True)
  image = models.URLField(blank=True, null=True)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    ordering = ('-created',)

  def ___str__(self):
    return self.name

class SubCategory(AbstractBase):
  category = models.ForeignKey(Category, related_name='category_name', null=True, blank=True, on_delete=models.PROTECT)
  name = models.CharField(max_length=255, blank=False, null=False)
  description = models.TextField(blank=True, null=True)
  image = models.URLField(blank=True, null=True)

  class Meta:
    verbose_name = 'Sub Category'
    verbose_name_plural = 'Sub Categories'
    ordering = ('-created',)

  def ___str__(self):
    return self.name

class Product(AbstractBase):
  category = models.ForeignKey(Category, related_name='product_category', null=True, blank=True, on_delete=models.PROTECT)
  sub_category = models.ForeignKey(SubCategory, related_name='product_category', null=True, blank=True, on_delete=models.PROTECT)
  name = models.CharField(max_length=255, null=False, blank=False)
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=21, decimal_places=2, default=0.00)
  image = models.URLField(blank=True, null=True)

  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    ordering = ('-created',)

  def ___str__(self):
    return self.name


class RegisterUrl(AbstractBase):
  shortcode = models.CharField(max_length=21, null=True)
  confirmation = models.URLField()
  validated = models.URLField()
  response_description = models.CharField(max_length=1000)
  response_type = models.CharField(max_length=21)

  def __str__(self):
    return self.confirmation

class Payment(AbstractBase):
  transction_type = models.CharField(max_length=21, null=True, blank=True)
  transction_id = models.CharField(max_length=21, null=True, blank=True)
  transaction_time = models.CharField(max_length=21, null=True, blank=True)
  transaction_amount = models.DecimalField(max_digits=21, decimal_places=2, default=0.00)
  short_code = models.CharField(max_length=21, blank=True, null=True)
  bill_ref_number = models.CharField(max_length=21, blank=True, null=True)
  org_account_balance = models.CharField(max_length=21, blank=True, null=True)
  third_party_trans_id = models.CharField(max_length=21, blank=True, null=True)
  msisdb = models.CharField(max_length=21, blank=True, null=True)
  first_name = models.CharField(max_length=21, blank=True, null=True)
  middle_name = models.CharField(max_length=21, blank=True, null=True)
  last_name = models.CharField(max_length=21, blank=True, null=True)
  confirm = models.BooleanField(default=False)

  class Meta:
    verbose_name = 'Payment'
    verbose_name_plural = 'Payments'
    ordering = ('-created',)

class ShortCode(AbstractBase):
  owner = models.ForeignKey(AUTH_USER_MODEL, related_name='short_code_name', blank=True, null=True, on_delete=models.PROTECT)
  company = models.ForeignKey(Company, related_name='company_of_short_code', null=True, blank=True, on_delete=models.PROTECT)
  short_code = models.CharField(max_length=21, blank=True, null=True)
  organization_name = models.CharField(max_length=100, blank=True, null=True)
  mpesa_user_name = models.CharField(max_length=21, blank=True, null=True)
  consumer_key = models.CharField(max_length=999, blank=True, null=True)
  consumer_secret = models.CharField(max_length=21, blank=True, null=True)
  verified = models.BooleanField(default=False)
  pass_key = models.CharField(max_length=255, blank=True, null=True, unique=True )

  def is_verified(self):
    if self.verified:
      return 'YES'
    return 'PENDING'

  def __str__(self):
    return str(self.short_code)