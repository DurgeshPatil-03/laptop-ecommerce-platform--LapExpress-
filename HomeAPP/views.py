from django.shortcuts import render, redirect
from .models import ProductModel, Cart, CartItem
from StaffAPP.models import BlogModel
from  django.contrib.auth.decorators import login_required

def home_view(request):
    template_name = "HomeAPP/index.html"
    context = {}
    return render(request, template_name, context)

def about_view(request):
    template_name = "HomeAPP/about.html"
    context = {}
    return render(request, template_name, context)

def services_view(request):
    template_name = "HomeAPP/services.html"
    context = {}
    return render(request, template_name, context)

def blog_view(request):
    blogs = BlogModel.objects.all()
    template_name = "HomeAPP/blog.html"
    context = {'blogs':blogs}
    return render(request, template_name, context)

def first_blog_view(request, i):
    blogs = BlogModel.objects.get(id = i)
    if not blogs:
        return redirect('blog')
    template_name = "HomeAPP/first_blog.html"
    context = {'blogs':blogs}
    return render(request, template_name, context)

def contact_view(request):
    template_name = "HomeAPP/contact.html"
    context = {}
    return render(request, template_name, context)

def deals_view(request):
    template_name = "HomeAPP/deals.html"
    context = {}
    return render(request, template_name, context)

def product_details_view(request, id):
    laptop = ProductModel.objects.get(id = id)
    if not laptop:
        return redirect('products')
    template_name = "HomeAPP/product_details.html"
    context = {"laptop": laptop}
    return render(request, template_name, context)

def products_view(request):
    laptop = ProductModel.objects.all()
    template_name = "HomeAPP/products.html"
    context = {"laptop": laptop}
    return render(request, template_name, context)

# ==========Cart Views===========

def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return cart

@login_required(login_url='login')
def cart_view(request):
    cart = get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = 0
    items = 0
    for item in cart_items:
        total_price += item.item_total()
        items += item.quantity
        
    delivery_charge = 0
    if total_price < 50000:
        delivery_charge = 250

    total = total_price + delivery_charge

    template_name = "HomeAPP/cart.html"
    context = { "cart_items": cart_items, "total_price": total_price, "delivery_charge": delivery_charge, "total": total, "items": items }
    return render(request, template_name, context)

@login_required(login_url='login')
def add_to_cart_view(request, i):
    product = ProductModel.objects.get(id=i)
    cart = get_cart(request)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=1
        )

    return redirect('cart')

@login_required(login_url='login')
def update_cart_view(request, i, action):
    cart = get_cart(request)
    cart_item = CartItem.objects.get(id=i, cart=cart)

    if action == "increase":
        cart_item.quantity += 1
        cart_item.save()

    if action == "decrease":
        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()
        else:
            cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def remove_cart_item_view(request, i):
    cart = get_cart(request)
    CartItem.objects.get(id=i, cart=cart).delete()
    return redirect('cart')