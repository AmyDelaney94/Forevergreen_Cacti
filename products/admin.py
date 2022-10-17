''' Adding Imports to beggining of file '''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Product, Review

# Register your models here.


class ProductAdmin(SummernoteModelAdmin):
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


class ReviewAdmin(admin.ModelAdmin):
    """Class to display reviews on admin site"""
    list_display = ('name', 'your_review', 'product', 'date_posted')
    list_filter = ('date_posted', 'name')
    search_fields = ('name', 'your_review')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
