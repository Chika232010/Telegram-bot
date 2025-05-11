from django.urls import path
from .views import view_cart,add_to_cart,update_cart,remove_from_cart
from . import views
app_name = 'cart'

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>/', update_cart, name='update_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.create_checkout_session, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
