from django.contrib import admin
from .models import Programa
# Register your models here.

class ProgramaAdmin(admin.ModelAdmin):
	model = Programa
	list_display = ['id_programa','id_criador','criador','titulo']
	# list_filter = []
	# search_fields = []
	save_on_top = True

admin.site.register(Programa, ProgramaAdmin)