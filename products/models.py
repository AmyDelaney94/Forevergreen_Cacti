''' Adding Imports to beggining of file '''
from django.db import models


class Category(models.Model):
    """
    Model to display product category name.
    """
    name = models.CharField(max_length=200, unique=True)
    friendly_name = models.CharField(
        max_length=200, null=True, blank=True, unique=True
        )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        ''' Function to return frontend name'''
        return self.friendly_name


class Product(models.Model):
    """
    Model to display a product on the store.
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    variety = models.TextField(max_length=300,null=True, blank=True)
    description = models.TextField()
    care = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        To display the products by date added to the store in desending order.
        """
        ordering = ['-date_added']

    def __str__(self):
        return self.name
