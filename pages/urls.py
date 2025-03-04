from django.urls import path
from .views import home_page_view, contact_page_view, about_page_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_page_view, name='contact'),
    path('about/', about_page_view, name='about'),
]