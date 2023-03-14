from django.db import models

#User_Details
class User_detail(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    dateofbirth = models.DateField(max_length=25)
    gender = models.BooleanField()
    phone_number = models.CharField(max_length=10)

#Order_Details
class Order_Detail(models.Model):
    user_id = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    order_id = models.IntegerField(primary_key=True)
    placement_date = models.DateField(max_length=25)
    delivery_date = models.DateField(max_length=25)
    item_name = models.CharField(max_length=25)
    total_items = models.IntegerField()

#Meal_Planner
class Meal_Planner(models.Model):
    user_id = models.ForeignKey(User_detail,on_delete=models.CASCADE,primary_key=True)
    target_calories = models.IntegerField()
    food_choice_preferences = models.CharField(max_length=15)
    intermittent_fasting = models.BooleanField()
    recipe_preferences = models.CharField(max_length=15)
    food_allergies = models.CharField(max_length=20)

#Keto_Age
class Keto_Age(models.Model):
    user_id = models.ForeignKey(User_detail,on_delete=models.CASCADE,primary_key=True)
    current_age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    experience_ketodiet = models.IntegerField()
    number_of_meals = models.IntegerField()
    number_of_snacks = models.IntegerField() 
    intermittent_fasting = models.BooleanField()
    number_of_steps = models.IntegerField()
    exercise_days = models.IntegerField()
    isSmoker = models.BooleanField()
    number_of_sleep_hours = models.FloatField()
    waist_to_height_ratio = models.FloatField()
    systolic_bp = models.IntegerField()
    diastolic_bp = models.IntegerField() 
    oxygen_level = models.IntegerField() 
    hemoglobin = models.FloatField()

#Food_Details
class Food_Detail(models.Model):
    Food_category = models.CharField(max_length=15)
    Food_Brand = models.CharField(max_length=15)
    Food_Item = models.CharField(max_length=15)

#Address_Details
class Address(models.Model):
    order_id = models.ForeignKey(Order_Detail,on_delete=models.CASCADE)
    house_number = models.IntegerField() 
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)


class KetoCalculator(models.Model):
    body_Fat=models.FloatField()
    total_net_carbs_per_day=models.IntegerField()
    protein_consumed_each_day=models.IntegerField()
    choose_a_goal=models.CharField(max_length=50)

class Login(models.Model):
    user_id = models.ForeignKey(User_detail,on_delete=models.CASCADE,primary_key=True,related_name = 'useroflogin')
    password = models.ForeignKey(User_detail,on_delete = models.CASCADE,related_name='passwordoflogin')

