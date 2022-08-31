''' Adding Imports to beggining of file '''
from django.contrib import admin
from .models import Order, CartItem


class CartItemAdminInline(admin.TabularInline):
    '''
    Readonly fields added to ensure cart items cannot be edited.
    Admin can edit items
    '''
    model = CartItem
    readonly_fields = ('cart_total',)


class OrderAdmin(admin.ModelAdmin):
    '''
    View for admin view of shopping cart.
    Readonly fields added to ensure cart items cannot be edited
    '''
    inlines = (CartItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'total', 'grand_total',)

    fields = ('order_number', 'date', 'username',
              'email', 'mobile', 'address_line1',
              'address_line2', 'town_or_city', 'county',
              'eircode', 'total', 'delivery_cost', 'grand_total'
              )

    list_display = ('order_number', 'date', 'username',
                    'total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
