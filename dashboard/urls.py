from django.conf.urls import url
from . import views 

urlpatterns = [
	#urls mapping the views of the application come here
	url(r'^$',views.index,name='index'),
]