from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    ssn = models.CharField(max_length=10)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse("user:user-detail", kwargs={"pk" : self.pk})
    