from django.contrib import admin
from .models import Selecao, Participe

# Register your models here.
class SelecaoAdmin(admin.ModelAdmin):
	model = Selecao
	list_display = ['idSelecao','idCriador','idPrograma','nome', 'inicio', 'fim','vagas']
	# list_filter = ['inicio', 'fim']
	search_fields = ['nome']
	save_on_top = True
	# verbose_name_plural = "Selecao"

class ParticipanteAdmin(admin.ModelAdmin):
	model = Participe
	list_display = ['id','idUsuario']
	# list_filter = ['inicio', 'fim']
	# search_fields = ['nome']
	save_on_top = True
	# verbose_name_plural = "Selecao"
	
admin.site.register(Selecao, SelecaoAdmin)
admin.site.register(Participe, ParticipanteAdmin)