from rest_framework import serializers

from .models import AbstractBase

class AbstractBaseSerializer(serializers.ModelSerializer):
  """Serialize the AbstractBase Object """

  class Meta:
    model = AbstractBase
    fields = ('id', 'created', 'updated', 'is_active', 'created_by', 'updated_by', )
    abstract = True
