
from horarios.data.database.entities.ClaseEntity import Clase

class ClaseDao():


    @staticmethod
    def obtenerContadorMateriaEnClases(materiaClave: str, docenteMatricula:str):
        return Clase.objects.filter(materia_clave = materiaClave, docente_matricula = docenteMatricula).count()

    @staticmethod
    def obtenerClase(claseId):
        return Clase.objects.get(id = claseId)
    
    @staticmethod
    def obtenerClase(docente, materia, hora, dia):
        return Clase.objects.get(docente = docente, materia = materia, hora = hora, dia = dia)
    
    @staticmethod
    def obtenerClasesPorDocenteYGrupo(docenteMatricula:str, grupo_id):
        return Clase.objects.filter(docenteMatricula = docenteMatricula)
    
    @staticmethod
    def crearClase(materia, docente, hora:str, dia:str):
        Clase(materia = materia, docente = docente, hora = hora, dia = dia).save()
    
    @staticmethod
    def actualizarClase(claseId: str, materia):
        Clase.objects.filter(id = claseId).update(materia = materia)

    @staticmethod
    def eliminarClase(id: str):
        Clase.objects.get(id = id).delete()
    