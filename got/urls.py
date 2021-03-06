"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^cart/', include('cart.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('home.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
