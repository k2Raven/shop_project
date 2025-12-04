from django.shortcuts import get_object_or_404, redirect
from django.db.models import F, Sum
from django.views.generic import View, ListView, TemplateView

from webapp.models import Product, Cart
from webapp.forms import OrderForm

class AddProductToCartView(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        product = get_object_or_404(Product, pk=kwargs.get('pk'))

        if product.balance > 0:
            qty = 1
            print(cart)
            str_product_id = str(product.pk)
            if str_product_id in cart:
                if cart[str_product_id] < product.balance:
                    qty += cart[str_product_id]
                else:
                    qty = cart[str_product_id]
            cart[str_product_id] = qty

        request.session['cart'] = cart

        # if product.balance > 0:
        #     cart, created = Cart.objects.get_or_create(product=product)
        #     if not created and cart.qty < product.balance:
        #         cart.qty += 1
        #         cart.save()

        return redirect('product_list')


class CartView(TemplateView):
    template_name = 'cart/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_in_cart = []
        all_total = 0
        cart = self.request.session.get('cart', {})
        for product_id, qty in cart.items():
            product = Product.objects.get(pk=product_id)
            total = product.price * qty
            products_in_cart.append({'product': product, 'qty': qty, 'total': total})
            all_total += total
        print(products_in_cart)
        print(cart)
        context['products_in_cart'] = products_in_cart
        context['all_total'] = all_total
        context['form'] = OrderForm()
        return context

class DeleteProductFromCartView(View):
    def get(self, request, *args, **kwargs):
        product_id = str(kwargs.get('pk'))
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart.pop(product_id)

        request.session['cart'] = cart
        return redirect('cart')