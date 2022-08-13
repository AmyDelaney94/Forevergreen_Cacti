''' Adding Imports to beggining of file '''
from django.contrib import admin
from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    '''Display of products section of admin site'''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('-sku',)


class CategoryAdmin(admin.ModelAdmin):
    '''Display of categories section of admin site'''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
