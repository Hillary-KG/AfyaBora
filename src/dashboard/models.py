from __future__ import unicode_literals

from django.db import models
#import datetime

# Create your models here.
class PatientBioData(models.Model):
	patient_no = models.IntegerField(primary_key=True,blank=False,null=False)
	sir_name = models.CharField(max_length=50,null=False,blank=False)
	first_name = models.CharField(max_length=50,null=False,blank=False)
	last_name = models.CharField(max_length=50,null=False,blank=False)
	DOB = models.DateField(null=True,blank=True)
	id_no = models.IntegerField(blank=True,null=True)
	phone_no = models.IntegerField(null=False,blank=False)
	NoK = models.CharField(max_length=50,null=True,blank=True,default=None)####
	physical_address = models.CharField(max_length=60,null=False,blank=False)
	def __str__(self):
		return (self.sir_name,self.last_name)
	#adding admin class to allow the model to be editable form the Django admin interface
	class Admin:
		pass
	class Meta:
		ordering=['patient_no']

class NextOfKin(models.Model):
	patient_no = models.ForeignKey(PatientBioData,on_delete=models.CASCADE,primary_key=True,blank=False,null=False)
	sir_name = models.CharField(max_length=50,blank=False,null=False)
	first_name = models.CharField(max_length=50,null=False,blank=False)
	phone_no = models.IntegerField(null=False,blank=False)
	relationship = models.CharField(max_length=30,null=False,blank=False)
	def __str__(self):
		return (self.sir_name,self.last_name)
	class Admin:
		pass 
	class Meta:
		ordering=['patient_no']

class PatientMedicalData(models.Model):
	patient_no = models.ForeignKey(PatientBioData,on_delete=models.CASCADE,primary_key=True,blank=False,null=False)
	date_confirmed = models.DateField(blank=False,null=False,auto_now_add = False,auto_now = False)
	date_enrolled = models.DateField(blank=False,null=False,auto_now_add = False,auto_now = False)
	used_arv = models.CharField(blank=False,null=False,max_length=20)####
	known_allergies = models.CharField(null=True,blank=True,max_length=500)
	entry_point = models.CharField(null=False,blank=False,max_length=30)######
	CD4_count = models.IntegerField(null=True,blank=True) # only applies for new patients
	DLD = models.CharField(blank=False,null=False,max_length=50) #viral load
	def __str__(self):
		return self.patient_no
	class Admin:
		pass 
	class Meta:
		ordering=['patient_no']

class ARTVisitDetails(models.Model):
	YES = 'Yes'
	NO = 'No'
	DRUG_REFILLED_CHOICES = (
		(YES,'refilled'),
		(NO,'Not refilled'),
		)
	patient_no = models.ForeignKey(PatientBioData,on_delete=models.CASCADE,primary_key=True,blank=False,null=False)
	visit_date = models.DateField(blank=False,null=False,auto_now_add = False,auto_now = False)
	drug_refill = models.CharField(max_length=5,choices = DRUG_REFILLED_CHOICES,default ='Yes')######
	tests_done = models.TextField(max_length=500,blank=False,null=False)######
	comments = models.TextField(max_length=1000)
	def __str__(self):
		return self.visit_date
	class Meta:
		ordering=['patient_no']

class TransferInPatient(models.Model):
	#medical data is a must have for one to get a refill or enrollment 
	patient_no = models.IntegerField(blank=False,null=False,default=001,primary_key=True)#capture or assign new if not remembered 
	sir_name = models.CharField(null=False,blank=False,max_length=30)
	first_name = models.CharField(null=False,blank=False,max_length=30)
	last_name = models.CharField(null=False,blank=False,max_length=30)
	DOB = models.DateField(auto_now_add = False,auto_now = False)
	incoming_date = models.DateField(auto_now_add = False,auto_now = False)
	ccc_from = models.CharField(null=False,blank=False,max_length=50)
	date_confirmed = models.DateField(auto_now_add = False,auto_now = False)
	date_enrolled = models.DateField(auto_now_add = False,auto_now = False)
	def __str__(self):
		return (self.sir_name,self.last_name)
	class Admin:
		pass
	class Meta:
		ordering = ['patient_no']

class ClinicianData(models.Model):
	job_id = models.IntegerField(null=False,blank=False)
	first_name = models.CharField(max_length=50,null=False,blank=False)
	last_name = models.CharField(max_length=50,null=False,blank=False)
	email_address = models.EmailField(primary_key=True,blank=False,null=False)
	facility = models.CharField(max_length=100,blank=False,null=False)
	def __str__(self):
		return (self.job_id,self.first_name,self.last_name)

class ClinicianLoginCredentials(models.Model):
	job_id = models.IntegerField(null=False,blank=False)
	email_address = models.ForeignKey(ClinicianData,primary_key=True,blank=False,null=False)
	pswd = models.CharField(max_length=100,null=False,blank=False)
	login_time = models.DateTimeField(auto_now_add = False,auto_now = True,blank=False,null=False)
	def __str__(self):
		return (self.email_address,self.login_time)
	class Admin:
		pass
	class Meta:
		ordering = ['email_address']

class AdminLoginCredentials(models.Model):
	email_address = models.EmailField(primary_key=True,null=False,blank=False)
	first_name = models.CharField(null=False,blank=False,max_length=30)
	last_name = models.CharField(null=False,blank=False,max_length=30)
	login_time = models.DateTimeField(blank=False,null=False,auto_now_add = False,auto_now = True)
	pswd = models.CharField(max_length=30,null=False,blank=False)
	"""docstring for Admin_Login"""
	def __str__(self):
		return (self.email_address,self.login_time)

class SecondaryCondition(models.Model):
	condition_name = models.CharField(max_length=50,null=False,blank=False)
	date_tested = models.DateField(blank=False,null=False,auto_now_add = False,auto_now = False)
	comments = models.CharField(max_length=500,null=True,blank=True)
	def __str__(self):
		return (self.condition_name,self.date_tested)
# class Spouse(models.Model):
# 	patient_no = models.ForeignKey(Bio_data,blank=False,null=False)
# 	first_name = models.CharField(blank=False,null=False,max_length=30)
# 	last_name = models.CharField(blank=False,null=False,max_length=30)
# 	phone_no = models.IntegerField(blank=False,null=False)
# 	status = models.CharField(max_length=30,blank=False,null=False)
# 	def __str__(self):
# 		return self.first_name


############################################################################################


	