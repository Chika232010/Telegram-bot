from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm

def apply_coupon(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST or None)
    message = ""
    
    if request.method == 'POST' and form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, active=True,
                                        valid_from__lte=now, valid_to__gte=now)
            request.session['coupon_id'] = coupon.id
            message = f"Купон {coupon.code} применён! Скидка {coupon.discount}%"
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            message = "Купон недействителен"
    
    return render(request, 'coupon/apply.html', {'form': form, 'message': message})
 