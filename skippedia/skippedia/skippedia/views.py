from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .forms import NewStudentForm
import json

def index(request) :
    return render(request,"skippedia/index.html")


def home(request) :
    if request.user.is_authenticated :
        return render(request,"skippedia/home.html")
    else :
        return redirect('/')

@csrf_exempt
def student(request) :
	if(request.method == "POST"):
		new_student = Student()
		new_student.email = request.POST.get("email")
		new_student.nama = request.POST.get("nama")
		new_student.nim = request.POST.get("nim")
		new_student.jurusan = request.POST.get("jurusan")
		new_student.angkatan = request.POST.get("angkatan")
		new_student.save()
		return HttpResponse("Success")