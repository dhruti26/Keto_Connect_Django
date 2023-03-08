from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Keto_Age_Form
from ketoconnect.models import Keto_Age
from .forms import UserDetails
from ketoconnect.models import User_detail
from ketoconnect.models import *
from .forms import *
def User(request):
   if request.method == 'POST':
      fm = UserDetails(request.POST)
      if fm.is_valid():
         uid = fm.cleaned_data['user_id']
         una = fm.cleaned_data['user_name']
         pw = fm.cleaned_data['password']
         em = fm.cleaned_data['email']
         dob = fm.cleaned_data['dateofbirth']
         gen = fm.cleaned_data['gender']
         pnum = fm.cleaned_data['phone_number']
         reg = User_detail(user_id = uid,user_name = una,password=pw,email=em,dateofbirth=dob,gender=gen,phone_number=pnum)
         reg.save()
         return render(request,"UserRegistration.html",{'user_form' : fm})
   else:
      fm = UserDetails()
      return render(request,"UserRegistration.html",{'user_form' : fm})

def KetoAge(request):
   if request.method == 'POST':
      ka=Keto_Age_Form(request.POST)
      if ka.is_valid():
         user_id = ka.cleaned_data['user_id']
         currentage=ka.cleaned_data['current_age']
         ht=ka.cleaned_data['height']
         wt=ka.cleaned_data['weight']
         expkdiet=ka.cleaned_data['experience_ketodiet']
         nummeals=ka.cleaned_data['number_of_meals']
         numsnacks=ka.cleaned_data['number_of_snacks']
         interfasting=ka.cleaned_data['intermittent_fasting']
         numsteps=ka.cleaned_data['number_of_steps']
         exedays=ka.cleaned_data['exercise_days']
         isSmoker=ka.cleaned_data['isSmoker']
         sleephours=ka.cleaned_data['number_of_sleep_hours']
         waistheight=ka.cleaned_data['waist_to_height_ratio']
         systolic=ka.cleaned_data['systolic_bp']
         diastolic=ka.cleaned_data['diastolic_bp']
         oxygen=ka.cleaned_data['oxygen_level']
         hemoglobin=ka.cleaned_data['hemoglobin']
         reg = Keto_Age(user_id=user_id,current_age=currentage,height=ht,weight=wt,experience_ketodiet=expkdiet,number_of_meals=nummeals,number_of_snacks=numsnacks,intermittent_fasting = interfasting,number_of_steps = numsteps,exercise_days = exedays,
                      isSmoker = isSmoker,number_of_sleep_hours=sleephours,waist_to_height_ratio = waistheight,systolic_bp = systolic,diastolic_bp = diastolic,oxygen_level = oxygen,hemoglobin=hemoglobin)
         reg.save()
         keto_age = currentage+(ht/wt)+expkdiet+(exedays/365.0)+(nummeals/2.0)+(numsnacks/2.0)+(sleephours/24.0)+(hemoglobin/15.0)+((systolic/120.0)+1)+(diastolic/80.0)+1+0.01*oxygen
         #  print("abc")
         return render(request,"displayketoAge.html",{'form' : ka, 'keto_age_value' : keto_age})
   else :
      ka=Keto_Age_Form()
      return render(request,"ketoAge.html",{'form':ka})


def Keto_Calculator(request):
   if request.method == 'POST':
      fm = Keto_Calculator_Form(request.POST)
      if fm.is_valid():
         bf = fm.cleaned_data['body_Fat']
         netc = fm.cleaned_data['total_net_carbs_per_day']
         pc = fm.cleaned_data['protein_consumed_each_day']
         chgoal = fm.cleaned_data['choose_a_goal']
         reg = KetoCalculator(body_Fat = bf, total_net_carbs_per_day = ntc,protein_consumed_each_day = pc,choose_a_goal = chgoal)
         reg.save()
         return render(request,"ketocalculator.html",{'ketocalc_form' : fm})
   else:
      fm = Keto_Calculator_Form()
      return render(request,"ketocalculator.html",{'ketocalc_form' : fm})


def FoodDetail(request):
   if request.method == 'POST':
      fm = Food_Detail_Form(request.POST)
      if fm.is_valid():
         fc = fm.cleaned_data['Food_category']
         fbr = fm.cleaned_data['Food_Brand']
         fi = fm.cleaned_data['Food_Item']
         reg = Food_Detail(Food_category = fc,Food_Brand = fbr,Food_Item=fi)
         reg.save()
         return render(request,"fooddetails.html",{'fooddetailform' : fm})
   else:
      fm = Food_Detail_Form()
      return render(request,"fooddetails.html",{'fooddetailform' : fm})


def MealPlanner(request):
   if request.method == 'POST':
      fm = Meal_Planner_Form(request.POST)
      if fm.is_valid():
         tc = fm.cleaned_data['target_calories']
         fcp = fm.cleaned_data['food_choice_preferences']
         ifast = fm.cleaned_data['intermittent_fasting']
         rpref = fm.cleaned_data['recipe_preferences']
         fall = fm.cleaned_data['food_allergies']
         reg = Meal_Planner(target_calories = tc,food_choice_preferences=fcp,intermittent_fasting=ifast,recipe_preferences=rpref,food_allergies=fall)
         reg.save()
         return render(request,"mealplanner.html",{'mealplanform' : fm})
   else:
      fm = Meal_Planner_Form()
      return render(request,"mealplanner.html",{'mealplanform' : fm})