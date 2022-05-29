from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .forms import SignUp_Form
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse

# Create your views here.

def signup(request):
    form = SignUp_Form()
    if request.method=='POST':
        form = SignUp_Form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            auth_login(request,user)
            return redirect(reverse('Restaurant:Restaurant_list'))
    else:
        form = SignUp_Form()

    context={'form':form}
    return render(request,'accounts/signup.html',context)