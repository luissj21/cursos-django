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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"), #Ruta para llamar a la vista principal
    path('cursos/', views.cursos, name="Cursos"), #Ruta para llamar a la vista cursos
    path('contacto/', views.contacto, name="Contacto"), #Ruta para llamar a la vista contacto
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)