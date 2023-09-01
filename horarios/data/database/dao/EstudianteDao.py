
from horarios.data.database.entities.EstudianteEntity import Estudiante
from horarios.data.database.entities.GrupoEntity import Grupo
from horarios.data.database.entities.GrupoHasEstudianteEntity import GrupoHasEstudiante
from horarios.data.database.entities.DocenteEntity import Docente

class EstudianteDao():

    @staticmethod
    def obtenerEstudiantesPorGrupo(grupoId):
        return GrupoHasEstudiante.objects.filter(grupo_id = grupoId).only('estudiante')
    
    @staticmethod
    def obtenerTodosLosGruposRelacionadosAEstudiante(estudianteMatricula):
        return GrupoHasEstudiante.objects.filter(estudiante= Estudiante.objects.get(matricula=estudianteMatricula)).only('estudiante')
    
    @staticmethod
    def crearEstudiante(matricula: str, nombre: str, apellidos:str):
        Estudiante(matricula = matricula, nombre = nombre, apellidos = apellidos).save()
    
    @staticmethod
    def actualizarEstudiante(matricula: str, nuevoNombre: str, nuevoApellidos: str):
        Estudiante.objects.filter(matricula = matricula).update(nombre =nuevoNombre, apellidos = nuevoApellidos)

    @staticmethod
    def eliminarEstudiante(matricula: str):
        Estudiante.objects.filter(matricula = matricula).delete()
    
    @staticmethod
    def asignarEstudianteAGrupo(estudianteMatricula: str, grupoId: int):
        GrupoHasEstudiante(
            estudiante = Estudiante.objects.get(matricula = estudianteMatricula), 
            grupo = Grupo.objects.get(id = grupoId)
            ).save()
        
    @staticmethod
    def desasignarEstudianteAGrupo(estudianteMatricula: str, grupoId: int):
        GrupoHasEstudiante.objects.filter(
            estudiante = Estudiante.objects.get(matricula = estudianteMatricula), 
            grupo = Grupo.objects.get(id = grupoId)
            ).delete()
    
    
    
    
    