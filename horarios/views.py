from django.shortcuts import render
from horarios.models import *
# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Testing")

def alumnos(request):
    alumnos  = Alumno.objects.all()
    return HttpResponse(alumnos)

def registrarAlumno(request):
    alumnos  = Alumno.objects.all()
    return HttpResponse(alumnos)

def listaAlumnosPorMaestro(request, id_maestro):
    alumnos  = Alumnos_Por_Maestro.objects.filter(maestro = id_maestro)
    return HttpResponse(alumnos)
