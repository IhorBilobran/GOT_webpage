from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}, 
		name='login'),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, 
		name='logout'),

	url(r'^register/$', views.register, name='register'),	
	url(r'^create-profile/$', views.create_profile, name='create_profile'),
	url(r'^view-profile/$', views.view_profile, name='view_profile'),
	url(r'^view-profile/(?P<id>\d+)/$', views.view_profile, 
		name='view_profile'),
] 