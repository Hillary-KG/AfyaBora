from django.contrib import admin

from .models import *

class PatientAdmin(admin.ModelAdmin):
	list_display = ['first_name','sir_name','age','visiting_date','residence']
class DoctorAdmin(admin.ModelAdmin):
	list_display = ['job_number','first_name','sir_name']
class Login(admin.ModelAdmin):
	pass
class Medication(admin.ModelAdmin):
	list_display = ['first_name','sir_name','start_date']
class StaffLogin(admin.ModelAdmin):
	list_display = ['__str__','job_number']
class AdminLogin(admin.ModelAdmin):
	list_display = ['time','email_address']
		
# Register your models here.
admin.site.register(Staff_login,StaffLogin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Health_staff,DoctorAdmin)
admin.site.register(Patient_medication,Medication)
admin.site.register(Admin_login,AdminLogin)
