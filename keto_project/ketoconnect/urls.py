from django.contrib import admin
from django.urls import path
from ketoconnect import views
from django.conf import settings

urlpatterns = [
    path('/User/',views.User,name = 'User'),
    path('/keto-age/',views.KetoAge,name = 'KetoAge'),
    path('/keto-calculator/',views.KCalc,name = 'KCalc'),
    path('/meal-planner/',views.Mealplanner,name = 'Mealplanner'),
    path('/food-finder/',views.FoodFinder,name = 'FoodFinder'),
    path('homepage/',views.HomePage),
    path('lifestyle/',views.articlelifestyle,name = 'articlelifestyle'),
    path('therauptic/',views.articletherauptic,name = 'articletherauptic'),
    path('nutrition/',views.articlenutrition,name = 'articlenutrition'),
    path('breakfast/',views.breakfast,name='breakfast'),
    path('lunch/',views.lunch,name='lunch'),
    path('snacks/',views.snacks,name='snacks'),
    path('dinner/',views.dinner,name='dinner'),
    path('accessories/',views.accessories,name='accessories'),
    path('ebooks/',views.ebooks,name='ebooks')
]