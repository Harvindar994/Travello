from django.db import models


# Create your models here.
class Destination(models.Model):
    image = models.ImageField(upload_to='pics')
    destination = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    last_sended_post = models.IntegerField()


