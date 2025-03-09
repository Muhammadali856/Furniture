from django.shortcuts import render
from django.views.generic import ListView
from blogs.models import BlogModel



def blog_detail_view(request):
     return render(request, template_name='blogs/blog-detail.html')

class BlogListViews(ListView):
    template_name = 'blogs/blog-list-sidebar-left.html'
    model = BlogModel
    context_object_name = 'blogs'