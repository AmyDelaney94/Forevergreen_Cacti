''' Documenting imports at the beginning of file '''
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    ''''Creating Form for checkout with required fields'''
    class Meta:
        ''''Fields being populated from Order Model'''
        model = UserProfile
        exclude = ('user',)
