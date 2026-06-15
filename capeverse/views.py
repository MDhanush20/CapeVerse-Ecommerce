from django.shortcuts import render,redirect
from .models import *
from .forms import *
from products.models import *
# Create your views here.
def homepage(req):
    categories = Category.objects.all()
    trending = Product.objects.order_by('-updated_at')[:8]

    return render(req, 'home.html', {
        'categories': categories,
        'trending': trending
    })