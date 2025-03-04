from django.shortcuts import render

def home_page_view(request):
    return render(request, template_name='home3.html')

def contact_page_view(request):
    return render(request, template_name='pages/contact.html')

def about_page_view(request):
    return render(request, template_name='pages/about-us.html')