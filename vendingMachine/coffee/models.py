# machine/models.py

from django.db import models

class Ingredient(models.Model):
    # The name of the ingredient
    name = models.CharField(max_length=50)
    # The current quantity of the ingredient in stock
    quantity = models.IntegerField()
    # The maximum capacity of the ingredient that can be stored
    max_capacity = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class Beverage(models.Model):
    # The name of the beverage
    name = models.CharField(max_length=50)
    # Many-to-Many relationship to Ingredient through BeverageIngredient
    ingredients = models.ManyToManyField(Ingredient, through='BeverageIngredient')

    def __str__(self):
        return self.name

class BeverageIngredient(models.Model):
    # The beverage associated with this ingredient
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    # The ingredient associated with this beverage
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # The quantity of the ingredient used in this beverage
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.beverage.name} - {self.ingredient.name} ({self.quantity})"
