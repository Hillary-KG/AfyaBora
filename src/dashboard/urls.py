from django.conf.urls import url
from . import views 

urlpatterns = [
	#urls mapping the views of the application come here
	url(r'^home/$',views.home,name ='home'),
	url(r'^clinicianLogin/$',views.clinicianLogin,name ='clogin'),
	url(r'^managePatient/$',views.managePatient,name ='managePatient'),
	url(r'^manageClinician/$',views.manageClinician,name ='manageClinician'),
	url(r'^visitDetails/$',views.visit,name ='visitDetails'),
	url(r'^medicationDetails/$',views.medicationDetails,name ='medicationDetails'),
	url(r'^dashboard/$',views.clinicianDashboard,name ='clinician_dashbd'),
	url(r'^Admin/$',views.Admin,name ='admin'),
]