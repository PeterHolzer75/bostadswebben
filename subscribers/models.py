import email
from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(blank=False, null=False, help_text="Epostadress")
    full_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.email
