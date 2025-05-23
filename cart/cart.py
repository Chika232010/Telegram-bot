from decimal import Decimal
from django.conf import settings
from catalog.models import Product
from coupons.models import Coupon

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSIONS_ID] = {}
        self.cart = cart
        self.coupon_id = self.sessions.get("coupon_id")

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
            return None
    def get_discount(self):
        if self.coupon:
            return(self.coupon.discount / Decimal(100)) * self.get_total_price()
        return Decimal(0)
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
    def add(self, product, quatity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in  self.cert:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price)
            }
        if override_quantity:
            self.card[product_id]["quantity"] = quatity
        else:
            self.cart[product_id]["quantity"] += quatity
        self.save()
    def save(self):
        self.session.modified = True
    def removed(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save
    def __init__(self):
        product_ids = self.card.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item
    def __len__(self):
        return sum(item["quantity"] for item in self.cart())
    
    def get_total_price(self):
        return sum(Decimal(item["price"] * item["quanatily"]) for item in self.cart.values())
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()