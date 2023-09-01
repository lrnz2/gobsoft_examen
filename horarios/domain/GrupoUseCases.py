
from horarios.data.database.entities.GrupoEntity import Grupo
from horarios.data.repositories.GrupoRepository import GrupoRepository

from horarios.domain.model.RespuestaOperacion import RespuestaOperacion

class GrupoUseCases():
    
    @staticmethod
    def obtenerGrupoUseCase(grupoId):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: Grupo = GrupoRepository.obtenerGrupoDeBD(grupoId=grupoId)
        except Grupo.DoesNotExist as error:
            print("ERROR:obtenerGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def obtenerGruposPorDocenteUseCase(docenteMatricula):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: list[Grupo] = GrupoRepository.obtenerGruposPorDocenteDeBD(docenteMatricula=docenteMatricula)
        except Grupo.DoesNotExist as error:
            print("ERROR:obtenerGruposPorDocenteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerGruposPorDocenteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearGrupoUseCase(docenteMatricula: str, grado: str, subgrupo:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            GrupoRepository.crearGrupoEnBD(docenteMatricula = docenteMatricula,  grado = grado, subgrupo = subgrupo)
            respuesta.mensaje = "Grupo creado con exito"
        except Exception as error:
            print("ERROR:crearGruposUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarGrupoUseCase(grupo_id: str, nuevoGrado: str, nuevoSubgrupo: str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            GrupoRepository.actualizarGrupoEnBD(grupo_id = grupo_id,  nuevoGrado = nuevoGrado, nuevoSubgrupo=nuevoSubgrupo)
            respuesta.mensaje = "Grupo actualizado con exito"
        except Exception as error:
            print("ERROR:actualizarGruposUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarGrupoUseCase(grupoId: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            GrupoRepository.eliminarGrupoEnBD(grupoId = grupoId)
            respuesta.mensaje = "Grupo eliminado exitosamente"
        except Exception as error:
            print("ERROR:eliminarGruposUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        