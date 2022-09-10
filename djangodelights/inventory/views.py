from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from .forms import IngredientForm, MenuItemForm, PurchaseForm
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
    form_class = IngredientForm
    success_url = '/inventory/ingredient/list'


class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create_form.html'
    form_class = IngredientForm


class MenuItemList(ListView):
    model = MenuItem
    template_name = 'inventory/menu_item_list.html'


class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_item_delete_form.html'

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_item_update_form.html'
    form_class = MenuItemForm
    success_url = '/inventory/menu_item/list'

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menu_item_create_form.html'
    form_class = MenuItemForm




class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirment_list.html'


class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_delete.html'


class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_update.html'


class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_create.html'


class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchase_view.html'


class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_delete.html'
    success_url = '/inventory/purchase/list'

class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_update.html'
    fields = ['menu_item', 'time_stamp']


class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_create.html'
    form_class = PurchaseForm

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("purchase_list")


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
                total_cost += recipe_requirement.ingredient.unit_price * \
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context


