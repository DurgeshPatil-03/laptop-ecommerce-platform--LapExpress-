from django.db import models
from django.contrib.auth.models import User


class ProductModel(models.Model):
    image = models.ImageField(upload_to='media/', default='media/default.png')
    brand = models.CharField(max_length=100, default='Unknown')
    model = models.CharField(max_length=100, default='Unknown')
    price = models.FloatField(default=0.0)
    processor = models.CharField(max_length=100, default='Not Specified')
    ram = models.IntegerField(default=0)
    rom = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, default="Unknow")
    display = models.FloatField(default=15.6)
    graphics = models.CharField(max_length=100, default='Integrated')
    os = models.CharField(max_length=100, default='Windows')
    review = models.CharField(max_length=100, default='No reviews yet')
    status = models.BooleanField(default=True)
    quentity = models.IntegerField(default=1)
    category = models.CharField(max_length=100, default='Laptop')
    def __str__(self):
        return self.model
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def item_total(self):
        return self.product.price * self.quantity