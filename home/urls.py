"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url, include

from . import views
from .views import Home
#[\w\-]+)
app_name = 'home'
urlpatterns = [
	url(r'^$', Home.as_view(), name='home'),
	url(r'^view_house/(?P<id>\d+)/$', views.view_house,
		name='view_house'),
	url(r'^view_profile/(?P<id>\d+)/$', views.view_profile,
		name='view_profile'),
]
