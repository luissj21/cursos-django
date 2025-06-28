from django.contrib import admin
from .models import Curso
# Register your models here.
class AdministrarCurso(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('titulo', 'profesor', 'precio','disponibilidad','duracion')
    search_fields = ('titulo', 'profesor')
    date_hierarchy = 'created'
    list_filter = ('profesor', 'disponibilidad')
admin.site.register(Curso, AdministrarCurso)