from django.urls import path
from . import views

app_name = 'cook_book_app'

urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('recipes_add/', views.add_recipe, name='add_recipe'),
    path('vw/', views.view_recipes, name='view_recipes'),
]


