"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views #Se importa el modulo views desde la app contenido
from django.conf import settings
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"), #Ruta para llamar a la vista principal
    path('curso/', views.cursos, name="Curso"), #Ruta para llamar a la vista cursos
    path('contacto/', views.contacto, name="Contacto"), #Ruta para llamar a la vista contacto
    path('cursos/',views_cursos.consultas, name="Cursos"),
    path('registrar/', views_cursos.registrarCurso, name="Registrar"),
    path('<int:id>/editar/', views_cursos.editarCurso, name='Editar'),
    path('cursos/<int:id>/eliminar/', views_cursos.eliminarCurso, name='Eliminar'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)