# coding: utf-8
from django.conf.urls import  url

from rest_framework.urlpatterns import format_suffix_patterns


from programa.views import ProgramaListView, ProgramaView
from selecao.views import SelecaoListView, SelecaoView
# from usuario.views import UsuarioViewSet, GroupViewSet

# helper_patterns

urlpatterns = [
    url(r'^programa/$', ProgramaListView.as_view(), name='programa'),
    url(r'^programa/(?P<pk>[0-9]+)/$', ProgramaView.as_view(), name='get_programa'),
    
    url(r'^selecao/$', SelecaoListView.as_view(), name='selecao'),
    url(r'^selecao/(?P<pk>[0-9]+)/$', SelecaoView.as_view(), name='get_selecao'),

    # url(r'^usuario/$', UsuarioViewSet.as_view({'get': 'list'}), name='usuario')
]

# urlpatterns = helper_patterns
urlpatterns = format_suffix_patterns(urlpatterns)
