# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def registration(request):
    if request.method=='GET':
        return render(request,"register.html")
    elif request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        User.objects.create_user(username=uname,email=email,password=password)
        return render(request,"register.html",{"data":"successfully registered please login here..."})

def loginpage(request):
    if request.method=="GET":
        return render(request,"login.html")
    if request.method=="POST":
       username=request.POST.get("username")
       password=request.POST.get("password")
       user=authenticate(request,username=username,password=password)
       if user is not None:
          login(request,user)
          return render(request,'login.html',{"data":'Successfully LogedIn...'})
       else:
          return render(request,"login.html",{"data":'invalid details'})


