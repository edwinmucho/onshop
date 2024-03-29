from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import AddProductForm


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

    # 제품 설명에서는 Update False
    add_to_cart = AddProductForm(initial={'quantity': 1})

    passon = {
        'product':product,
        'add_to_cart': add_to_cart
    }
    return render(request, 'shop/detail.html', passon)
