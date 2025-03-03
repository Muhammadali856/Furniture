from django.urls import path
from .views import product_cart, product_checkout, product_detail, product_grid_sidebar

app_name = 'products'

urlpatterns = [
    path('', product_cart, name='product_cart'),
    path('checkout/',product_checkout, name='checkout'),
    path('detail/', product_detail, name='detail'),
    path('grid_sidebar/', product_grid_sidebar, name='grid_sidebar'),
]