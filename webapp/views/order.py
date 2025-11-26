from django.views.generic import View
from django.shortcuts import redirect

from webapp.models import Order, Cart
from webapp.forms import OrderForm

class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for cart in Cart.objects.all():
                order.order_products.create(product=cart.product, qty=cart.qty)
                cart.delete()
        return redirect('cart')
