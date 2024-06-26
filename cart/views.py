from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from product.models import Product
from .forms import AddProductForm
from .cart import Cart

@require_POST
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # 데이터 처리
    form = AddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])
    
    return redirect('cart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def detail(request):
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'], 'is_update':True})
    
    is_empty = len(cart) == 0
    
    return render(request, 'cart/detail.html', {'cart': cart, 'is_empty': is_empty})
    
