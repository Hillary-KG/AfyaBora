from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bio_data(models.Model):
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	first_name = models.CharField(null=False,blank=False,max_length=30)
	second_name = models.CharField(null=False,blank=False,max_length=30)
	DOB = models.DateField(null=False,blank=False)
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
class Next_of_kin(models.Model):
	first_name = models.CharField(null=False,blank=False,max_length=30)
	sir_name = models.ForeignKey(Bio_data,on_delete=models.CASCADE)
	phone_no = models.IntegerField(null=False,blank=False)
	relationship = models.CharField(null=False,blank=False,max_length=40)
	def __str__(self):
		return self.relationship
	class Admin:
		pass
	class Meta:
		ordering = ['sir_name']
class Medical_Data(models.Model):
	date_confirmed = models.DateField(null=False,blank=False)
	date_enrolled = models.DateTimeField(null=False,blank=False)
	used_arv = models.CharField(blank=False,null=False,max_length=10)#######
	spouse = models.CharField(null=True,blank=True,max_length=40)
	known_allergies = models.CharField(null=True,blank=True,max_length=200)
	entry_point = models.CharField(null=False,blank=False,max_length=30)
	CD4_count = models.IntegerField(null=True,blank=True) # only applies for new patients
	def __str__(self):
		return self.date_confirmed
	class Admin:
		pass
	class Meta:
		ordering = ['date_confirmed']
class Transfer_in(models.Model):
	#medical data is a must have for one to get a refill or enrollment 
	date_coming = models.DateField(null=False,blank=False)
	facility_from = models.CharField(null=False,blank=False,max_length=50)
	date_confirmed = models.DateField(null=False,blank=False)
	date_enrolled = models.DateField(null=False,blank=False)
	date_started_ART = models.DateField(null=False,blank=False)
	def __str__(self):
		return self.date_coming
	class Admin:
		pass
	class Meta:
		ordering = ['facility_from']
class Visit_details(models.Model):
	visit_date = models.DateTimeField(blank=False,null=False)
	DLD = models.CharField(blank=False,null=False,max_length=20)#Viral load
	CD4_count = models.ForeignKey(Medical_Data,blank=False,null=False)
	refilled = models.CharField(blank=False,null=False,max_length=10)#yes if they got a refill and no if they didn't #####
	def __str__(self):
		return self.visit_date
	class Admin:
		pass
	class Meta:
		ordering = ['visit_date']

class Health_staff(models.Model):
	first_name = models.CharField(null=False,blank=False,max_length=30)
	second_name = models.CharField(null=False,blank=False,max_length=30)
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	job_number = models.IntegerField(null=False,blank=False,primary_key=True)
	Health_centre = models.CharField(blank=False,null=False,max_length=100)
	def __str__(self):
		self.job_number = str(self.job_number)
		return self.job_number
	#adding admin class to allow the model to be editable form the Django admin interface
	class Admin:
		pass
	class Meta:
		ordering = ['sir_name']


############################################################################################

# class Patient(models.Model):
# 	"""docstring for ClassName"""
# 	patient_no = models.IntegerField(primary_key=True);
# 	first_name = models.CharField(null=False,blank=False,max_length=30)
# 	second_name = models.CharField(null=False,blank=False,max_length=30)
# 	sir_name = models.CharField(null=False,blank=False,max_length=30)
# 	id_no = models.IntegerField(null=False,blank=False)
# 	residence = models.CharField(null=False,blank=False,max_length=30)
# 	age = models.IntegerField(null=True,blank=True)
# 	visiting_date = models.DateTimeField(auto_now=True,blank=False,null=False)
# 	occupation = models.CharField(null=False,blank=False,max_length=30)
# 	def __str__(self):
# 		return self.sir_name
# 	#adding admin class to allow the model to be editable form the Django admin interface
# 	class Admin:
# 		pass
# 	class Meta:
# 		ordering = ['sir_name']
# class Health_staff(models.Model):
# 	first_name = models.CharField(null=False,blank=False,max_length=30)
# 	second_name = models.CharField(null=False,blank=False,max_length=30)
# 	sir_name = models.CharField(null=False,blank=False,max_length=30)
# 	job_number = models.IntegerField(null=False,blank=False,primary_key=True)
# 	def __str__(self):
# 		self.job_number = str(self.job_number)
# 		return self.job_number
# 	#adding admin class to allow the model to be editable form the Django admin interface
# 	class Admin:
# 		pass
# 	class Meta:
# 		ordering = ['sir_name']
# class Patient_medication(models.Model):
# 	med_name = models.CharField(null=False,blank=False,max_length=30)
# 	patient_no = models.ForeignKey(Patient,on_delete=models.CASCADE)
# 	first_name = models.CharField(null=False,blank=False,max_length=30)
# 	sir_name = models.CharField(max_length=50,null=False,blank=False)
# 	start_date = models.DateTimeField(null=False,blank=False)
# 	def __str__(self):
# 		return self.sir_name
# class Staff_login(models.Model):
# 	email_address = models.EmailField(primary_key=True,null=False)
# 	pswd = models.CharField(max_length=30,null=False,blank=False)
# 	job_number = models.IntegerField(null=False,blank=False)
# 	time = models.DateTimeField(auto_now = True)
# 	def __str__(self):
# 		return self.email_address
# class Admin_login(models.Model):
# 	email_address = models.EmailField(primary_key=True,null=False,blank=False)
# 	time = models.DateTimeField(auto_now_add = False,auto_now = True)
# 	pswd = models.CharField(max_length=30,null=False,blank=False)
# 	"""docstring for Admin_Login"""
# 	def __init__(self):
# 		return self.email_address
		

	