from django import forms

class NewStudentForm(forms.Form):
	email = forms.EmailField()
	nama = forms.CharField(max_length=255)
	nim = forms.CharField(max_length=8)
	jurusan = forms.CharField(max_length=3)
	angkatan = forms.IntegerField()