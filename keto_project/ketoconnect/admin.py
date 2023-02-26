from django.contrib import admin
from ketoconnect.models import User_detail
from ketoconnect.models import Order_Detail
from ketoconnect.models import Meal_Planner   
from ketoconnect.models import Keto_Age
from ketoconnect.models import Food_Detail
from ketoconnect.models import Address
from ketoconnect.models import KetoCalculator



@admin.register(User_detail)
class StudentAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','password','email','dateofbirth','gender','phone_number')


@admin.register(Order_Detail)
class OrderAdmin(admin.ModelAdmin):
    list_display=('user_id','order_id','placement_date','delivery_date','item_name','total_items')    

@admin.register(Meal_Planner)
class MealAdmin(admin.ModelAdmin):
    list_display=('user_id','target_calories','food_choice_preferences','intermittent_fasting','recipe_preferences','food_allergies') 


@admin.register(Keto_Age)
class Keto_Age_Admin(admin.ModelAdmin):
    list_display=('user_id','current_age','height','weight','experience_ketodiet','number_of_meals','number_of_snacks','intermittent_fasting','number_of_steps','exercise_days','isSmoker','number_of_sleep_hours','waist_to_height_ratio','systolic_bp','diastolic_bp','oxygen_level','hemoglobin')   

@admin.register(Food_Detail)
class FoodAdmin(admin.ModelAdmin):
    list_display=('Food_category','Food_Brand') 

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=('order_id','house_number','street','city','state')  

@admin.register(KetoCalculator)
class KetoCalculatorAdmin(admin.ModelAdmin):
    list_display=('body_Fat','total_net_carbs_per_day','protein_consumed_each_day','choose_a_goal')                     
   
