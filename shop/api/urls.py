from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetail.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>\d+)/$', views.ProductDetail.as_view()),

]
