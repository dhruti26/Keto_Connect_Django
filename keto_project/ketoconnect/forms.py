from django.core import validators
from django import forms
from .models import Keto_Age
from .models import User_detail
from .models import *
class UserDetails(forms.ModelForm):
    class Meta:
        model = User_detail
        fields = ['user_id','user_name','password','email','dateofbirth','gender','phone_number']

class Keto_Age_Form(forms.ModelForm):
    class Meta:
        model = Keto_Age
        fields = ['user_id','current_age','height','weight','experience_ketodiet','number_of_meals','number_of_snacks','intermittent_fasting','number_of_steps','exercise_days','isSmoker','number_of_sleep_hours','waist_to_height_ratio','systolic_bp','diastolic_bp','oxygen_level','hemoglobin'] 

class Keto_Calculator_Form(forms.ModelForm):
    class Meta:
        model = KetoCalculator
        fields = ['body_Fat','total_net_carbs_per_day','protein_consumed_each_day','choose_a_goal']

class Food_Detail_Form(forms.ModelForm):
    class Meta :
        model = Food_Detail
        fields = ['Food_category','Food_Brand','Food_Item']

class Meal_Planner_Form(forms.ModelForm):
    class Meta:
        model = Meal_Planner
        fields = ['target_calories','food_choice_preferences','intermittent_fasting','recipe_preferences','food_allergies']