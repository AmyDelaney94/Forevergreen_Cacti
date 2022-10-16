''' Documenting imports at the beginning of file '''
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    ''''Creating Form for checkout with required fields'''
    class Meta:
        ''''Fields being populated from Order Model'''
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field so cursor begins there
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_mobile': 'Contact Number',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_eircode': 'Eircode',
            }

        self.fields['default_mobile'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Form customisation, adds * to required fields.
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = [
                    'rounded-0 profile-form-input']
                self.fields[field].label = False
