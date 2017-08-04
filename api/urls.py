# coding: utf-8
from django.conf.urls import  url

from rest_framework.urlpatterns import format_suffix_patterns


from programa.views import ProgramaListView, ProgramaView
from selecao.views import SelecaoListView, SelecaoView, ParticipeListView, ParticipeView, ParticipantesView, ParticipantesDeleteView
# from usuario.views import UsuarioViewSet, GroupViewSet

# helper_patterns

urlpatterns = [
    url(r'^programa/$', ProgramaListView.as_view(), name='programa'),
    url(r'^programa/(?P<pk>[0-9]+)/$', ProgramaView.as_view(), name='get_programa'),
    
    url(r'^selecao/$', SelecaoListView.as_view(), name='selecao'),
    url(r'^selecao/(?P<pk>[0-9]+)/$', SelecaoView.as_view(), name='get_selecao'),

    url(r'^selecao/(?P<pk>[0-9]+)/participantes/$', ParticipantesView.as_view(), name='get_participantes'),

    url(r'^participe/$', ParticipeListView.as_view(), name='participe'),
    url(r'^participe/(?P<pk>[0-9]+)/$', ParticipeView.as_view(), name='get_participe'),

    url(r'^selecao/(?P<pk>[0-9]+)/participantes/(?P<pk2>[0-9]+)/$', ParticipantesDeleteView.as_view(), name='delete_participantes'),

    # url(r'^usuario/$', UsuarioViewSet.as_view({'get': 'list'}), name='usuario')
]

# urlpatterns = helper_patterns
urlpatterns = format_suffix_patterns(urlpatterns)
