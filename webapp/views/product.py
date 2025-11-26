from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product
from webapp.forms import ProductForm, SimpleSearchForm


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['category__title', 'title']

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        search_value = ''
        if self.search_form.is_valid():
            search_value = self.search_form.cleaned_data.get('search', '')
        return search_value

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = self.search_form
        if self.search_value:
            context['search_value'] = self.search_value
            context['query'] = urlencode({'searh': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(balance=0)
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    queryset = Product.objects.exclude(balance=0)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    queryset = Product.objects.exclude(balance=0)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('product_list')
    queryset = Product.objects.exclude(balance=0)