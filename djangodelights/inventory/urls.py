from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='ingredient_delete'),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name='ingredient_update'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='ingredient_create'),
    path('menu_item/list', views.MenuItemList.as_view(), name='menu_item_list'),
    path('menu_item/delete/<pk>', views.MenuItemDelete.as_view(), name='menu_item_delete'),
    path('menu_item/update/<pk>', views.MenuItemUpdate.as_view(), name='menu_item_update'),

]