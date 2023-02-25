from django.contrib import admin
from ketoconnect.models import User_details

# class Keto_Age_Admin(admin.ModelAdmin):
#     list_display=['user_id','current_age','height','weight','experience_ketodiet','number_of_meals','number_of_snacks','ntermittent_fasting','number_of_steps','exercise_days','isSmoker','number_of_sleep_hours','waist_to_height_ratio','systolic_bp','diastolic_bp','oxygen_level','hemoglobin']

# admin.site.register(Keto_Age,Keto_Age_Admin)
# # Register your models here.

@admin.register(User_details)
class StudentAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','password','email','dateofbirth','gender','phone_number')
   
