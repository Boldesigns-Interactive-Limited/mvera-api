from django.urls import path

from products import views


app_name = 'products'

urlpatterns = [
  path('categories/', views.CreateCategoryView.as_view(), name='categories'),
  path('sub_categories/', views.CreateSubCategoryView.as_view(), name='sub_categories'),
  path('products/', views.CreateProductView.as_view(), name='products'),
]