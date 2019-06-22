from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Reputation
from .forms import NewStudentForm
from django.db.models import Avg
<<<<<<< HEAD
from django.db import connection

import json
=======
>>>>>>> 85803bf8b7abea62407aa2f7d124c1bfba01dc71

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



def students(request) :
	students_query = Student.objects.all()
	jurusan = str(request.GET.get("jurusan"))
	angkatan = request.GET.get("angkatan")
	sort_rating = request.GET.get("sort_rating")
	if(jurusan is not None):
		students_query = students_query.filter(jurusan = jurusan)
	if(angkatan is not None):
		students_query = students_query.filter(angkatan = int(str(angkatan)))
	return render(request,"skippedia/students.html",{"students":students_query})

def student_by_nim(request,nim) :
	student = Student.objects.get(nim=nim)
	reputations = Reputation.objects.all().filter(receiver=student)
	average_rating = Reputation.objects.all().filter(receiver=student).aggregate(Avg('rating'))
	data = {"student":student,"reputations":reputations,"average_rating":average_rating["rating__avg"]}
	print(data)
	return render(request,"skippedia/student.html",data)

