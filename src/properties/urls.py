from django.urls import path

from properties import views


app_name = 'properties'

urlpatterns = [
  path('companies/', views.CreateCompanyView.as_view(), name='company'),
  path('estates/', views.CreateEstateView.as_view(), name='estate'),
  path('blocks/', views.CreateBlockView.as_view(), name='block'),
  path('units/', views.CreateUnitView.as_view(), name='block'),
  path('leases/', views.CreateLeaseView.as_view(), name='block'),
]