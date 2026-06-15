from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.productpage,name='productpage'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('category/<int:id>/', views.category_page, name='category_page'),
    path('search/', views.search_products, name='search_products'),
    
]
