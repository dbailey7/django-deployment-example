from django.conf.urls import url;
from templatesapp import views;

#Template Tagging for relative url template usage ...
app_name = 'templatesapp';

urlpatterns = [
    # for relative templete tagging usage ...
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
];
