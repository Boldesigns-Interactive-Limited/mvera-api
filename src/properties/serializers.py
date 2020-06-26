from core.serializers import AbstractBaseSerializer
from core.models import Company, Estate, Block, Unit, Lease


class CompanySerializer(AbstractBaseSerializer):
  """Serializes the company object"""
  class Meta:
    model = Company
    fields = '__all__'


class RetrieveUpdateRemoveCompany(generics.RetrieveUpdateDestroyAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer


class EstateSerializer(AbstractBaseSerializer):
  """Serializes the Estate Object"""
  class Meta:
    model = Estate
    fields = '__all__'


class RetrieveUpdateRemoveEstate(generics.RetrieveUpdateDestroyAPIView):
  queryset = Estate.objects.all()
  serializer_class = EstateSerializer


class BlockSerializer(AbstractBaseSerializer):
  """Serializes the Block Object"""
  class Meta:
    model = Block
    fields = '__all__'

class RetrieveUpdateRemoveBlock(generics.RetrieveUpdateDestroyAPIView):
  queryset = Block.objects.all()
  serializer_class = BlockSerializer

class UnitSerializer(AbstractBaseSerializer):
  """Serializes the Unit Object"""
  class Meta:
    model = Unit
    fields = '__all__'


class RetrieveUpdateRemoveUnit(generics.RetrieveUpdateDestroyAPIView):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer

class LeaseSerializer(AbstractBaseSerializer):
  """Serializes the Lease Object"""
  class Meta:
    model = Lease
    fields = '__all__'


class RetrieveUpdateRemoveLease(generics.RetrieveUpdateDestroyAPIView):
  queryset = Lease.objects.all()
  serializer_class = LeaseSerializer