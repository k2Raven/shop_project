from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title

from webapp.models import Category, Product

def product_list_view(request):
    products = Product.objects.exclude(balance=0).order_by('category__title', 'title')
    return render(request, 'product_list.html', {'products': products})

def product_create_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image_url')
        category_id = request.POST.get('category_id')
        product = Product.objects.create(title=title, description=description, price=price, image=image, category_id=category_id)
        return redirect('product_detail', pk=product.pk)

    return render(request, 'article_create.html', {'categories': categories})

def product_detail_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'article_detail.html', {'product': product})


def category_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Category.objects.create(title=title, description=description)
        return redirect('product_list')
    return render(request, 'category_create.html')