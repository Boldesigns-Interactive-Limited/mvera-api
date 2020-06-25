from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from core.serializers import AbstractBaseSerializer

class UserSerializer(AbstractBaseSerializer):
  """Serializers for the users object"""

  class Meta:
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name', 'other_names', 'phone', 'national_id', 'photo', 'is_admin', 'is_staff', 'is_superuser')
    extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5}}

  def create(self, validated_data):
    """Create a new user with encrypted password and return it"""
    return get_user_model().objects.create_user(**validated_data)



class AuthTokenSerializer(serializers.ModelSerializer):
  """Serializers for the user authentication object"""
  email = serializers.EmailField()
  password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

  class Meta:
    model = get_user_model()
    fields = ('email', 'password')

  def validate(self, attrs):
    """Validate and authenticate the user"""
    email = attrs.get('email')
    password = attrs.get('password')

    user = authenticate(request = self.context.get('request'), username=email, password=password)

    if not user:
      msg = _('Unable to authenticate with provided credentials')
      raise serializers.ValidationError(msg, code='authentication')

    attrs['user'] = user
    return attrs