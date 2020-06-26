from rest_framework import generics
from rest_framework.settings import api_settings

from core.models import Category, SubCategory, Product
from products.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CreateCategoryView(generics.ListCreateAPIView):
  """Creates a new user in the system"""
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class RetrieveUpdateRemoveCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  

class CreateSubCategoryView(generics.ListCreateAPIView):
  """Creates a new user in the system"""
  queryset = SubCategory.objects.all()
  serializer_class = SubCategorySerializer

class RetrieveUpdateRemoveSubCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = SubCategory.objects.all()
  serializer_class = SubCategorySerializer


class CreateProductView(generics.ListCreateAPIView):
  """Creates a new user in the system"""
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class RetrieveUpdateRemoveCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer