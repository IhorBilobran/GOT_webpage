from django.conf.urls import url, include

urlpatterns = [
	url(r'^paypal/', include('paypal.standard.ipn.urls')),
]