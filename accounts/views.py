from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import *
from .forms import *
# Create your views here.

def signuppage(req):
    if req.method == 'POST':
        form = capesignup(req.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('homepage')

            except Exception as e:
                print(e)
                return render(req,'accounts/Signup.html',{
                    'form': form,
                    'error': 'User already exists or DB error'
                })

        else:
            print(form.errors)
            return render(req,'accounts/Signup.html',{
                'form': form,
                'errors': form.errors
            })

    else:
        form = capesignup()
        return render(req,'accounts/Signup.html',{'form': form})


def loginpage(req):
    if req.method == 'POST':
        identifier = req.POST.get('identifier')
        password = req.POST.get('password')

        user = None

        if identifier.isdigit():
            user = capesign.objects.filter(mob=int(identifier)).first()
        else:
            user = capesign.objects.filter(email=identifier).first()

        if user and check_password(password, user.password):
            req.session['user_id'] = user.id 
            return redirect('homepage')

        return render(req,'accounts/login.html',{'error':'Invalid Data'})

    return render(req,'accounts/login.html')



def profile_page(request):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.age = request.POST.get("age")
        user.mob = request.POST.get("mob")
        user.email = request.POST.get("email")
        user.save()

        return redirect('/accounts/profile/')

    return render(request, 'accounts/profile.html', {'user': user})

def wishlist_page(request):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    wishlist_items = Wishlist.objects.filter(user=user)

    return render(request, 'accounts/wishlist.html', {
        'wishlist_items': wishlist_items
    })

def cart_page(request):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    cart_items = Cart.objects.filter(user=user)

    total = sum(item.total_price() for item in cart_items)

    return render(request, 'accounts/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def orders_page(request):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    orders = Order.objects.filter(user=user)

    return render(request, 'accounts/orders.html', {
        'orders': orders
    })

def logoutpage(request):
    request.session.flush()
    return redirect('/accounts/login/')

def add_to_cart(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])
    product = Product.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/accounts/cart/')

def add_to_wishlist(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])
    product = Product.objects.get(id=id)

    Wishlist.objects.get_or_create(
        user=user,
        product=product
    )

    return redirect('/accounts/wishlist/')

def buy_now(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])
    product = Product.objects.get(id=id)

    order = Order.objects.create(
        user=user,
        total_amount=product.price,
        status="Pending"
    )

    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=1,
        price=product.price
    )

    return redirect('/accounts/orders/')

def remove_from_cart(request, id):

    user = capesign.objects.get(id=request.session['user_id'])

    cart_item = get_object_or_404(Cart, id=id, user=user)

    cart_item.delete()

    return redirect('/accounts/cart/')

def increase_cart(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    cart_item = Cart.objects.get(id=id, user=user)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('/accounts/cart/')

def decrease_cart(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    cart_item = get_object_or_404(Cart, id=id, user=user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('/accounts/cart/')

def remove_from_wishlist(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    item = get_object_or_404(Wishlist, id=id, user=user)

    item.delete()

    return redirect('/accounts/wishlist/')

def cancel_product(request, id):

    if not request.session.get('user_id'):
        return redirect('/accounts/login/')

    user = capesign.objects.get(id=request.session['user_id'])

    ordered_item = get_object_or_404(Order, id=id, user=user)

    ordered_item.delete()

    return redirect('/accounts/orders/')

def edit_profile(request):
    user = request.user

    if request.method == "POST":
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.mob = request.POST.get('mob')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': user})