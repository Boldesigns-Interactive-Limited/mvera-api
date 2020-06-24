from django.urls import path

from users import views


app_name = 'users'

urlpatterns = [
  path('create/', views.CreateView.as_view(), name='create'),
  path('token/', views.CreateAuthTokenView.as_view(), name='token'),
]