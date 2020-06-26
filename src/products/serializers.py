from core.serializers import AbstractBaseSerializer
from core.models import Category, SubCategory, Product

class CategorySerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = Category
    fields = '__all__'


class SubCategorySerializer(AbstractBaseSerializer):
  """Serializes the Sub Category Object"""

  class Meta:
    model = SubCategory
    fields = '__all__'


class ProductSerializer(AbstractBaseSerializer):
  """ Serializes the Product Object """

  class Meta:
    model = Product
    fields = '__all__'