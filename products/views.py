""" Adding Imports to beggining of file """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    if request.method == "POST":
        rf = ReviewForm(request.POST)
        # create a view to see reviews
        if rf.is_valid():
            your_review = request.POST.get("your_review")
            review = Review.objects.create(product=product,
                                           name=request.user,
                                           your_review=your_review)
            review.save()
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
            # return redirect(review.get_absolute_url())
        else:
            rf = ReviewForm()

        context = {
            "product": product,
            "review_form": rf,
        }

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
        # return render(request, "products/product_detail.html", context)

    context = {
            "product": product,
            "review_form": rf,
        }

    return render(request, "products/product_detail.html", context)


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class to allow logged in users to update their reviews """

    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        """
        Function to set signed in user
        as author of the review form to post
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        To set test_func to ensure only the author of the review can update it
        and show 403 forbidden if url entered by another user
        """
        review = self.get_object()
        if self.request.user == review.name:
            return True
        return False

    def get_success_url(self):
        """ On successful review update, return to product_detail view"""
        product = self.object.product
        messages.success(self.request, "Your Review Was Successfully Updated")
        return reverse_lazy("product_detail.html")


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allow author to delete review.
    """

    model = Review

    def test_func(self):
        """
        To set test_func to ensure only the author of the review can delete it
        and show 403 forbidden if url entered by another user
        """
        review = self.get_object()
        if self.request.user == review.name:
            return True
        return False

    def get_success_url(self):
        """ On successful review deletion, stay on same page"""
        product = self.object.product
        messages.success(self.request, "Your Review Was Successfully Deleted")
        return reverse_lazy("product_detail.html")
