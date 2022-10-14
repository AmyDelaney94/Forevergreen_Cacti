''' Adding imports to beginning of file '''
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm

# Create your views here.


def add_subscriber(request):
    """Add email to the subscriber list"""

    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(
                request,
                f"{instance.email} already exists in our database. \
                    Please check your email and try again."
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            instance.save()
            messages.success(
                request,
                f"{instance.email} has been added to our the newsletter"
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def remove_subscriber(request):
#     """Remove email from the subscriber list"""

#     form = SubscriberForm(request.POST or None)

#     if form.is_valid():
#         instance = form.save(commit=False)

#         if Subscriber.objects.filter(email=instance.email).exists():
#             Subscriber.objects.filter(email=instance.email).delete()

#         else:
#             instance.save()
#             messages.success(
#                 request,
#                 f"{instance.email} already exists in our database. \
#                     Please check your email and try again."
#             )
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
