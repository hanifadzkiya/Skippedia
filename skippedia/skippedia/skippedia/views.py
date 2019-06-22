from django.shortcuts import render
from django.template import loader

# Create your views here.


def index(request) :
    return render(request,"skippedia/index.html")


def home(request) :
    return render(request,"skippedia/home.html")