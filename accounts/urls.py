from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout

from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^view-profile/$', views.view_profile, name='view_profile'),
	url(r'^view-profile/(?P<id>\d+)/$', views.view_profile,
		name='view_profile'),
	url(r'^change-profile/$', views.change_profile, name='change_profile'),
	url(r'^api/', include('accounts.api.urls')),
	# define urls for reseting password
    url('^', include('django.contrib.auth.urls')),

]
