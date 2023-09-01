
from horarios.data.database.dao.GrupoHasDao import GrupoHasDao

class GrupoHasRepository():

    @staticmethod
    def asignarClaseAGrupoEnBD(grupo, clase):
        GrupoHasDao.asignarClaseAGrupo(grupo = grupo, clase = clase)
    
    @staticmethod
    def obtenerClasesDeGrupoDeBD(grupoId):
        return GrupoHasDao.obtenerClasesDeGrupo(grupoId=grupoId)
    
    @staticmethod
    def asignarEstudianteAGrupoEnBD(estudianteMatricula: str, grupoId: int):
        GrupoHasDao.asignarEstudianteAGrupo(estudianteMatricula=estudianteMatricula, grupoId=grupoId)
        
    @staticmethod
    def desasignarEstudianteAGrupoEnBD(estudianteMatricula: str, grupoId: int):
        GrupoHasDao.desasignarEstudianteAGrupo(estudianteMatricula=estudianteMatricula, grupoId=grupoId)
    
    @staticmethod
    def obtenerEstudiantesDeGrupoDeBD(grupoId):
        response = GrupoHasDao.obtenerEstudiantesDeGrupo(grupoId=grupoId)
        return response
    
    @staticmethod
    def obtenerEstudiantesNoPertenezcanAGrupoDeBD(grupoId):
        response = GrupoHasDao.obtenerEstudiantesDeGrupo(grupoId=grupoId)
        return response
    
    