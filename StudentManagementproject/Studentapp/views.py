from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from Studentapp.models import City, Course, Student


# Create your views here.


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_fun(request):
    return render(request,'login.html',{'data':''})


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request,'register.html',{'data': ''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def regdata_fun(request):
    User_name = request.POST['txtName']
    User_email = request.POST['txtEmail']
    User_pswd = request.POST['txtpswd']
    if User.objects.filter(Q(username=User_name) | Q(email=User_email)).exists():
        return render(request, 'register.html',{'data': 'username,email,and password is already exists'})
    else:
        u1 = User.objects.create_superuser(username=User_name,email=User_email,password=User_pswd)
        u1.save()
        return redirect('log')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_data(request):
    User_Name=request.POST['txtname']
    User_Password=request.POST['txtpswd']
    user1 = authenticate(username=User_Name,password=User_Password)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data': 'user is not superuser'})
    else:
        return render(request, 'login.html', {'data': 'enter proper username and password'})


@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def addstudent_fun(request):
    city=City.objects.all()
    course=Course.objects.all()
    return render(request,'addstudents.html',{'City_data': city,'Course_data': course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def read_data_fun(request):
    s1 = Student()
    s1.S_Name = request.POST["txtname"]
    s1.S_Age = request.POST["txtage"]
    s1.S_Phno = request.POST["txtphno"]
    s1.S_City = City.objects.get(City_Name=request.POST['ddlcity'])
    s1.S_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display_fun(request):
    s1 = Student.objects.all()
    return render(request,'display.html',{'data': s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method=='POST':
        s1.S_Name = request.POST["txtname"]
        s1.S_Age = request.POST["txtage"]
        s1.S_Phno = request.POST["txtphno"]
        s1.S_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s1.S_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data': s1,'City_data': city,'Course_data': course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logout_fun(request):
    logout(request)
    return redirect('log')