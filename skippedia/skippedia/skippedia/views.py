from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .forms import NewStudentForm
from django.db.models import Avg
from django.db import connection

import json

def index(request) :
    return render(request,"skippedia/index.html")




def home(request) :
	if request.user.is_authenticated :
		cursor=connection.cursor()
		cursor.execute("SELECT st.id, st.nama , st.nim , IFNULL(AVG(sp.rating),0) as 'avg_rating' FROM skippedia_student AS st LEFT JOIN skippedia_reputation AS sp ON st.id = sp.receiver_id WHERE angkatan=2016 GROUP BY st.id ORDER BY avg_rating ASC LIMIT 10")
		top_performers_IF = cursor.fetchall()
		print(top_performers_IF)
		return render(request,"skippedia/home.html",
			{'top_performers_if' : top_performers_IF}
		)
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