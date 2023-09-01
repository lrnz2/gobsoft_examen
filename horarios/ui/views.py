from django.shortcuts import render
from horarios.data.database.entities.ClaseEntity import *
from horarios.data.database.entities.DocenteEntity import *
from horarios.data.database.entities.EstudianteEntity import *
from horarios.data.database.entities.GrupoEntity import *
from horarios.data.database.entities.MateriaEntity import *
from horarios.data.database.entities.GrupoHasClaseEntity import *
from horarios.data.database.entities.GrupoHasEstudianteEntity import *
from horarios.core.utils.Reverse import Reverse as custom_reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from django.views.decorators.http import require_http_methods

from django.shortcuts import redirect
from django.db.models import Q

from ..domain.EstudianteUseCases import EstudianteUseCases
from ..domain.DocenteUseCases import DocenteUseCases
from ..domain.model.RespuestaOperacion import RespuestaOperacion
from ..domain.GrupoUseCases import GrupoUseCases
from ..domain.ClaseUseCases import ClaseUseCases
from ..domain.GrupoHasUseCases import GrupoHasUseCases


from django.utils.http import urlencode

from dataclasses import asdict

require_http_methods(["GET"])
def home(request):

    mensaje = request.GET.get('mensaje')
    error = request.GET.get('error') == 'True'

    respuesta: RespuestaOperacion = DocenteUseCases.obtenerDocentesUseCase()
    
    context = {
        "lista_docentes":respuesta.contenido,
        "mensaje": mensaje,
        "error": error
    }

    return render(request, "horarios/index.html", context)

