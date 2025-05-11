from django.shortcuts import render, get_object_or_404
from .models import Category
from .models import Product
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'catalog/category_detail.html', {'category': category})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'catalog/product_detail.html', {'product': product})
