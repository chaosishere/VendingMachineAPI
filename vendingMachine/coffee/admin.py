# machine/admin.py

from django.contrib import admin
from .models import Ingredient, Beverage, BeverageIngredient

class BeverageIngredientInline(admin.TabularInline):
    # Inline model for displaying BeverageIngredient within BeverageAdmin
    model = BeverageIngredient
    extra = 1

class BeverageAdmin(admin.ModelAdmin):
    # Admin configuration for the Beverage model
    inlines = [BeverageIngredientInline]

# Register models with the Django admin site
admin.site.register(Ingredient)
admin.site.register(Beverage, BeverageAdmin)
