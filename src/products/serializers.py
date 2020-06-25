from core.serializers import AbstractBaseSerializer
from core.models import Category, SubCategory, Product

class CategorySerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = Category
    fields = ('name', 'description', 'image', )


class SubCategorySerializer(AbstractBaseSerializer):
  """Serializes the Sub Category Object"""

  class Meta:
    model = SubCategory
    fields = ('category', 'name', 'description', 'image', )


class ProductSerializer(AbstractBaseSerializer):
  """ Serializes the Product Object """

  class Meta:
    model = Product
    fields = ('category', 'sub_category', 'name', 'description', 'price', 'image', )