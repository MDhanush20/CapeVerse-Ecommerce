from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product


def productpage(request):

    categories = Category.objects.all()
    new_products = Product.objects.order_by('-updated_at')[:8]
    products = Product.objects.all()

    wishlist_ids = []

    if request.user.is_authenticated:
        wishlist_ids = request.user.wishlist_set.values_list('product_id', flat=True)

    return render(request, 'products/products.html', {
        'categories': categories,
        'new_products': new_products,
        'products': products,
        'wishlist_ids': wishlist_ids,
    })


def category_page(request, id):

    category = get_object_or_404(Category, id=id)

    products = Product.objects.filter(category=category)

    return render(request, 'products/category.html', {
        'category': category,
        'products': products
    })


def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    return render(request, 'products/product_detail.html', {
        'product': product
    })

def search_products(request):
    query = request.GET.get('q', '')

    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    )

    return render(request, 'products/products.html', {
        'products': products,
        'query': query,
    })