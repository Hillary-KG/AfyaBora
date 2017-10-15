from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
def index(request):
	return HttpResponse("You are now in the index page")

# from django.shortcuts import render_to_response

# Create your views here.
def login(request):
	return HttpResponse('login.html',locals())
def myAdmin(request):
	return HttpResponse('admin.html',locals())
def managePatient(request):
	return HttpResponse('managePatient.html',locals())
def manageClinician(request):
	return HttpResponse('manageStaff.html',locals())
def medication(request):
	return HttpResponse('medication.html',locals())
	