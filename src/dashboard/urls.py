from django.conf.urls import url
from . import views 

urlpatterns = [
	#urls mapping the views of the application come here
	url(r'^$',views.login,name ='login'),
# 	url(r'^$',views.login,name = 'login'),
# 	url(r'^$',views.myAdmin,name ='myAdmin'),
# 	url(r'^$',views.managePatient,name ='managePatient'),
# 	url(r'^$',views.manageClinician,name ='manageClinician'),
# 	url(r'^$',views.medication,name ='medication'),
 ]