from django.shortcuts import render, redirect
from webapp.models import Category, Product

def product_list_view(request):
    products = Product.objects.all()
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
        return redirect('product_list')

    return render(request, 'article_create.html', {'categories': categories})
