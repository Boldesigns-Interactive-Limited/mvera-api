from core.serializers import AbstractBaseSerializer
from core.models import RegisterUrl, Payment, ShortCode

class PaymentSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = Payment
    fields = ('transaction_type', 'transaction_id', 'transaction_time', 'transaction_amount', 'short_code', 'bill_ref_number', 'org_account_balance', 'third_party_trans_id', 'msisdb', 'first_name', 'middle_name', 'last_name', 'confirm')


class ShortCodeSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = ShortCode
    fields = ('company', 'short_code', 'organization_name', 'mpesa_user_name', 'consumer_key', 'consumer_secret', 'verified', 'pass_key')

  
class RegisterUrlSerializer(AbstractBaseSerializer):
  """ Serializes the Category Object """

  class Meta:
    model = RegisterUrl
    fields = ('shortcode', 'confirmation', 'validation', 'response_description', 'response_type')