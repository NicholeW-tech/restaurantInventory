from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"