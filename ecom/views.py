from django.shortcuts import render,redirect
from .models import Product,Category,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import userProfile
from django import forms

def home(request):
    product = Product.objects.all()
    if request.user.is_authenticated:
        return render(request,'index.html',{'product':product})
    else:
        messages.success(request,"Please Login To Continue...")
        return redirect('login')

def about(request):
    return render(request,'about.html',{})

def user_profile(request):
    if request.user.is_authenticated:
        current_user =  User.objects.get(id=request.user.id)
        current_user1 = Profile.objects.get(user__id=request.user.id)
        form = userProfile(request.POST or None,instance= current_user1)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Address is updated')
            return redirect('home')
        return render(request,'profile.html',{'current_user':current_user,'form':form})
    else:
        messages.success(request,'Please Login TO proceed')
        return redirect('home')

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        current_user = User.objects.get(id=request.user.id)
        if current_user.check_password(current_password):
            if password1 == password2:
                current_user.set_password(password1)
                current_user.save()
                return redirect('login')
            else:
                messages.success(request,'passwords are not same...')
                return redirect('user_profile')
        else:
            messages.success(request,'Current Password is not correct..')
            return redirect('user_profile')
    return render(request,'profile.html')
        

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome To Ecommerce Website..')
            return redirect('home')
        else:
            messages.success(request,'Please enter the correct Credentials')
            return redirect('login')
    else:
        return render(request,'login.html',{})


def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1)
            user.save()
            return redirect('login')
        else:
            messages.success(request,'passwords are not same')
            return redirect('register')
    else:
        return render(request,'register.html',{})
    
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def category(request,c):
    c = c.replace('-',' ')
    category = Category.objects.get(name=c)
    product = Product.objects.filter(category=category)
    return render(request,'category.html',{'product':product})