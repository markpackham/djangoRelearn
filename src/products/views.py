from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)
