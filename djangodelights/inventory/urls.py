from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('inventory/list', views.IngredientList.as_view(), name='ingredientlist'),

]