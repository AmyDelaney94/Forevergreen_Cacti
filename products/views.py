""" Adding Imports to beggining of file """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models.functions import Lower
from django.views.generic import UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Product, Category, Review
from .forms import ReviewForm


# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            # Allows user to search by name in upper or lower case
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                # If results are decending flip to acesnding
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            # Allows filter of products by individual categories
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            # Activates the search bar and shows user error message
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter a valid search!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


@login_required
def product_detail(request, product_id):
    """ A view to show individual products when selected """

    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()
    reviews = Review.objects.filter(product=product)

    if request.method == "POST":
        r_f = ReviewForm(request.POST)
        # create a view to see reviews
        if r_f.is_valid():
            your_review = request.POST.get("your_review")
            reviews = Review.objects.create(product=product,
                                            name=request.user,
                                            your_review=your_review)
            reviews.save()
            return HttpResponseRedirect(request.META["HTTP_REFERER"])

        else:
            r_f = ReviewForm()

        context = {
            "product": product,
            "review_form": r_f,
            "reviews": reviews
        }

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
        # return render(request, "products/product_detail.html", context)

    context = {
            "product": product,
            "review_form": ReviewForm(),
            "reviews": reviews
        }

    return render(request, "products/product_detail.html", context)


class UpdateReview(UpdateView):
    '''
    View to update a review if user is logged in.
    '''
    model = Review
    template_name = 'review_form.html'
    form_class = ReviewForm()
    success_url = "products/product_detail.html"


class DeleteReview(DeleteView):
    '''
    View to delete a review
    '''
    model = Review
    template_name = 'products/review_delete.html'
    success_url = reverse_lazy('home')
