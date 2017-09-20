from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
def index(request):
	return HttpResponse("You are now in the index page")

# from django.shortcuts import render_to_response

# # Create your views here.
# def login(request):
# 	return render_to_response('login.html',locals())
# def myAdmin(request):
# 	return render_to_response('admin.html',locals())
# def manage_patient(request):
# 	return render_to_response('manage_patient.html',locals())
# def manage_staff(request):
# 	return render_to_response('manage_staff.html',locals())
# def patient_medication(request):
# 	return render_to_response('medication.html',locals())
# 	