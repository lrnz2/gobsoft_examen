from django.urls import path
from horarios.ui import views

urlpatterns = [
    path("", views.home, name="home"),
    path("docente/crear/", views.crearDocente, name = "docente_crear"),
    path("docente/actualizar/", views.actualizarDocente, name = "docente_actualizar"),
    path("docente/eliminar/", views.eliminarDocente, name = "docente_eliminar"),
    path("docente/<str:docente_matricula>/", views.detalleDocente, name="docente_detalle"),
    path("docente/<str:docente_matricula>/<str:grupo_seleccionado_id>/", views.detalleDocente, name="docente_detalle"),

    path("docente/grupo/crear", views.crearGrupo, name="crear_grupo"),
    path("docente/grupo/eliminar", views.eliminarGrupo, name="eliminar_grupo"),

    path("docente/clase/crear", views.crearHorarioClase, name="clase_crear"),
    path("docente/clase/actualizar", views.actualizarHorarioClase, name="actualizar_horario_clase"),
    path("docente/clase/eliminar", views.eliminarHorarioClase, name="eliminar_horario_clase"),

    path("docente/estudiante/crear", views.crearEstudiante, name="crear_estudiante"),
    path("docente/estudiante/actualizar", views.actualizarEstudiante, name="actualizar_estudiante"),
    path("docente/estudiante/eliminar", views.eliminarEstudiante, name="eliminar_estudiante"),
    
]