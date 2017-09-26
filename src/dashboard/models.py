from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bio_data(models.Model):
	patient_no = models.IntegerField(primary_key=True,blank=False,null=False,default=001)
	sir_name = models.CharField(null=False,blank=False,max_length=30,default='')
	first_name = models.CharField(null=False,blank=False,max_length=30,default='')
	second_name = models.CharField(null=False,blank=False,max_length=30,default='')
	DOB = models.DateTimeField(null=True,blank=True)
	phone_no = models.IntegerField(null=False,blank=False)
	id_no = models.IntegerField(null=False,blank=False)
	age = models.IntegerField(null=True,blank=True)
	NoK = models.CharField(null=True,blank=True,max_length=30)
	physical_address = models.CharField(null=False,blank=False,max_length=30)
	def __str__(self):
		return self.sir_name
	#adding admin class to allow the model to be editable form the Django admin interface
	class Admin:
		pass
	class Meta:
		ordering = ['sir_name']
class Next_of_Kin(models.Model):
	sir_name = models.ForeignKey(Bio_data,on_delete=models.CASCADE)
	first_name = models.CharField(null=False,blank=False,max_length=30,default='')
	phone_no = models.IntegerField(null=False,blank=False)
	relationship = models.CharField(null=False,blank=False,max_length=40,default='None')
	def __str__(self):
		return self.sir_name
	class Admin:
		pass 
	class Meta:
		ordering=['sir_name']
class Medical_data(models.Model):
	patient_no = models.IntegerField(blank=False,null=False,default=001)
	date_confirmed = models.DateField(auto_now_add = False,auto_now = False)
	date_enrolled = models.DateField(auto_now_add = False,auto_now = False)
	used_arv = models.CharField(blank=False,null=False,max_length=20,default='None')
	spouse = models.CharField(null=True,blank=True,max_length=40,default='None')
	known_allergies = models.CharField(null=True,blank=True,max_length=500)
	entry_point = models.CharField(null=False,blank=False,max_length=30,default='None')
	CD4_count = models.IntegerField(null=True,blank=True,default=0000) # only applies for new patients
	DLD = models.CharField(blank=False,null=False,max_length=50,default='') #viral load
	def __str__(self):
		return self.patient_no
	class Admin:
		pass 
	class Meta:
		ordering=['patient_no']
class Visit_details(models.Model):
	patient_no = models.ForeignKey(Medical_data,blank=False,null=False,on_delete=models.CASCADE,default=001)
	sir_name= models.CharField(blank=False,null=False,max_length=50)
	last_name = models.CharField(blank=False,null=False,max_length=50)
	visit_date = models.DateField(auto_now_add = False,auto_now = False)
	refilled = models.CharField(blank=False,null=False,max_length=30)######
	tests_done = models.CharField(blank=False,null=False,max_length=500)
	comments = models.CharField(blank=False,null=False,max_length=500)
	def __str__(self):
		return self.visit_date

class Transfer_in(models.Model):
	#medical data is a must have for one to get a refill or enrollment 
	patient_no = models.IntegerField(blank=False,null=False,default=001)#capture or assign new if not remembered 
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	first_name = models.CharField(null=False,blank=False,max_length=30)
	second_name = models.CharField(null=False,blank=False,max_length=30)
	DOB = models.DateField(auto_now_add = False,auto_now = False)
	date_coming = models.DateField(auto_now_add = False,auto_now = False)
	facility_from = models.CharField(null=False,blank=False,max_length=50)
	date_confirmed = models.DateField(auto_now_add = False,auto_now = False)
	date_enrolled = models.DateField(auto_now_add = False,auto_now = False)
	date_started_ART = models.DateField(auto_now_add = False,auto_now = False)
	def __str__(self):
		return self.facility_from
	class Admin:
		pass
	class Meta:
		ordering = ['date_coming']

class Clinician_details(models.Model):
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	first_name = models.CharField(null=False,blank=False,max_length=30)
	second_name = models.CharField(null=False,blank=False,max_length=30)
	job_number = models.IntegerField(null=False,blank=False,primary_key=True)
	facility = models.CharField(blank=False,null=False,max_length=100)
	def __str__(self):
		return self.email_address

class Clinician_login(models.Model):
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	second_name = models.CharField(null=False,blank=False,max_length=30)
	email_address = models.EmailField(primary_key=True,null=False)
	pswd = models.CharField(max_length=30,null=False,blank=False)
	job_number = models.IntegerField(null=False,blank=False)
	last_login_time = models.DateTimeField(auto_now = True)
	def __str__(self):
		return email_address
	class Admin:
		pass
	class Meta:
		ordering = ['sir_name']

class Admin_login(models.Model):
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	last_name = models.CharField(null=False,blank=False,max_length=30)
	email_address = models.EmailField(primary_key=True,null=False,blank=False)
	Login_time = models.DateTimeField(auto_now_add = False,auto_now = True)
	pswd = models.CharField(max_length=30,null=False,blank=False)
	"""docstring for Admin_Login"""
	def __init__(self):
		return self.email_address
		

############################################################################################


	