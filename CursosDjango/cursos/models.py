from django.db import models

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo del Curso")
    descripcion = models.TextField(verbose_name="Descripción del Curso")
    profesor = models.CharField(max_length=50, verbose_name="Nombre del Profesor")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Foto del Curso")
    disponibilidad = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio del Curso")
    duracion = models.DurationField(verbose_name="Duración del Curso")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['created']