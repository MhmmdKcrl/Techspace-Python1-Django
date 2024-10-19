from django.contrib import admin

# Register your models here.


from core.models import Contact, Subscriber

admin.site.register(Contact)
admin.site.register(Subscriber)