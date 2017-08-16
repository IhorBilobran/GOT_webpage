from django.conf.urls import url, include

from . import views

app_name = 'shop'
urlpatterns = [
	url(r'^view-categories/$', views.view_categories, name='view_categories'),
	url(r'^view-products/$', views.view_products, name='view_products'),
	url(r'^view-category/(?P<id>\d+)/$', views.view_category,
		name='view_category'),
	url(r'^api/', include('shop.api.urls')),
]
