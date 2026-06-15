from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signuppage, name='Signuppage'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logoutpage, name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('wishlist/', views.wishlist_page, name='wishlist'),
    path('cart/', views.cart_page, name='cart'),
    path('orders/', views.orders_page, name='orders'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('buy-now/<int:id>/', views.buy_now, name='buy_now'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('wishlist/remove/<int:id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('cart/increase/<int:id>/', views.increase_cart, name='increase_cart'),
    path('cart/decrease/<int:id>/', views.decrease_cart, name='decrease_cart'),
    path('cancel_product/<int:id>/', views.cancel_product, name='cancel_product'),
    path('edit-profile/', views.edit_profile, name='edit_profile')
    
]