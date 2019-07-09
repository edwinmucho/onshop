from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def product_in_category(request, category_slug=None):
    current_category = None

    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    passon = {
        'current_category': current_category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/list.html', passon)


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)

    passon = {
        'product':product
    }
    return render(request, 'shop/detail.html', passon)