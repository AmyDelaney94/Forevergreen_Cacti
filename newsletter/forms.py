''' Adding Imports to begining of file '''
from crispy_forms.helper import FormHelper
from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """ Form required for subscribing with email address """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

    class Meta:
        """ Class calling a model and required field """
        model = Subscriber
        fields = ('email',)
