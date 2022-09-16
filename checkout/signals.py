''' Documenting imports at the beginning of file '''
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CartItem


@receiver(post_save, sender=CartItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on CartItem update/creation
    """
    instance.order.update_total()


@receiver(post_delete, sender=CartItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on CartItem deletion
    """
    instance.order.update_total()
