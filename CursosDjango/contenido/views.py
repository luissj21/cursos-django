from django.shortcuts import render, HttpResponse

#Menu para acceder a las demas paginas del proyecto desde la pagina principal


# Create your views here.
#Aquí se define la vista principal la cual mostrará la pagina inicial del proyecto y en donde se encuentra el menú para acceder a las demas paginas.  
def principal(request):
    return render(request, "contenido/principal.html")

#Aqui se define la vista de cursos 
def cursos(request):
    return render(request, "contenido/cursos.html") #Retorna el contenido de la pagina cursos

#Se define la vista contacto
def contacto(request):
    return render(request, "contenido/contacto.html") #Retorna el contenido de la pagina contacto
