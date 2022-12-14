from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    unit_price = models.FloatField(default=0.00)

    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit} ${self.unit_price};'

    def get_absolute_url(self):
        return './list'


class MenuItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)


    def __str__(self):
        return f'{self.title} ${self.price}'

    def get_absolute_url(self):
        return './list'

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return f'menu item={self.menu_item.__str__()}; ingredient={self.ingredient}; quantity={self.quantity};'

    def enough(self):
        return self.quantity <= self.ingredient.quantity




class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return './list'

    def __str__(self):
        return f'menu item={self.menu_item.__str__()}; timestamp={self.time_stamp};'


