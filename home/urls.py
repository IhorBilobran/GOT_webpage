"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url, include

from . import views
#[\w\-]+)
app_name = 'home'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^house-gallery/$', views.house_gallery, name='house_gallery'),
	url(r'^castel-gallery/$', views.castel_gallery, name='castel_gallery'),
	url(r'^view-house/(?P<id>\d+)/$', views.view_house, name='view_house'),
	url(r'^view-profile/(?P<id>\d+)/$', views.view_profile, name='view_profile'),
	url(r'^view-castel/(?P<id>\d+)/$', views.view_castel, name='view_castel'),
]
	