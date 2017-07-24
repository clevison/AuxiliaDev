# coding: utf-8
from django.conf.urls import  url
from programa.views import ProgramaListView, ProgramaView


helper_patterns = [
    url(r'^programa/$', ProgramaListView.as_view(), name='programa'),
    url(r'^programa/(?P<pk>[0-9]+)/$', ProgramaView.as_view(), name='get_programa')
]

urlpatterns = helper_patterns