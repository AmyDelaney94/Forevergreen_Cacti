''' Documenting imports at beginning of file'''
from django import template

# From django library documentation
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Function to calculate total cost of multiple
    products in shopping cart
    """
    return price * quantity
