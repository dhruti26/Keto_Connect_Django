from django.contrib import admin
from django.urls import path
from ketoconnect import views
from django.conf import settings

urlpatterns = [
    path('keto-age/',views.KetoAge),
    path('User/',views.UserDetails),
    path('keto-calculator/',views.Keto_Calculator),
    path('food-finder/',views.FoodDetail),
    path('meal-planner/',views.MealPlanner)
]