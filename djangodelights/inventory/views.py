from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Sum


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


class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchase_view'


class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_delete'


class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_update'
    fields = ['menu_item', 'time_stamp']


class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_create'
    fields = ['menu_item', 'time_stamp']


class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context


class ReportView(TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * \
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context