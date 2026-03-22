from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='staff_dashboard'),
    path('manage/', views.manage_products_view, name='manage_products'),
    path('add/', views.add_product_view, name='add_product'),
    path('update/<i>/', views.update_product_view, name='update_product'),
    path('delete/<i>/', views.delete_product_view, name='delete_product'),
    path('delete_confirmation/<i>/', views.delete_product_confirmation_view, name='delete_confirmation'),
    path('customers/', views.customers_view, name='customers'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('addblog/', views.add_blog_view, name='add_blog'),
    path('updateblog/<i>/', views.update_blog_view, name='update_blog'),
    path('deleteblog/<i>/', views.delete_blog_view, name='delete_blog'),
    path('blog_del_confirm/<i>/', views.delete_blog_confirmation_view, name='delete_blog_confirmation'),
    path('reports/', views.reports_view, name='reports'),
    path('logout/', views.logout_view, name='staff_logout'),
]