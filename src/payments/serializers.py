from core.serializers import AbstractBaseSerializer
from core.models import RegisterUrl, Payment, ShortCode

class PaymentSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = Payment
    fields = ('name', 'description', 'image', )


class ShortCodeSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = ShortCode
    fields = ('name', 'description', 'image', )

  
class RegisterUrlSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = RegisterUrl
    fields = ('name', 'description', 'image', )