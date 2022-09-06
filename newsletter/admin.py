''' Adding imports to beginning of file '''

from django.contrib import admin
from .models import Subscriber

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    ''' Orders email addresses by date subscribed '''
    list_display = ('email', 'date_added')

    ordering = ('-date_added',)


admin.site.register(Subscriber, SubscriberAdmin)
