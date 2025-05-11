import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from catalog.models import Product

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.subtotal() for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def update_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    if 'quantity' in request.POST:
        cart_item.quantity = int(request.POST['quantity'])
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('view_cart')


def create_checkout_session(request):
    cart = Cart(request)
    items = []

    for item in cart:
        product = item['product']
        items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': item['quantity'],
        })

    if not items:
        return redirect('cart:cart_detail')

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://localhost:8000/cart/success/',
        cancel_url='http://localhost:8000/cart/cancel/',
    )

    return redirect(session.url, code=303)




def payment_success(request):
 
    request.session['cart'] = {}
    return render(request, 'cart/payment_success.html')
def payment_cancel(request):
    return render(request, 'cart/payment_cancel.html')
