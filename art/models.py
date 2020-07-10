from django.db import models
from users.models import User


# Create your models here.
class Piece(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    medium = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    production = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    stamp = models.CharField(max_length=50)


class Transaction(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller', on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    price = models.FloatField()