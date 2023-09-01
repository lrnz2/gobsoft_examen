
from horarios.data.database.entities.GrupoHasClaseEntity import GrupoHasClase
from horarios.data.database.entities.GrupoHasEstudianteEntity import GrupoHasEstudiante
from horarios.data.database.entities.ClaseEntity import Clase
from horarios.data.database.entities.EstudianteEntity import Estudiante
from horarios.data.database.entities.EstudianteEntity import Estudiante

class GrupoHasDao():

    @staticmethod
    def asignarClaseAGrupo(grupo, clase):
        GrupoHasClase(grupo = grupo, clase = clase).save()
    
    @staticmethod
    def obtenerClasesDeGrupo(grupoId):
        clases_ids = GrupoHasClase.objects.filter(grupo_id = grupoId).values_list('clase', flat=True)
        clases = Clase.objects.filter(pk__in=clases_ids)
        return clases    
    
    @staticmethod
    def asignarEstudianteAGrupo(estudianteMatricula: str, grupoId: int):
        GrupoHasEstudiante(
            estudiante_matricula = estudianteMatricula, 
            grupo_id = grupoId
            ).save()
        
    @staticmethod
    def desasignarEstudianteAGrupo(estudianteMatricula: str, grupoId: int):
        GrupoHasEstudiante.objects.filter(
            estudiante_matricula = estudianteMatricula, 
            grupo_id = grupoId
            ).delete()
    
    @staticmethod
    def obtenerEstudiantesDeGrupo(grupoId):
        estudiantes_ids = GrupoHasEstudiante.objects.filter(grupo_id = grupoId).values_list('estudiante', flat=True)
        estudiantes = Estudiante.objects.filter(pk__in=estudiantes_ids)
        return estudiantes 
    
    @staticmethod
    def obtenerEstudiantesNoPertenezcanAGrupo(grupoId):
        response: list[Estudiante] = GrupoHasEstudiante.objects.exclude(grupo_id = grupoId).only('estudiante')
        return response
        
