from django.urls import path
from horarios import views

urlpatterns = [
    path("", views.home, name="home"),
    path("alumnos/", views.alumnos, name="alumnos"),
    path("alumnos/registrar", views.registrarAlumno, name="registrarAlumno"),
    path("alumnos/eliminar", views.registrarAlumno, name="eliminarAlumno"),

    path("materias/registrar", views.registrarAlumno, name=""),

    path("maestro/registrar", views.registrarAlumno, name=""),
    path("maestro/actualizar", views.registrarAlumno, name=""),
    
    path("maestro/<int:id_maestro>/alumnos", views.listaAlumnosPorMaestro, name="alumnos_por_maestro"),
    
]