from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Keto_Age_Form
from ketoconnect.models import Keto_Age
from ketoconnect.models import User_detail
from .forms import User
def UserDetails(request):
   if request.method == 'POST':
      ud = User(request.POST)
      if ud.is_valid():
         uid = ud.cleaned_data['user_id']
         uname = ud.cleaned_data['user_name']
         upswd = ud.cleaned_data['password']
         uema = ud.cleaned_data['email']
         udob = ud.cleaned_data['dateofbirth']
         ugen = ud.cleaned_data['gender']
         uphon = ud.cleaned_data['phone_number']
         userde  = User(user_id = uid,user_name = uname,password = upswd,email=uema,date_of_birth = udob,gender=ugen,phone_number = uphon)
         userde.save()
         return HttpResponse('<h1>The user is created</h1>')
      else :
       u = User()
       return render(request,"userdetails.html",{'form':u})
      
      
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
       keto_age = currentage+(ht/wt)+expkdiet+(exedays/365.0)+(nummeals/2.0)+(numsnacks/2.0)+(sleephours/24.0)+(hemoglobin/15.0)+((systolic/120.0)+1)+(diastolic/80.0)+1+0.01*oxygen
       reg = Keto_Age(user_id=user_id,current_age=currentage,height=ht,weight=wt,experience_ketodiet=expkdiet,number_of_meals=nummeals,number_of_snacks=numsnacks,intermittent_fasting = interfasting,number_of_steps = numsteps,exercise_days = exedays,
                      isSmoker = isSmoker,number_of_sleep_hours=sleephours,waist_to_height_ratio = waistheight,systolic_bp = systolic,diastolic_bp = diastolic,oxygen_level = oxygen,hemoglobin=hemoglobin,keto_age_value = keto_age)
       reg.save()
       return render(request,"displayketoAge.html",{'Keto_Age_value' : keto_age})
    else :
       ka=Keto_Age_Form()
       return render(request,"ketoAge.html",{'form':ka})
    
