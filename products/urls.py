from django.urls import path
from .views import product_checkout, product_detail, product_grid_sidebar

app_name = 'products'

urlpatterns = [
    path('detail/', product_detail, name='detail'),
    path('grid_sidebar/', product_grid_sidebar, name='grid_sidebar'),
]