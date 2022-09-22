'''Added imports to start of file'''
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Views used for shopping Cart.


def view_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated quantity of {product.name} in {cart[item_id]}'
            )
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity in the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {product.name} in {cart[item_id]}'
            )
    else:
        cart.pop(item_id)
        messages.success(
            request, f'Removed quantity of {product.name} from cart'
            )

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('view_cart'))


def delete_cart(request, item_id):
    """Remove the item from the shopping cart"""
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    try:
        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from Shopping Cart'
            )

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
