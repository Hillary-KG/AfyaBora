from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
	#urls mapping the views of the application come here
	url(r'^login/$',views.clinician_login,name ='login'),#clinician login
	url(r'^logout/$',views.logout_view,name ='logout'),#clinician logout
	url(r'^managePatient/$',views.managePatient,name ='managePatient'),#page to manage patient
	url(r'^manageClinician/$',views.manageClinician,name ='manageClinician'),#page to manage the clinician
	url(r'^visitDetails/$',views.visit,name ='visitDetails'),#page to view patient ART details 
	url(r'^p_medical_info/$',views.patientMadicalInfo,name ='p_medical_info'),#page to edit patient medical information
	url(r'^clinician_home/$',views.clinician_home,name ='clinician_home'),#clinician dashboard
	url(r'^Admin/$',views.Admin,name ='admin'),
	url(r'^register/$',views.registerClinician,name ='register'),#clinician registration
	url(r'^home',views.home_view,name='home'),
	url(r'^ussd/$',views.callback, name = 'callback'),
]