from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.

class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'


class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'


class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update_form.html'
    fields = ['name', 'quantity"', 'unit', 'unit_price']


class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create_form.html'
    fields = ['name', 'quantity"', 'unit', 'unit_price']


class MenuItemList(ListView):
    model = MenuItem
    template_name = 'inventory/menu_item_list.html'


class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_item_delete_form.html'

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_item_update_form.html'
    fields = ['title', 'price']

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menu_item_create_form.html'
    fields = ['title', 'price']

class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirment_list'


class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_delete'


class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_update'


class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_create'


class PurchaseView(ListView):
    model = Purchase
    template_name = 'inventory/purchase_view'