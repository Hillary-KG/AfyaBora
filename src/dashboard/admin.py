from django.contrib import admin

from .models import *


class BioData(admin.ModelAdmin):
	list_display = ['patient_no','first_name','sir_name','age','age']
class NextOfKin(admin.ModelAdmin):
	list_display = ['sir_name','first_name','relationship']
class MedicalData(admin.ModelAdmin):
	list_display = ['patient_no','date_confirmed','date_enrolled','entry_point','CD4_count','DLD']
class Visit(admin.ModelAdmin):
	list_display= ['patient_no','visit_date','tests_done','comments']
class TransferIn(admin.ModelAdmin):
	list_display = ['patient_no','sir_name','second_name','facility_from','date_confirmed','date_enrolled']
class ClinicianDetails(admin.ModelAdmin):
	list_display = ['sir_name','second_name','job_number','facility']
class ClinicianLogin(admin.ModelAdmin):
	list_display = ['job_number','sir_name','second_name','email_address']
class AdminLogin(admin.ModelAdmin):
	list_display = ['sir_name','last_name','email_address','Login_time']
		
# Register your models here.
admin.site.register(Bio_data,BioData)
admin.site.register(Next_of_Kin,NextOfKin)
admin.site.register(Medical_data,MedicalData)
admin.site.register(Visit_details,Visit)
admin.site.register(Transfer_in,TransferIn)
admin.site.register(Clinician_details,ClinicianDetails)
admin.site.register(Clinician_login,ClinicianLogin)
admin.site.register(Admin_login,AdminLogin)


