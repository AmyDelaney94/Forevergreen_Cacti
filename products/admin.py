''' Adding Imports to beggining of file '''
from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)