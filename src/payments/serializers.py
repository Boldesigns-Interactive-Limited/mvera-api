from core.serializers import AbstractBaseSerializer
from core.models import RegisterUrl, Payment, ShortCode

class PaymentSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = Payment
    fields = '__all__'


class ShortCodeSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = ShortCode
    fields = '__all__'
  
class RegisterUrlSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = RegisterUrl
    fields = '__all__'