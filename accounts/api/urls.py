from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
    url(r'^profiles/$', views.ProfileList.as_view()),
    url(r'^profiles/(?P<pk>\d+)/$', views.ProfileDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
