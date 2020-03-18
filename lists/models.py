from django.db import models
from django.urls import reverse

# Create your models here.


class List(models.Model):

    def get_absolute_url(self):
        return reverse("lists:view_list", kwargs={"pk": self.pk})


class Item(models.Model):
    text = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
