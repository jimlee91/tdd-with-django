from django.db import models

# Create your models here.


class List(models.Model):
    pass


class Item(models.Model):
    text = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
