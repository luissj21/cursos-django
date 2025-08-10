from django.contrib import admin
from .models import Curso
from .models import Actividad
# Register your models here.
class AdministrarCurso(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('titulo', 'profesor', 'precio','disponibilidad','duracion')
    search_fields = ('titulo', 'profesor')
    date_hierarchy = 'created'
    list_filter = ('profesor', 'disponibilidad')
admin.site.register(Curso, AdministrarCurso)

class AdministrarActividades(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(Actividad, AdministrarActividades)