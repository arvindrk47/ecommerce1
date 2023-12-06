from django.urls import re_path,path,include
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>', views.store, name='product_by_category'),
]