from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    catagory = models.CharField(max_length = 200)
    discription = models.CharField(max_length = 1000)
    price = models.IntegerField()
    src = models.CharField(max_length = 500)