from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
	#urls mapping the views of the application come here
	#url(r'^home/$',views.home,name ='home'),
	url(r'^login/$',auth_views.login,{'template_name':'clinicianLogin.html'},name ='login'),
	url(r'^logout/$',auth_views.logout,{'template_name':'logout.html'},name ='logout'),
	#url(r'^clinicianLogin/$',views.clinicianLogin,name ='clogin'),
	url(r'^managePatient/$',views.managePatient,name ='managePatient'),
	url(r'^manageClinician/$',views.manageClinician,name ='manageClinician'),
	url(r'^visitDetails/$',views.visit,name ='visitDetails'),
	url(r'^p_medical_info/$',views.patientMadicalInfo,name ='p_medical_info'),
	url(r'^dashboard/$',views.clinicianDashboard,name ='clinician_dashboard'),
	url(r'^Admin/$',views.Admin,name ='admin'),
]