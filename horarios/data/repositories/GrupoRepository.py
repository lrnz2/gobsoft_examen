from horarios.data.database.dao.GrupoDao import GrupoDao
from horarios.data.database.entities.GrupoEntity import Grupo


class GrupoRepository():
    
    @staticmethod
    def obtenerGrupoDeBD(grupoId:str):
        response:Grupo = GrupoDao.obtenerGrupo(grupoId=grupoId)
        return response
    
    @staticmethod
    def obtenerGruposPorDocenteDeBD(docenteMatricula:str):
        response:list[Grupo] = GrupoDao.obtenerGruposPorDocente(docenteMatricula = docenteMatricula)
        return response
    
    @staticmethod
    def crearGrupoEnBD(docenteMatricula: str, grado: str, subgrupo:str):
        GrupoDao.crearGrupo(docenteMatricula = docenteMatricula,  grado = grado, subgrupo = subgrupo)
    
    @staticmethod
    def actualizarGrupoEnBD(grupo_id: str, nuevpGrado: str, nuevoSubgrupo:str):
        GrupoDao.actualizarGrupo(grupo_id = grupo_id,  nuevoGrado = nuevpGrado, nuevoSubgrupo=nuevoSubgrupo)
    
    @staticmethod
    def eliminarGrupoEnBD(grupoId: str):
        GrupoDao.eliminarGrupo(grupoId=grupoId)