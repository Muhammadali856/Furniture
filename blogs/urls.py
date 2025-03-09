from django.urls import path
from .views import blog_detail_view, BlogListViews

app_name = 'blogs'

urlpatterns = [
    path('', BlogListViews.as_view(), name='list'),
    path('detail/', blog_detail_view, name='detail'),
]