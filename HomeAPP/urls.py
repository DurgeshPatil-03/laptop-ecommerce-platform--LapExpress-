from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('products/', views.products_view, name='products'),
    path('deals/', views.deals_view, name='deals'),
    path('details/<id>/', views.product_details_view, name='details'),
    path('fblog/<i>/', views.first_blog_view, name='fblog'),
    path('cart/', views.cart_view, name = 'cart',),
    path('add_cart/<i>/', views.add_to_cart_view, name = 'add_cart',),
    path('update_cart/<i>/<action>/', views.update_cart_view, name = 'update_cart',),
    path('remove_cart/<i>/', views.remove_cart_item_view, name = 'remove_cart',),
]