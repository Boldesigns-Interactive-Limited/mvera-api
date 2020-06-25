from rest_framework import generics
from rest_framework.settings import api_settings

from core.models import Company, Estate, Block, Unit, Lease
from properties.serializers import CompanySerializer ,EstateSerializer, BlockSerializer, UnitSerializer, LeaseSerializer


class CreateCompanyView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = Company.objects.all()
  serializer_class = CompanySerializer

class CreateEstateView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = Estate.objects.all()
  serializer_class = EstateSerializer

class CreateBlockView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = Block.objects.all()
  serializer_class = BlockSerializer
  

class CreateUnitView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer
  

class CreateLeaseView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = Lease.objects.all()
  serializer_class = LeaseSerializer
