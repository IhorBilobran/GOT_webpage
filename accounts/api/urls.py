from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view()),
    url(r'^posts/$', views.PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)