from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import AddCouponForm

@require_POST
def add_coupon(request):
    now = timezone.now()
    form = AddCouponForm(request.POST)

    if form.is_valid():
        code = form.cleaned_data['code']

        try:
            coupon = Coupon.objects.get(code__iexact=code, use_from__lte=now, use_to__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
            
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()

    for item in cart:
        init_item = {
        'quantity':item['quantity'],
        'is_update':True
        }

        item['quantity_form'] = AddProductForm(initial=init_item)

    passon = {
        'cart': cart,
        'add_coupon': add_coupon
    }
    return render(request, 'cart/detail.html', passon)
