from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import  login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from random import randint
from django.contrib import messages

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Registered Successfully", extra_tags="success")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.", extra_tags="danger")
    template_name = "AuthAPP/register.html"
    context = {'form':form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == "POST":
        user = request.POST['username']
        pas = request.POST['password']
        user = authenticate(request, username = user, password = pas)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, "Admin logged in successfully", extra_tags="success")
                return redirect('admin_dashboard')
            if user.is_staff:
                messages.success(request, "Staff logged in successfully", extra_tags="success")
                return redirect('staff_dashboard')
            else:
                messages.success(request, "User logged in successfully", extra_tags="success")
                return redirect('home')
        else:
            messages.error(request, "Invalid Credentials", extra_tags="danger")
            return redirect('login')
    template_name = "AuthAPP/login.html"
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    messages.success(request, "logged out successfully", extra_tags="success")
    return redirect('home')

def forget_view(request):
    if request.method == "POST":
        context = {}

        action = request.POST.get('action')        

        if action == "generate_otp":
            email = request.POST.get('email')
            
            try:
                user = User.objects.get(email=email)
                
            except User.DoesNotExist:
                return HttpResponse("Email not registered")

            otp = str(randint(1000, 9999))
            request.session['email'] = email
            request.session['otp'] = otp

            send_mail(
                subject="Reset Passwod",
                message=f"OTP for reset Password {otp}",
                from_email="d.kshewal@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
            )

            messages.success(request, "OTP sent to your email", extra_tags="success")
            return render(request, "AuthAPP/forget.html", {"otp_sent": True})

        elif action == "verify_otp":
            user_otp = request.POST.get('OTP')
            gen_otp = request.session.get('otp')

            if user_otp == gen_otp:
                messages.success(request, "OTP verified successfully", extra_tags="success")
                return render(request, "AuthAPP/forget.html", {"otp_verified": True, })
            else:
                messages.error(request, "Invalid OTP", extra_tags="danger")
        
        elif action == "reset_password":
            pass1 = request.POST.get('new_password1')
            pass2 = request.POST.get('new_password2')
            if pass1 == pass2:
                email = request.session.get('email')
                user = User.objects.get(email=email)
                user.set_password(pass1)
                user.save()
                messages.success(request, "Password reset successfully", extra_tags="success")
                return redirect('login')
            else:
                messages.error(request, "Passwords do not match", extra_tags="danger")
            
    template_name = "AuthAPP/forget.html"
    context = {"load_email": True}
    return render(request, template_name, context)