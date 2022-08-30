'''Added imports to start of file'''
from django.shortcuts import render, redirect, reverse, HttpResponse

# Views used for shopping Cart.


def view_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the quantity in the shopping cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('view_cart'))


def delete_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        quantity = None
        if 'product_quantity' in request.POST:
            quantity = request.POST['product_quantity']
            cart = request.session.get('cart', {})

        if quantity:
            del cart[item_id]['product_quantity']
            if not cart[item_id]['product_quantity']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
