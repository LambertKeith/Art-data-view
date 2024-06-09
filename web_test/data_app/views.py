from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    filters = {}
    
    for key, value in request.GET.items():
        if value:
            filters[key + '__icontains'] = value
    
    if filters:
        products = products.filter(**filters)
    
    context = {
        'products': products,
        'filters': request.GET
    }
    
    return render(request, 'product_list.html', context)
