''' Loading imports at beginning of file '''
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': user_profile,
    }

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    '''
        view to display users order history
    '''
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """ View for user Wishlist """
    user = UserProfile.objects.get(user=request.user)

    return render(request,
                  "profiles/wishlist.html",
                  {"wishlist": user.product_wishlist})


@login_required
def add_to_wishlist(request, id):
    """ View to add and remove products from Wishlist """
    product = get_object_or_404(Product, id=id)

    user = UserProfile.objects.get(user=request.user)

    if user.product_wishlist.filter(id=product.id).exists():
        user.product_wishlist.remove(product)
        messages.success(request, product.name +
                         " has been removed from your WishList")
    else:
        user.product_wishlist.add(product)
        messages.success(request, "Added " + product.name +
                         " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
