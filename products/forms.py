''' Documenting imports at beginning of file '''
from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """Create a form creation of products"""
    class Meta:
        """
        Selecting model and fields to display on the form
        """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """Create a form for users to leave reviews on tour page"""
    class Meta:
        """
        Selecting model and fields to display on the form
        """
        model = Review
        fields = ('your_review',)
