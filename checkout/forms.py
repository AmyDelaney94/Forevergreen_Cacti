''' Documenting imports at the beginning of file '''
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    ''''Creating Form for checkout with required fields'''
    class Meta:
        ''''Fields being populated from Order Model'''
        model = Order
        fields = ('username', 'email', 'mobile', 'address_line1',
                  'address_line2', 'town_or_city', 'county', 'country',
                  'eircode')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field so cursor begins there
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Full Name',
            'email': 'Email Address',
            'mobile': 'Contact Number',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'eircode': 'Eircode',
            }

        self.fields['username'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Form customisation, adds * to required fields.
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
