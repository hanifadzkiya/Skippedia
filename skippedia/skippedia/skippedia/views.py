from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.


def index(request) :
    return render(request,"skippedia/index.html")


def home(request) :
    if request.user.is_authenticated :
        return render(request,"skippedia/home.html")
    else :
        return redirect('/')