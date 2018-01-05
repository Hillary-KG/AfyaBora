from django.shortcuts import render
from django.http import HttpResponse 
from .forms import *


# Create your views here.
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
	return render(request,'home.php',context)
def managePatient(request):
	context = {
	}
	return render(request,'managePatient.html',context)
def manageClinician(request):
	context = {
	}
	return render(request,'manageClinician.html',context)
def medicationDetails(request):
	context = {
	}
	return render(request,'medication.html',context)
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
	return render(request,'clinicianDashboard.php',context)