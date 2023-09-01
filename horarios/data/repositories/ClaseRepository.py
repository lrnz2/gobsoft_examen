from horarios.data.database.dao.ClaseDao import ClaseDao
from horarios.data.database.entities.ClaseEntity import Clase


class ClaseRepository():

    @staticmethod
    def obtenerContadorMateriaEnClasesDeBD(materiaClave: str, docenteMatricula:str):
        response:int = ClaseDao.obtenerContadorMateriaEnClases(materiaClave=materiaClave,docenteMatricula=docenteMatricula)
        return response

    @staticmethod
    def obtenerClaseDeBD(claseId):
        response:Clase = ClaseDao.obtenerClase(claseId=claseId)
        return response
    
    @staticmethod
    def obtenerClaseDeBD(materia, docente, hora: str, dia:str):
        response:Clase = ClaseDao.obtenerClase(materia=materia, docente=docente, hora=hora, dia=dia)
        return response
    
    @staticmethod
    def obtenerClasesDeBD():
        response:list[Clase] = ClaseDao.obtenerClases()
        return response
    
    @staticmethod
    def crearClaseEnBD(materia, docente, hora: str, dia:str):
        ClaseDao.crearClase(materia = materia, docente = docente, hora = hora, dia = dia)
    
    @staticmethod
    def actualizarClaseEnBD(claseId: str, materia):
        ClaseDao.actualizarClase(claseId = claseId, materia=materia)
    
    @staticmethod
    def eliminarClaseEnBD(id: str):
        ClaseDao.eliminarClase(id)