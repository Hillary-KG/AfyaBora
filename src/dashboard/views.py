from django.shortcuts import render
from django.http import HttpResponse 
from .forms import *


# Create your views here.
def home_view(request):
	context={
	}
	return render(request,'ART_home.html',context);
def clinicianLogin(request):

	# title = "Welcome"
	# login_form = LoginForm()
	context = {
		# "title":title,
		# "login":login_form
	}
	return render(request,'clinicianLogin.php',context)
def home(request):
	context = {
	}
	return render(request,'home.html',context)
def managePatient(request):
	context = {
	}
	return render(request,'managePatient.html',context)
def manageClinician(request):
	context = {
	}
	return render(request,'manageClinician.html',context)
def patientMadicalInfo(request):
	context = {
	}
	return render(request,'patientMedicalInfo.html',context)
def visit(request):
	context = {
	}
	return render(request,'visit.html',context)
def Admin(request):
	context = {
	}
	return render(request,'admin.html',context)
def clinicianDashboard(request):
	context = {
	}
	return render(request,'clinicianDashboard.html',context)
def index(request):
	context={

	}
	return render(request,'index.php',context)