from .models import session_levels,ClinicianProfile,PatientMedicalData,PatientBioData

from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
from africastalking.config import username,apikey
from django.http import HttpResponse 
def callback(request):
	if request.method == 'POST'and request.POST:
		sessionId = request.POST.get('sessionId')
		serviceCode =request.POST.get('serviceCode')
		phoneNumber =request.POST.get('phoneNumber')
		text=request.POST.get('text')
		now = datetime.datetime.now()
		textList = text.split('*')
		userResponse = textList[-1].strip()
		trial = Tester(trial=1)
		trial.save()

		try:
			session_level = session_levels.objects.get(session_id=sessionId)
			if session_level.level == 1:
				if userResponse == PatientBioData.objects.get(id_no=userResponse) or userResponse == PatientBioData.objects.get(phone_no=userResponse):
					patientName = PatientBioData.objects.get(id_no=userResponse).first_name
					response = "CON Select "+patientName+"'s"+" information to access\n"
					response += "1. visit details\n"
					response += "2. CD4 count.\n"
					response += "3. DLD.\n"
					session_level.level=2
					session_level.p_no = PatientBioData.objects.get(phone_no=userResponse).patient_no
					session_level.p_id = PatientBioData.objects.get(phone_no=userResponse).id_no
					session_level.save()
				else:
					response="END Not found"
					return HttpResponse(response,content_type="text/plain")
			elif session_level.level==2:
				if userResponse=="1":
					patientNo = session_level.p_no
					visitDetails = ARTVisitDetails.objects.get(patient_no=patientNo)
					print (visitDetails)
					response = "END Thankyou"
					return HttpResponse(response,content_type="text/plain")
				elif userResponse=="2":
					patientNo = session_level.p_no
					CD4_count = PatientMedicalData.objects.get(patient_no=p_no).CD4_count
					print(CD4_count)
					response = "END Thankyou"
					print(response)
					return HttpResponse(response,content_type="text/plain")
				elif userResponse=="3":
					patientNo = session_level.p_no
					DLD = PatientMedicalData.objects.get(patient_no=p_no).DLD
					print(DLD)
					response = "END Thankyou"
					return HttpResponse(response,content_type="text/plain")
				else:
					response = "END Wrong input"
					return HttpResponse(response,content_type="text/plain")
		except session_levels.DoesNotExist:
			response = "END Error"

		try:
			result = ClinicianProfile.objects.get(phone_no = phoneNumber)
			if result:
				if text=="":
					response = "CON Welcome to ART Bora.\n"
					response += "1. Please input ID number or phone number of the patient.\n"
					session_level = session_levels(session_id=sessionId,phonenumber=phoneNumber,level=1)
					session_level.save()
				elif 
			else:
					response = "END Error"
		except ClinicianProfile.DoesNotExist as e:
			response = "END Error"
