from rest_framework import generics
from rest_framework.settings import api_settings

from core.models import Payment, RegisterUrl, ShortCode
from payments.serializers import PaymentSerializer, RegisterUrlSerializer, ShortCodeSerializer


class CreatePaymentView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = Payment.objects.all()
  serializer_class = PaymentSerializer

class RegisterUrlView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = RegisterUrl.objects.all()
  serializer_class = RegisterUrlSerializer

class CreateShortCodeView(generics.CreateAPIView):
  """Creates a new user in the system"""
  queryset = ShortCode.objects.all()
  serializer_class = ShortCodeSerializer