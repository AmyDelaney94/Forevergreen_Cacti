''' Adding Imports to begining of file '''
from .forms import SubscriberForm


def render_subscribe_form(request):
    """ Render subscribe form across all pages """

    subscribe_form = SubscriberForm()

    context = {
        'subscribe_form': subscribe_form,
    }

    return context
