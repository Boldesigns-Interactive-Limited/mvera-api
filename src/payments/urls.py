from django.urls import path

from payments import views


app_name = 'payments'

urlpatterns = [
  path('payments/', views.CreatePaymentView.as_view(), name='payments'),
  path('registered_urls/', views.RegisterUrlView.as_view(), name='registered_urls'),
  path('short_codes/', views.CreateShortCodeView.as_view(), name='short_codes'),
]