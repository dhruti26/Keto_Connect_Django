from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Keto_Age_Form
from ketoconnect.models import Keto_Age
from .forms import UserDetails
from ketoconnect.models import User_detail
from ketoconnect.models import *
from .forms import *
import matplotlib
import os
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import numpy as np
def User(request):
   if request.method == 'POST':
      userid = request.POST['uid']
      username = request.POST['uname']
      pas = request.POST['pswd']
      ema = request.POST['em']
      date = request.POST['dob']
      gen = request.POST['gen']
      phone = request.POST['phnum']
      user=User_detail(user_id = userid,user_name=username,password=pas,email=ema,dateofbirth=date,gender=gen,phone_number=phone)
      user.save()
      return render(request,'index.html',{})
   else:
      user = User_detail()
      return render(request,'index1.html') 


def KetoAge(request):
   if request.method == 'POST':
      uidd = request.POST['uid']
      ui = User_detail.objects.get(user_id=uidd)
      ag = request.POST['age']
      heigh = request.POST['height']
      weigh = request.POST['weight']
      exp_diet = request.POST['kdiet']
      meals = request.POST['meals']
      snacks = request.POST['snacks']
      itfast = request.POST['itfast']
      step = request.POST['steps']
      exe = request.POST['exdays']
      smo = request.POST['smoke']
      sle = request.POST['sleep']
      hw = request.POST['heightwaist']
      sbpre = request.POST['sbp']
      dbpre = request.POST['dbp']
      oxle = request.POST['oxy']
      hb = request.POST['hemoglobin']
      kage = Keto_Age(user_id = ui,current_age=ag,height = heigh,weight=weigh,experience_ketodiet=exp_diet,number_of_meals=meals,number_of_snacks=snacks,intermittent_fasting=itfast,number_of_steps=step,exercise_days=exe,isSmoker=smo,number_of_sleep_hours=sle,waist_to_height_ratio=hw,systolic_bp=sbpre,diastolic_bp=dbpre,oxygen_level=oxle,hemoglobin=hb)
      kage.save()
      keage = (eval(ag) + (eval(weigh)/eval(heigh)) + eval(exp_diet) + ((eval(meals))/2) + ((eval(snacks))/2) + (eval(itfast)) + ((eval(step))/100) + ((eval(exe))/7) + eval(smo) + eval(sle) + ((eval(hw))/100) + ((eval(sbpre))/90) + ((eval(dbpre))/120) + ((eval(oxle))/80) + ((eval(hb))/15))
      data = { 'begin' : str(0),'chronological age' : ag , 'keto age' : str(keage)}
      ages = list(data.keys())
      ageval = list(data.values())
      fig = plt.figure(figsize = (15,8))
      plt.bar(ages,ageval,color='black',width = 0.1)
      plt.ylim(ymin=0)
      plt.xlabel('Ages')
      plt.ylabel('Values')
      plt.title('KetoAge vs ChronologicalAge')
      plt.savefig('static/Otherfiles/ketoage.png',dpi=100)
      return render(request,'displayketoAge.html',{})
   else:
      kage = Keto_Age()
      return render(request,'ketoAge.html')


def KCalc(request):
   if(request.method=='POST'):
      bf = request.POST['bfat']
      tc = request.POST['ncarbs']
      pcons = request.POST['pc']
      cgo = request.POST['cgoal']
      meal = KetoCalculator(body_Fat=bf,total_net_carbs_per_day=tc,protein_consumed_each_day=pcons,choose_a_goal=cgo)
      meal.save()
      glu = 100-(eval(bf)+eval(tc)+eval(pcons))
      labels = 'BodyFat','Net Carbs','Proteins consumed','Glucose Content'
      sizes = [bf,tc,pcons,glu]
      fig1,ax1 = plt.subplots();
      ax1.pie(sizes,explode = None,labels = labels, shadow=True, startangle=90)
      ax1.axis('equal') 
      plt.savefig('static/Otherfiles/ketocalculator.png',dpi=100)
      return render(request,'displayketocalc.html',{})
   else:
      kc = KetoCalculator()
      return render(request,'ketocalculator.html')

def Mealplanner(request):
   if(request.method == 'POST'):
      uidd = request.POST['uid']
      ui = User_detail.objects.get(user_id=uidd)
      tcal = request.POST['tc']
      fcp = request.POST['foodcp']
      infast = request.POST['ifast']
      rp = request.POST['rpref']
      fall = request.POST['fa']
      mealp = Meal_Planner(user_id = ui,target_calories=tcal,food_choice_preferences=fcp,intermittent_fasting=infast,recipe_preferences = rp,food_allergies=fall)
      mealp.save()
      return render(request,'mealplan.html',{})
   else:
      mealp = Meal_Planner()
      return render(request,'mealplanner.html')


def FoodFinder(request):
   if(request.method=='POST'):
      fc = request.POST['fcat']
      fbrand = request.POST['fb']
      food = Food_Detail(Food_category=fc,Food_Brand=fbrand)
      food.save()
      return render(request,'fooddetails.html',{})
   else:
      food = Food_Detail()
      return render(request,'fooddetails.html')


def HomePage(request):
   return render(request,'index.html')


def articlelifestyle(request):
   return render(request,'articles\lifestyle-article\lifestyle.html')

def articlenutrition(request):
   return render(request,'articles/nutrition-article/articles.html')

def articletherauptic(request):
   return render(request,'articles/Therapeutics-article/thrapy.html')

def breakfast(request):
   return render(request,'recipe/breakfast/breakfast.html')

def lunch(request):
   return render(request,'recipe/lunch/lunch.html')

def snacks(request):
   return render(request,'recipe/snacks/snacks.html')

def dinner(request):
   return render(request,'recipe/dinner/dinner.html')


def accessories(request):
   return render(request,'Shop/accesories/accesories.html')


def ebooks(request):
   return render(request,'Shop/ebooks/ebooks.html')


# def about(request):
#     return render(request,'about.html')

# def index(request):
#    return render(request,'index.html')