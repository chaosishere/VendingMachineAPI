# machine/serializers.py

from rest_framework import serializers
from .models import Ingredient, Beverage, BeverageIngredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class BeverageIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = BeverageIngredient
        fields = ['ingredient', 'quantity']

class BeverageSerializer(serializers.ModelSerializer):
    ingredients = BeverageIngredientSerializer(source='beverageingredient_set', many=True)

    class Meta:
        model = Beverage
        fields = ['id', 'name', 'ingredients']
