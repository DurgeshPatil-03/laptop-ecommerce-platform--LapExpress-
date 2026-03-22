from django import forms
from .models import BlogModel
from HomeAPP.models import ProductModel

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = "__all__"

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"