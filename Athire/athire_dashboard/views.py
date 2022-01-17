from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import signin_credentials
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = signin_credentials.objects.filter(username=username).first()

        if user and user.password == password:
            return redirect('home')
        else:
            return render(request, "login.html")


    context={}
    return render(request, "login.html", context)

def home(request):
    return render(request, "home.html")