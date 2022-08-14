def cart_contents(request):
    ''' Calculating total cost in shopping cart '''

    cart_items = []
    total = 0
    product_count = 0
    delivery = 7.99

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
