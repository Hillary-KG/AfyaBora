from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ClinicianForm,ClinicianProfileForm,ClinicianProfile,PatientBioData,ARTVisitDetails,PatientMedicalData,Tester
@csrf_exempt
def ussd(request):
	if request.method = 'POST' and request.POST:
		sessionId = request.POST.get('sessionId')
		serviceCode =request.POST.get('serviceCode')
		phoneNumber =request.POST.get('phoneNumber')
		text=request.POST.get('text')
		clinician_phone = ClinicianProfile.objects.get(phone_no = phoneNumber)
		if clinician_phone = 
			pass
