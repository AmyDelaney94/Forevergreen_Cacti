''' Adding Imports to begining of file '''
from django.db import models

# Create your models here.


class Subscriber(models.Model):
    """ Model for Newsletter subscription """

    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
