from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='ingredient_delete'),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name='ingredient_update'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='ingredient_create'),
    path('menu_item/list', views.MenuItemList.as_view(), name='menu_item_list'),
    path('menu_item/delete/<pk>', views.MenuItemDelete.as_view(), name='menu_item_delete'),
    path('menu_item/update/<pk>', views.MenuItemUpdate.as_view(), name='menu_item_update'),
    path('menu_item/create', views.MenuItemCreate.as_view(), name='menu_item_create'),
    path('recipe_requirement/list', views.RecipeRequirementList.as_view(), name='recipe_requirement_list'),
    path('recipe_requirement/delete/<pk>', views.RecipeRequirementDelete.as_view(), name='recipe_requirement_delete'),
    path('recipe_requirement/update/<pk>', views.RecipeRequirementUpdate.as_view(), name='recipe_requirement_update'),
    path('recipe_requirement/create', views.RecipeRequirementCreate.as_view(), name='recipe_requirement_create'),
    path('purchase/list', views.PurchaseList.as_view(), name='purchase_list'),
    path('purchase/delete/<pk>', views.PurchaseDelete.as_view(), name='purchase_delete'),
    path('purchase/update/<pk>', views.PurchaseUpdate.as_view(), name='purchase_update'),
    path('purchase/create', views.PurchaseCreate.as_view(), name='purchase_create'),
    path('reports', views.ReportView.as_view(), name='reports'),

]