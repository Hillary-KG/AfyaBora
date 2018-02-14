from django.shortcuts import render
from django.http import HttpResponse 
from .forms import *
from .models import ClinicianForm,ClinicianProfileForm,ClinicianProfile,PatientBioData,ARTVisitDetails,PatientMedicalData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# from afyasmart.settings import MEDIA_ROOT
#importing the africastalking api 
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
from africastalking.config import username,apikey
from .models import session_levels
import datetime


# Create your views here.
#ussd view 
def callback(request):
	response = None
	if request.method == 'POST'and request.POST:
		sessionId = request.POST.get('sessionId')
		serviceCode =request.POST.get('serviceCode')
		phoneNumber =request.POST.get('phoneNumber')
		text=request.POST.get('text')
		now = datetime.datetime.now()
		textList = text.split('*')
		userResponse = textList[-1].strip()
	# #4. Check the level of the user from the DB and retain default level if none is found for this session
		try:
			result = ClinicianProfile.objects.get(phone_no = phoneNumber)
			level = session.level
		except ClinicianProfile.DoesNotExist as e:
			level=0 
		if result == True:
			if userResponse == "":
				if level == 0:
					session_level1 = ClinicianProfile.objects.get(phone_no = phoneNumber) 
					session_level1.level = 1
					session_level1.save()
					#service menu 
					response = "CON Welcome to ART Bora.\n"
					response += "1. Please input ID number or phone number of the patient.\n"
					return HttpResponse(response,content_type="text/plain")
			if userResponse == "0":
				if level == 0 :
					session1 = session_levels(session_id= sessionId, phoneNumber = phoneNumber, level=1) 
					session1.save() 
					response = "CON Welcome to ART Bora.\n"
					response += "1. Please input ID number or phone number of the patient.\n"
					return HttpResponse(response,content_type="text/plain")
			if userResponse == "":
				if level == 1:
					session_level1 = ClinicianProfile.objects.get(phone_no = phoneNumber) 
					session_level1.level = 1
					session_level1.save()
					response = "CON Welcome to ART Bora.\n"
					response += "1. Please input ID number or phone number of the patient.\n"
					return HttpResponse(response,content_type="text/plain")
			# patient_id = PatientBioData.objects.get(id_no=userResponse)
			# patient_phone = PatientBioData.objects.get(phone_no=userResponse)
			if userResponse == PatientBioData.objects.get(id_no=userResponse) or userResponse == PatientBioData.objects.get(phone_no=userResponse):
				patientName = PatientBioData.objects.get(id_no=userResponse).first_name
				if level == 1:
					response = "CON Select "+patientName+"'s"+" information to access\n"
					response += "1. visit details\n"
					response += "2. CD4 count.\n"
					response += "3. DLD.\n"
					return HttpResponse(response,content_type="text/plain")
			if userResponse == 1:
				if level == 1:
					p_no = PatientBioData.objects.get(id_no=userResponse).patient_no
					visitDetails = ARTVisitDetails.objects.get(patient_no=p_no)
					print (visitDetails)
					response = "END Thankyou"
					print(response)
					return HttpResponse(response,content_type="text/plain")
			if userResponse == 2:
				if  level == 1:
					p_no = PatientBioData.objects.get(id_no=userResponse).patient_no
					DLD = PatientMedicalData.objects.get(patient_no=p_no).CD4_count
					print(DLD)
					response = "END Thankyou"
					print(response)
					return HttpResponse(response,content_type="text/plain")
			if userResponse == 3:
				if  level == 1:
					p_no = PatientBioData.objects.get(id_no=userResponse).patient_no
					DLD = PatientMedicalData.objects.get(patient_no=p_no).DLD
					print(DLD)
					response = "END Thankyou"
					print(response)
					return HttpResponse(response,content_type="text/plain")

		
		#continue to process the ussd 
	else:
		response == "END Something went wrong,Sorry"
		print("This number is not for a registered clinician,please use the registered phone number\n")
		return HttpResponse(response,content_type="text/plain")


@login_required(login_url='/dashboard/login/')
def registerClinician(request):
	registered = False 
	if request.method == 'POST':
		clinician_form = ClinicianForm(data = request.POST)
		profile_form = ClinicianProfileForm(data = request.POST)
		if clinician_form.is_valid() and profile_form.is_valid():
			clinician = clinician_form.save()
			pw = clinician.password
			clinician.set_password(pw)
			profile = profile_form.save(commit=False)
			profile.clinician = clinician
			clinician.save()
			# save_file(request.FILES['picture'])
			registered = True
		else:
			print("success!")
	else:
		clinician_form = ClinicianForm()
		profile_form = ClinicianProfileForm()
	context = {
			'clinician_form':clinician_form,
			'profile_form':profile_form,
			'registered':registered
		}
	return render(request,'register_clinician.html',context)
# #function to save the image in the media root directory set in the setting.py
# def save_file(file,path=''):
# 	file_name = file._get_name()
# 	fd = open('%s/%s'%(MEDIA_ROOT,str(file_name)),'wb')
# 	for chunk in file.chunks():
# 		fd.write(chunk)
# 	fd.close()

def clinician_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		clinician = authenticate(username=username,password=password)
		if clinician is not None:
			if clinician.is_active:
				login(request,clinician)
				return redirect("clinician_home")
			else:
				return HttpResponse('Your account has been deactivated, please contact admin for assistance')
		else:
			print("Invalid login details:" + username + " " + password)
			return render(request,'login.html',{})
	else:
		return render(request,'login.html',{})
def home_view(request):
	context={
	}
	return render(request,'ART_home.html',{});

def logout_view(request):
    logout(request)
    print("You have successfully logged out")
    redirect('home')
    # Redirect to a success page.


def clinician_home(request):
	context = {
	}
	return render(request,'ART_home.html',context)
@login_required(login_url='/dashboard/login/')
def managePatient(request):
	context = {
	}
	return render(request,'managePatient.html',context)
@login_required(login_url='/dashboard/login/')
def manageClinician(request):
	context = {
	}
	return render(request,'manageClinician.html',context)
@login_required(login_url='/dashboard/login/')
def patientMadicalInfo(request):
	context = {
	}
	return render(request,'patientMedicalInfo.html',context)
@login_required(login_url='/dashboard/login/')
def visit(request):
	context = {
	}
	return render(request,'visit.html',context)
def Admin(request):
	context = {
	}
	return render(request,'admin.html',context)
@login_required(login_url='/dashboard/login/')
def clinician_home(request):
	context = {
	}
	return render(request,'clinician_home.html',context)
def index(request):
	context={

	}
	return render(request,'index.php',context)