''' Documenting imports at the beginning of file '''
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    ''' Class for name of checkout app '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        #import not added to top level itss designed to override the default.
        import checkout.signals
