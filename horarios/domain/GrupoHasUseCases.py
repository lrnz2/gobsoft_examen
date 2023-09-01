
from horarios.data.repositories.GrupoHasRepository import GrupoHasRepository
from horarios.domain.model.RespuestaOperacion import RespuestaOperacion
from horarios.data.database.entities.GrupoHasClaseEntity import GrupoHasClase

class GrupoHasUseCases():

    @staticmethod
    def asignarClaseAGrupoUseCase(grupo, clase):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            GrupoHasRepository.asignarClaseAGrupoEnBD(grupo=grupo, clase=clase)
            respuesta.mensaje = "Clase asignada a grupo axitosamente."
        except Exception as error:
            print("ERROR:asignarClaseAGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido asignar clase a grupo"

        return respuesta
    
    @staticmethod
    def obtenerClasesDeGrupoUseCase(grupoId):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido = GrupoHasRepository.obtenerClasesDeGrupoDeBD(grupoId=grupoId)
        except GrupoHasClase.DoesNotExist as error:
            print("ERROR:obtenerClasesDeGrupoUseCase: ", error)
            respuesta.contenido = []
            respuesta.mensaje = "No hay clases registradas para este grupo"
        except Exception as error:
            print("ERROR:obtenerClasesDeGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido obtener clases"
            respuesta.contenido = []

        return respuesta
    

    @staticmethod
    def asignarEstudianteAGrupoUseCase(estudianteMatricula: str, grupoId: int):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            GrupoHasRepository.asignarClaseAGrupoEnBD(estudianteMatricula = estudianteMatricula, grupoId=grupoId)
            respuesta.mensaje = "Estudiante asignado a Grupo exitosamente"
        except Exception as error:
            print("ERROR:asignarEstudianteAGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido asignar estudiante a grupo"

        return respuesta
    

    @staticmethod
    def desasignarEstudianteAGrupoUseCase(estudianteMatricula: str, grupoId: int):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            GrupoHasRepository.desasignarClaseAGrupoEnBD(estudianteMatricula = estudianteMatricula, grupoId=grupoId)
            respuesta.mensaje = "Estudiante desasignado a Grupo exitosamente"
        except Exception as error:
            print("ERROR:desasignarEstudianteAGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido desasignar estudiante a grupo"

        return respuesta

    @staticmethod
    def obtenerEstudiantesDeGrupo(grupoId):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido = GrupoHasRepository.obtenerEstudiantesDeGrupoDeBD(grupoId=grupoId)
        except GrupoHasClase.DoesNotExist as error:
            print("ERROR:obtenerClasesDeGrupoUseCase: ", error)
            respuesta.contenido = []
            respuesta.mensaje = "No hay clases registradas para este grupo"
        except Exception as error:
            print("ERROR:obtenerClasesDeGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido obtener clases"
            respuesta.contenido = []

        return respuesta
    

    @staticmethod
    def obtenerEstudiantesNoPertenezcanAGrupoUseCase(grupoId):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido = GrupoHasRepository.obtenerEstudiantesNoPertenezcanAGrupoDeBD(grupoId=grupoId)
        except GrupoHasClase.DoesNotExist as error:
            print("ERROR:obtenerEstudiantesNoPertenezcanAGrupoUseCase: ", error)
            respuesta.contenido = []
            respuesta.mensaje = "No hay clases registradas"
        except Exception as error:
            print("ERROR:obtenerEstudiantesNoPertenezcanAGrupoUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido obtener clases"
            respuesta.contenido = []

        return respuesta
