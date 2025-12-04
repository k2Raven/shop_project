from django.views.generic import View
from django.shortcuts import redirect

from webapp.models import Order, Cart
from webapp.forms import OrderForm

class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        carts = self.request.session.get('cart', {})
        if form.is_valid() and carts:
            order = form.save()

            for product_id, qty in carts.items():
                order.order_products.create(product_id=product_id, qty=qty)
            request.session['cart'] = {}
        return redirect('cart')
