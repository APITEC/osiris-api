from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    government_id = models.CharField(max_length=100)
    stamp = models.CharField(max_length=50)