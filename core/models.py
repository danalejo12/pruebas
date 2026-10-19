from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Aprendiz(models.Model):

    documento = models.CharField(max_length= 15, unique= True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    programa = models.ForeignKey('Programa', on_delete= models.CASCADE, null= True, blank=True, related_name= "aprendices") # models.PROTECT 
    competencia = models.ManyToManyField('Competencia',blank=True)
    def __str__(self):
        return f" Documento: {self.documento} - Nombre: {self.nombre} - Apellido: {self.apellido} - Correo: {self.correo}"


class   Programa(models.Model):

    grupo = models.CharField(max_length= 15, unique= True)
    nombre = models.CharField(max_length=15)
    nivel = models.CharField(max_length=15)
    sede = models.CharField(max_length=25)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f" Grupo: {self.grupo} - Nombre: {self.nombre} - Nivel Academico: {self.nivel} - Sede: {self.sede} - Fecha de inicio: {self.fecha_inicio} - Fecha en la cual termina el programa: {self.fecha_fin}"

class   Competencia(models.Model):

    codigo = models.CharField(max_length= 15, unique= True)
    nombre = models.CharField(max_length=15)
    raps = models.CharField(max_length=15)
    descripcion = models.CharField(max_length= 250)
               

    def __str__(self):
        return f" {self.codigo} -{self.nombre} -  {self.raps} -  {self.descripcion}"