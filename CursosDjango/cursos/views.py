from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm
from django.shortcuts import get_object_or_404
# Create your views here.

def consultas(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos.html',{'cursos':cursos})
            
def registrarCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cursos') 
    else:
        form = CursoForm()  

    return render(request, 'cursos/registrarCurso.html', {'form': form})

def editarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('Cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editarCurso.html',{'form':form})


def eliminarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('Cursos') 