
from horarios.data.database.entities.DocenteEntity import Docente
from horarios.data.database.entities.GrupoEntity import Grupo


class GrupoDao():

    @staticmethod
    def obtenerGrupo(grupoId:str):
        return Grupo.objects.get(id=grupoId)
    
    @staticmethod
    def obtenerGruposPorDocente(docenteMatricula:str):
        return Grupo.objects.filter(docente = Docente.objects.get(matricula = docenteMatricula))
    
    @staticmethod
    def crearGrupo(docenteMatricula: str, grado: str, subgrupo:str):
        Grupo(docente = Docente.objects.get(matricula = docenteMatricula), grado = grado, subgrupo = subgrupo).save()
    
    @staticmethod
    def actualizarGrupo(grupo_id: str, nuevoGrado: str, nuevoSubgrupo: str):
        Grupo.objects.filter(grupo_id).update(grado = nuevoGrado, subgrupo = nuevoSubgrupo)

    @staticmethod
    def eliminarGrupo(grupoId: str):
        Grupo.objects.get(id = grupoId).delete()
    