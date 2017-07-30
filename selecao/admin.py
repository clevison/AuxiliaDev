from django.contrib import admin
from .models import Selecao

# Register your models here.
class SelecaoAdmin(admin.ModelAdmin):
	model = Selecao
	list_display = ['idSelecao','idPrograma','nome', 'inicio', 'fim']
	list_filter = ['inicio', 'fim']
	search_fields = ['nome']
	save_on_top = True

admin.site.register(Selecao, SelecaoAdmin)