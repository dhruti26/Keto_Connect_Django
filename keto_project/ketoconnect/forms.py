from django.core import validators
from django import forms
from .models import Keto_Age
from .models import User_detail
class User(forms.ModelForm):
    class Meta:
        model = User_detail
        fields = ['user_id','user_name','password','email','dateofbirth','gender','phone_number']

class Keto_Age_Form(forms.ModelForm):
    class Meta:
        model = Keto_Age
        fields = ['user_id','current_age','height','weight','experience_ketodiet','number_of_meals','number_of_snacks','intermittent_fasting','number_of_steps','exercise_days','isSmoker',
                  'number_of_sleep_hours','waist_to_height_ratio','systolic_bp','diastolic_bp','oxygen_level','hemoglobin']
        
