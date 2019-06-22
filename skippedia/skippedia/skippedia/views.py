from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Reputation
from .forms import NewStudentForm
from django.db.models import Avg, Count
from django.db import connection

import json

def index(request) :
    return render(request,"skippedia/index.html")

def home(request) :
	if request.user.is_authenticated :
		return render(request,"skippedia/home.html",
			{'top_performers_if' : top_performers_IF}
		)
	else :
		return redirect('/')

def students(request) :
	students_query = Student.objects.all()
	jurusan = request.GET.get("jurusan")
	angkatan = request.GET.get("angkatan")
	ascending = request.GET.get("ascending")
	condition = "1 = 1"
	order = ""
	if(jurusan is not None):
		condition = condition + " AND jurusan = '" + jurusan + "'"
	if(angkatan is not None):
		condition = condition + " AND angkatan = " + str(angkatan) 
	if(ascending is not None):
		order = " ASC "
	cursor=connection.cursor()
	cursor.execute("SELECT st.id, st.nama , st.nim , IFNULL(AVG(sp.rating),0) as 'avg_rating' FROM skippedia_student AS st LEFT JOIN skippedia_reputation AS sp ON st.id = sp.receiver_id WHERE " + condition + " GROUP BY st.id ORDER BY avg_rating " + order + " LIMIT 10")
	top_performers_IF = cursor.fetchall()
	return HttpResponse(json.dumps(top_performers_IF))


def student_by_nim(request,nim) :
	student = Student.objects.get(nim=nim)
	reputations = Reputation.objects.all().filter(receiver=student)
	average_rating = Reputation.objects.all().filter(receiver=student).aggregate(Avg('rating'))
	data = {"student":student,"reputations":reputations,"average_rating":average_rating["rating__avg"]}
	return render(request,"skippedia/student.html",data)

