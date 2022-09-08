from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.charField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.charField(max_length=200)
    unit_price = models.FloatField(default=0)
