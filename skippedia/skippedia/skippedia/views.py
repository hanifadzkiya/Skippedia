from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Reputation
from .forms import NewStudentForm
from django.db.models import Avg, Count
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

def index(request) :
    return render(request,"skippedia/index.html")

def home(request) :
	if request.user.is_authenticated :
		print(request);
		return render(request,"skippedia/home.html")
	else :
		return redirect('/')

@csrf_exempt
def students(request) :
	students_query = Student.objects.all()
	jurusan = request.GET.get("jurusan")
	angkatan = request.GET.get("angkatan")
	sort = str(request.GET.get("sort"))
	nama = request.GET.get("nama");
	condition = "1 = 1"
	if(jurusan is not None):
		condition = condition + " AND jurusan = '" + jurusan + "'"
	if(angkatan is not None):
		condition = condition + " AND angkatan = " + str(angkatan) 
	if(nama is not None):
		condition = condition + " AND nama LIKE '%" + str(nama) + "%'"
	cursor=connection.cursor()
	cursor.execute("SELECT st.id, st.nama , st.nim , IFNULL(AVG(sp.rating),0) as 'avg_rating' FROM skippedia_student AS st LEFT JOIN skippedia_reputation AS sp ON st.id = sp.receiver_id WHERE " + condition + " GROUP BY st.id ORDER BY avg_rating " + sort + " LIMIT 10")
	top_performers_IF = cursor.fetchall()
	print("MASUK")
	return HttpResponse(json.dumps(top_performers_IF))


def student_by_nim(request,nim) :

	if request.user.is_authenticated :
		

		student = Student.objects.get(nim=nim)
		current_student = Student.objects.get(email = request.user.email)
		
		# Check whether renewed rating and comment is sent by post
		if request.method == "POST" :
			
			current_student = Student.objects.get(email = request.user.email)
			student = Student.objects.get(nim=nim)

			current_rep = Reputation.objects.all().filter(receiver_id = student.id, sender_id = current_student.id).first()

			if current_rep is None :

				# Save new reputation
				current_rep = Reputation.objects.create(receiver_id = student.id, rating = request.POST.get('rating'), comment = request.POST.get('comment'), sender_id = current_student.id)
			
			else :

				# Update reputation
				current_rep.comment = request.POST.get('comment')
				current_rep.rating = request.POST.get('rating')
				current_rep.save()

		# Get student object


		reputations = Reputation.objects.all().filter(receiver_id=student)
		page = request.GET.get('page',1)

		# Get user comment object for the specified student by the authenticated student
		current_rep = Reputation.objects.all().filter(receiver_id = student.id, sender_id = current_student.id).first()

		paginator = Paginator(reputations,10)

		try:
			reputations = paginator.page(page)
		except PageNotAnInteger:
			reputations = paginator.page(1)
		except EmptyPage:
			reputations = paginator.page(paginator.num_pages)
		average_rating = Reputation.objects.all().filter(receiver=student).aggregate(Avg('rating'))

		data = {

			"student":student,
			"reputations":reputations,
			"average_rating" : average_rating["rating__avg"],
			"current_rep" : current_rep
		}
		return render(request,"skippedia/student_temp.html",data)

	else :

		return redirect('/')

def setting(request) :
	return HttpResponse("Setting")

def logout(request) :
	return HttpResponse("logout")
