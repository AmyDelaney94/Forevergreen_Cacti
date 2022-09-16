''' Documenting imports at the beginning of file '''
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    ''' Created view for checkout and redirect empty carts to products page '''
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LifPjG8ZOXHqvwWNC42MjHyaOBg05Q8qDhCCmwz5awtPgdHtZUjKzhk9nbJ776ggqQXWj5HrQ2n4DX6N0IF1xA9009cTykESV',
    }

    return render(request, template, context)
