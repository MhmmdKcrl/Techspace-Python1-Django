from django.db import models
from django.db.models import CharField, EmailField, TextField

# Create your models here.


class Contact(models.Model):
    name = CharField(max_length=50)
    email = EmailField()
    subject = CharField(max_length=100)
    message = TextField()

    def __str__(self):
        return self.name
    

class Subscriber(models.Model):
    email = EmailField()

    def __str__(self):
        return self.email
    