from django.shortcuts import render


def product_checkout(request):
    return render(request, 'products/product-checkout.html')

def product_detail(request):
    return render(request, 'products/product-detail.html')

def product_grid_sidebar(request):
    return render(request, 'products/product-grid-sidebar-left.html')

