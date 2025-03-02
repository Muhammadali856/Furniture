from django.shortcuts import render

def blog_list_view(request):
    return render(request, template_name='blogs/blog-list-sidebar-left.html')

def blog_detail_view(request):
     return render(request, template_name='blogs/blog-detail.html')