from django.contrib import admin

from .models import *


class BioData(admin.ModelAdmin):
	list_display = ['patient_no','first_name','sir_name']
class Next_of_Kin(admin.ModelAdmin):
	list_display = ['sir_name','first_name','relationship']
class MedicalData(admin.ModelAdmin):
	list_display = ['patient_no','date_confirmed','date_enrolled','entry_point','CD4_count','DLD']
class Visit(admin.ModelAdmin):
	list_display= ['patient_no','visit_date','tests_done','comments']
class TransferIn(admin.ModelAdmin):
	list_display = ['patient_no','first_name','last_name','ccc_from','date_confirmed','date_enrolled']
class ClinicianDetails(admin.ModelAdmin):
	list_display = ['first_name','last_name','job_id','facility']
class Clinician_Login(admin.ModelAdmin):
	list_display = ['job_id','login_time']
class AdminLogin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email_address','login_time']
# class SpouseDetails(admin.ModelAdmin):
# 	list_display = ['patient_no','first_name','last_name']
		
# Register your models here.
admin.site.register(PatientBioData,BioData)
admin.site.register(NextOfKin,Next_of_Kin)
admin.site.register(PatientMedicalData,MedicalData)
admin.site.register(ARTVisitDetails,Visit)
admin.site.register(TransferInPatient,TransferIn)
admin.site.register(ClinicianData,ClinicianDetails)
admin.site.register(ClinicianLogin,Clinician_Login)
admin.site.register(AdminLoginCredentials,AdminLogin)
#admin.site.register(Spouse,SpouseDetails)


