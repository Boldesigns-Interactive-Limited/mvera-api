from core.serializers import AbstractBaseSerializer
from core.models import Company, Estate, Block, Unit, Lease


class CompanySerializer(AbstractBaseSerializer):
  """Serializes the company object"""
  class Meta:
    model = Company
    fields = ('name', 'email', 'phone', 'physical_address')


class EstateSerializer(AbstractBaseSerializer):
  """Serializes the Estate Object"""
  class Meta:
    model = Estate
    fields = ('name', 'company', )


class BlockSerializer(AbstractBaseSerializer):
  """Serializes the Block Object"""
  class Meta:
    model = Block
    fields = ('name', 'company', 'estate', 'plot_no')

class UnitSerializer(AbstractBaseSerializer):
  """Serializes the Unit Object"""
  class Meta:
    model = Unit
    fields = ('block', 'number')

class LeaseSerializer(AbstractBaseSerializer):
  """Serializes the Lease Object"""
  class Meta:
    model = Lease
    fields = ('start', 'end', 'unit')
    
  