require_http_methods(["POST"])
def crearDocente(request):
    matricula = request.POST['matricula']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']

    respuesta = DocenteUseCases.crearDocenteUseCase(matricula=matricula, nombre=nombre, apellidos = apellidos)
    url_encoded = custom_reverse.reverse('home',asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def actualizarDocente(request):
    matricula = request.POST['matricula']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']

    respuesta = DocenteUseCases.actualizarDocenteUseCase(matricula=matricula, nuevoNombre= nombre, nuevoApellidos=apellidos)
    url_encoded = custom_reverse.reverse('home',asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

require_http_methods(["POST"])
def eliminarDocente(request):
    matricula = request.POST["matricula"]

    respuesta = DocenteUseCases.eliminarDocenteUseCase(matricula=matricula)
    url_encoded = custom_reverse.reverse('home',asdict(respuesta))
    return HttpResponseRedirect(url_encoded)

def detalleDocente(request, docente_matricula, grupo_seleccionado_id=None):
    
    gruposPorDocente = GrupoUseCases.obtenerGruposPorDocenteUseCase(docenteMatricula=docente_matricula).contenido
    
    # Obtenemos los datos del grupo seleccionado de select grupo
    grupoSeleccionado = None
    if(grupo_seleccionado_id == None):
        grupo_seleccionado_id = request.GET.get('grupo-seleccionado-id')
    respuestaOperacionObtenerDatosDeGrupoSeleccionado = GrupoUseCases.obtenerGrupoUseCase(grupoId=grupo_seleccionado_id)
    if(not respuestaOperacionObtenerDatosDeGrupoSeleccionado.error):
        grupoSeleccionado = respuestaOperacionObtenerDatosDeGrupoSeleccionado.contenido

    # Obtenemos las clases y alumnos si se pudo obtener los datos del grupo seleccionado
    clasesPorGrupo = []
    if(not respuestaOperacionObtenerDatosDeGrupoSeleccionado.error):
        respuesaOperacionObtenerClasesPorGrupo = GrupoHasUseCases.obtenerClasesDeGrupoUseCase(grupo_seleccionado_id)
        if(not respuesaOperacionObtenerClasesPorGrupo.error):
            clasesPorGrupo = respuesaOperacionObtenerClasesPorGrupo.contenido
    
    # Obtenemos los estudiantes por grupo seleccionado
    estudiantesPorGrupo = []
    respuesaOperacionObtenerEstudiantesPorGrupo = GrupoHasUseCases.obtenerEstudiantesDeGrupo(grupoId=grupo_seleccionado_id)
    if(not respuesaOperacionObtenerEstudiantesPorGrupo.error):
        estudiantesPorGrupo = respuesaOperacionObtenerEstudiantesPorGrupo.contenido

    # Obtenemos estudiantes no registrados en el grupo actual
    estudiantesNoRegistradoEnGrupoActual =[]
    respuesaOperacionObtenerEstudiantesNoEnGrupo = GrupoHasUseCases.obtenerEstudiantesNoPertenezcanAGrupoUseCase(grupo_seleccionado_id)
    if(not respuesaOperacionObtenerEstudiantesNoEnGrupo.error):
        estudiantesNoRegistradoEnGrupoActual = respuesaOperacionObtenerEstudiantesNoEnGrupo.contenido
        
    horario_obj = {
        "7:30 - 8:30" : [[],[],[],[],[]],
        "8:30 - 9:30" : [[],[],[],[],[]],
        "9:30 - 10:30" : [[],[],[],[],[]],
        "11:00 - 12:00" : [[],[],[],[],[]],
        "12:00 - 13:00" : [[],[],[],[],[]],
        "13:00 - 14:00" : [[],[],[],[],[]],
        "14:00 - 15:00" : [[],[],[],[],[]],
        "15:00 - 16:00" : [[],[],[],[],[]],
    }
    
    for clase in clasesPorGrupo:
        if clase.dia == "Lunes":
            horario_obj[clase.hora][0] = clase
        elif clase.dia == "Martes":
            horario_obj[clase.hora][1] = clase
        elif clase.dia == "Miércoles":
            horario_obj[clase.hora][2] = clase
        elif clase.dia == "Jueves":
            horario_obj[clase.hora][3] = clase
        elif clase.dia == "Viernes":
            horario_obj[clase.hora][4] = clase

    final_arr = []
    for i in horario_obj:
        final_arr.append([i] + horario_obj[i])

    context = {
        "docente_matricula": docente_matricula,
        "docente_grupos": gruposPorDocente,
        "grupo_seleccionado": grupoSeleccionado,
        "horario_clases":final_arr,
        "clases_por_grupo": clasesPorGrupo,
        "estudiantes_por_grupo":estudiantesPorGrupo,
        "estudiantes_no_en_grupo": estudiantesNoRegistradoEnGrupoActual
    }

    return render(request, "horarios/detalle_docente.html", context)
    
def crearGrupo(request):
    docenteMatricula = request.POST["docente-matricula"]
    grupoGrado = request.POST['grupo-grado']
    grupoSubgrupo = request.POST['grupo-subgrupo']

    respuesta = GrupoUseCases.crearGrupoUseCase(docenteMatricula=docenteMatricula, grado=grupoGrado, subgrupo= grupoSubgrupo)
    url_encoded = custom_reverse.reverse('docente_detalle', kwargs={'docente_matricula':docenteMatricula},dict = asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

def eliminarGrupo(request):
    docenteMatricula = request.POST["docente-matricula"]
    grupoId = request.POST["grupo-id"]
    
    respuesta = GrupoUseCases.eliminarGrupoUseCase(grupoId = grupoId)
    
    url_encoded = custom_reverse.reverse('docente_detalle', kwargs={'docente_matricula':docenteMatricula}, dict = asdict(respuesta))
    return HttpResponseRedirect(url_encoded)

def crearHorarioClase(request):
    # Materia, Docente, hora, dia
    docenteMatricula = request.POST["docente-matricula"]
    materiaClave = request.POST['materia'] # valor de select materia
    claseHora = request.POST['hora']
    claseDia = request.POST['dia']
    grupoId = request.POST['grupo-id']

    nuevaMateriaNombre = ""
    nuevaMateriaClave = ""
    nuevaMateriaCreditos = ""

    if(materiaClave=="crear-nueva-materia"):
        nuevaMateriaNombre = request.POST['nueva-materia-nombre']
        nuevaMateriaClave = request.POST['nueva-materia-clave']
        nuevaMateriaCreditos = request.POST['nueva-materia-creditos']

    respuesta = ClaseUseCases.crearClaseUseCase(
            materiaClave=materiaClave,
            docenteMatricula=docenteMatricula,
            grupoId=grupoId,
            hora=claseHora,
            dia=claseDia,
            materiaNuevaClave = nuevaMateriaClave,
            materiaNombre=nuevaMateriaNombre,
            materiaCreditos=nuevaMateriaCreditos
        )
    kwargs={
        'docente_matricula': docenteMatricula,
        'grupo_seleccionado_id': grupoId,
    }
    url_encoded = custom_reverse.reverse(path = 'docente_detalle', kwargs=kwargs, dict= asdict(respuesta))
    return HttpResponseRedirect(url_encoded)

def actualizarHorarioClase(request):
    
    docenteMatricula = request.POST["docente-matricula"]
    grupoId = request.POST['grupo-id']
    materiaClaveNueva = request.POST['materia-clave'] # valor de select materia
    materiaClaveActual = request.POST['materia-clave-actual']
    claseId = request.POST['clase-id']


    nuevaMateriaNombre = ''
    nuevaMateriaClave = ''
    nuevaMateriaCreditos = ''

    if(materiaClaveNueva=="crear-nueva-materia"):
        # se crea materia
        nuevaMateriaNombre = request.POST['nueva-materia-nombre']
        nuevaMateriaClave = request.POST['nueva-materia-clave']
        nuevaMateriaCreditos = request.POST['nueva-materia-creditos']

    respuesta:RespuestaOperacion = ClaseUseCases.actualizarClaseUseCase(
        claseId=claseId,
        materiaClaveActual=materiaClaveActual,
        materiaClaveNueva = materiaClaveNueva,
        nuevaMateriaClave=nuevaMateriaClave,
        nuevaMateriaNombre=nuevaMateriaNombre,
        nuevaMateriaCreditos=nuevaMateriaCreditos
        )
    kwargs={
        'docente_matricula': docenteMatricula,
        'grupo_seleccionado_id': grupoId,
    }
    url_encoded = custom_reverse.reverse(path = 'docente_detalle', kwargs=kwargs, dict= asdict(respuesta))
    return HttpResponseRedirect(url_encoded)
    

def eliminarHorarioClase(request):
    docenteMatricula = request.POST['docente-matricula']
    grupoId = request.POST['grupo-id']
    claseId = request.POST['clase-id']
    materiaClave = request.POST['materia-clave']
    
    respuesta = ClaseUseCases.eliminarClaseUseCase(id=claseId,materiaClave=materiaClave, docenteMatricula=docenteMatricula)
    
    kwargs={
        'docente_matricula': docenteMatricula,
        'grupo_seleccionado_id': grupoId,
        }
    url_encoded = custom_reverse.reverse(path = 'docente_detalle', kwargs=kwargs, dict= asdict(respuesta))
    return HttpResponseRedirect(url_encoded)

def crearEstudiante(request):
    estudianteMatricula = request.POST['matricula']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    grupoId = request.POST['grupo-id']

    docenteMatricula = request.POST['docente-matricula']

    respuesta = EstudianteUseCases.crearEstudianteUseCase(matricula=estudianteMatricula, nombre=nombre, apellidos = apellidos, grupoId=grupoId)
    
    kwargs={
        'docente_matricula': docenteMatricula,
        'grupo_seleccionado_id': grupoId,
        }
    
    url_encoded = custom_reverse.reverse(path = 'docente_detalle', kwargs=kwargs, dict= asdict(respuesta))

    return HttpResponseRedirect(url_encoded)

def actualizarEstudiante(request):
       
    docenteMatricula = request.POST['docente-matricula']
    grupoId = request.POST['grupo-id']

    estudianteMatricula = request.POST['matricula']
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']

    respuesta = EstudianteUseCases.actualizarEstudianteUseCase(matricula=estudianteMatricula, nuevoNombre=nombre, nuevoApellidos=apellidos)
    kwargs = {
        'docente_matricula': docenteMatricula,
        'grupo_seleccionado_id': grupoId,
    }
    url_encoded = custom_reverse.reverse(path = 'docente_detalle', kwargs=kwargs, dict= asdict(respuesta))
    return HttpResponseRedirect(url_encoded)

def eliminarEstudiante(request):
       
    docenteMatricula = request.POST['docente-matricula']
    estudianteMatricula = request.POST['estudiante-matricula']
    grupoId = request.POST['grupo-id']

    respuesta = EstudianteUseCases.eliminarEstudianteUseCase(matricula=estudianteMatricula, grupoId = grupoId)
    kwargs={
        'docente_matricula': docenteMatricula,
        'grupo_seleccionado_id': grupoId,
    }
    url_encoded = custom_reverse.reverse(path = 'docente_detalle', kwargs=kwargs, dict= asdict(respuesta))
    return HttpResponseRedirect(url_encoded)



"""
TAREAS:
- eliminar estudiante si ya no esta registrado en algun grupo
- funcion de eliminar grupo

"""
