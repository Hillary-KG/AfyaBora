from django.contrib import admin

from .models import *


class BioData(admin.ModelAdmin):
	list_display = ['patient_no','first_name','sir_name']
	search_fields = ['patient_no','first_name','sir_name']
	list_filter = ['date_created','date_updated']
class Next_of_Kin(admin.ModelAdmin):
	list_display = ['sir_name','first_name','relationship']
	search_fields = ['sir_name','first_name']
class MedicalData(admin.ModelAdmin):
	list_display = ['patient_no','date_confirmed','date_enrolled','entry_point','CD4_count','DLD']
	search_fields = ['patient_no']
class Visit(admin.ModelAdmin):
	list_display= ['patient_no','visit_date','tests_done','comments']
	search_fields = ['patient_no']
class TransferIn(admin.ModelAdmin):
	list_display = ['patient_no','first_name','last_name','ccc_from','date_confirmed','date_enrolled']
	search_fields = ['patient_no','first_name','last_name']
class ClinicianDetails(admin.ModelAdmin):
	list_display = ['job_id','first_name','last_name','facility']
	search_fields = ['job_id','first_name','last_name']
class Clinician_Login(admin.ModelAdmin):
	list_display = ['job_id','login_time']
class AdminLogin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email_address','login_time']
class TransitPatient(admin.ModelAdmin):
	list_display=['temp_no','first_name','last_name','visit_date','drug_refill']
	search_fields = ['temp_no','first_name','last_name']
class Clinician(admin.ModelAdmin):
	list_display = ['job_id','first_name','last_name','login_time','status']
	search_fields = ['job_id','first_name','last_name']
# class SpouseDetails(admin.ModelAdmin):
# 	list_display = ['patient_no','first_name','last_name']
		
# Register your models here.
admin.site.register(PatientBioData,BioData)
admin.site.register(NextOfKin,Next_of_Kin)
admin.site.register(PatientMedicalData,MedicalData)
admin.site.register(ARTVisitDetails,Visit)
admin.site.register(TransferInPatient,TransferIn)
# admin.site.register(ClinicianData,ClinicianDetails)
#admin.site.register(ClinicianLogin,Clinician_Login)
admin.site.register(AdminLoginCredentials,AdminLogin)
admin.site.register(Transit_patient,TransitPatient)
admin.site.register(ClinicianProfile,Clinician)
#admin.site.register(Spouse,SpouseDetails)


