from django.shortcuts import render, redirect
from HomeAPP.models import ProductModel
from .models import BlogModel
from .forms import ProductModelForm
from django.contrib.auth import logout
from django.db.models import Sum
from django.contrib.auth.models import User
from .forms import BlogModelForm
from django.contrib.auth.decorators import user_passes_test, login_required

def is_staff(user):
    return user.is_staff

# Create your views here.
#================= Dashboard View ==================
@user_passes_test(is_staff, login_url='login')
def dashboard_view(request):
    count = ProductModel.objects.count()
    qty = ProductModel.objects.aggregate(total = Sum('quentity'))
    stock = qty['total']
    tempalte_name = "StaffAPP/staff_dashboard.html"
    context = {'count': count, 'stock': stock}
    return render(request, tempalte_name, context)


#================= Manage Products View ==================
@user_passes_test(is_staff, login_url='login')
def manage_products_view(request):
    template_name = "StaffAPP/manage_products.html"
    products = ProductModel.objects.all()
    context = {'products':products}
    return render(request, template_name, context)


#================= Add, Update, Delete Products View ==================
@user_passes_test(is_staff, login_url='login')
def add_product_view(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        print("your info is filed")
        if form.is_valid():
            print("info is valid")
            form.save()
            return redirect('manage_products')
    template_name = "StaffAPP/add_products.html"
    context = {'form': form}
    return render(request, template_name, context)

@user_passes_test(is_staff, login_url='login')
def update_product_view(request, i):
    product = ProductModel.objects.get(id= i)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_products')
    template_name = "StaffAPP/add_products.html"
    context = {'form': form}
    return render(request, template_name, context)

@user_passes_test(is_staff, login_url='login')
def delete_product_view(request, i):
    product = ProductModel.objects.get(id= i)
    product.delete()
    return redirect('manage_products')

@user_passes_test(is_staff, login_url='login')
def delete_product_confirmation_view(request, i):
    product = ProductModel.objects.get(id = i)
    template_name = 'StaffApp/delete_confirmation.html'
    context = {'product': product}
    return render(request, template_name, context)


#================= Customers View ==================
@user_passes_test(is_staff, login_url='login')
def customers_view(request):
    customers = User.objects.filter(is_superuser=False)
    template_name = "StaffAPP/customers.html"
    context = {'customers':customers}
    return render(request, template_name, context)


#================= Blog Views ==================
@user_passes_test(is_staff, login_url='login')
def add_blog_view(request):
    form = BlogModelForm()
    if request.method == 'POST':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    template_name = "StaffAPP/add_blog.html"
    context = {'form': form}
    return render(request, template_name, context)

@user_passes_test(is_staff, login_url='login')
def blogs_view(request):
    blogs = BlogModel.objects.all()
    template_name = "StaffAPP/blogs.html"
    context = {'blogs':blogs}
    return render(request, template_name, context)

@user_passes_test(is_staff, login_url='login')
def update_blog_view(request, i):
    blog = BlogModel.objects.get(id = i)
    form = BlogModelForm(instance = blog)
    if request.method == 'POST':
        form = BlogModelForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    template_name = "StaffAPP/add_blog.html"
    context = {'form': form}
    return render(request, template_name, context)

@user_passes_test(is_staff, login_url='login')
def delete_blog_view(request, i):
    blog = BlogModel.objects.get(id = i)
    blog.delete()
    return redirect('blogs')

@user_passes_test(is_staff, login_url='login')
def delete_blog_confirmation_view(request, i):
    blog = BlogModel.objects.get(id = i)
    template_name = "StaffAPP/blog_del_confirm.html"
    context = {'blog': blog}
    return render(request, template_name, context)

#================= Reports View ==================
@user_passes_test(is_staff, login_url='login')
def reports_view(request):
    template_name = "StaffAPP/reports.html"
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')