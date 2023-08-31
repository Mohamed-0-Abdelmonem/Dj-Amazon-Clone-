from django.urls import path
from .views import ProductList, ProductDetail, BrandList

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view(), name='brand_list'),
]