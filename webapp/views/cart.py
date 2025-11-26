from django.shortcuts import get_object_or_404, redirect
from django.db.models import F, Sum
from django.views.generic import View, ListView

from webapp.models import Product, Cart
from webapp.forms import OrderForm

class AddProductToCartView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        if product.balance > 0:
            cart, created = Cart.objects.get_or_create(product=product)
            if not created and cart.qty < product.balance:
                cart.qty += 1
                cart.save()

        return redirect('product_list')


class CartView(ListView):
    model = Cart
    template_name = 'cart/index.html'
    context_object_name = 'products_in_cart'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(total=F('product__price') * F('qty'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_total'] = self.get_queryset().aggregate(Sum('total'))['total__sum']
        context['form'] = OrderForm()
        return context

class DeleteProductFromCartView(View):
    def get(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, pk=kwargs.get('pk'))
        cart.delete()
        return redirect('cart')