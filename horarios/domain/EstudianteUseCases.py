
from horarios.data.database.entities.EstudianteEntity import Estudiante
from horarios.data.repositories.EstudianteRepository import EstudianteRepository

from horarios.domain.model.RespuestaOperacion import RespuestaOperacion

class EstudianteUseCases():
    @staticmethod
    def obtenerTodosLosGruposRelacionadosAEstudianteUseCase(estudianteMatricula) -> list[Estudiante]:
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: list[Estudiante] = EstudianteRepository.obtenerTodosLosGruposRelacionadosAEstudianteDeBD(estudianteMatricula=estudianteMatricula)
        except Estudiante.DoesNotExist as error:
            print("ERROR:obtenerEstudiantesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerEstudiantesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def obtenerEstudiantesPorGrupoUseCase(grupoId) -> list[Estudiante]:
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: list[Estudiante] = EstudianteRepository.obtenerEstudiantesPorGrupoDeBD(grupoId = grupoId)
        except Estudiante.DoesNotExist as error:
            print("ERROR:obtenerEstudiantesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerEstudiantesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearEstudianteUseCase(matricula: str, nombre: str, apellidos:str, grupoId: str):
        """
            Se crea el estudiante y se asigna al grupo
        """
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            EstudianteRepository.crearEstudianteEnBD(matricula = matricula, nombre = nombre, apellidos = apellidos)
            respuesta.mensaje = "Estudiante creado con éxito"
        except Exception as error:
            print("ERROR:crearEstudianteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido registrar el estudiante."
            return respuesta
        
        respuestaAsignacion:RespuestaOperacion = EstudianteUseCases.asignarEstudianteAGrupoUseCase(estudianteMatricula=matricula, grupoId=grupoId)
        if(respuestaAsignacion.error):
            EstudianteUseCases.eliminarEstudianteUseCase(matricula=matricula, grupoId= grupoId)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido registrar el estudiante."
            return respuesta
        respuesta.error = False
        respuesta.mensaje = "Estudiante creado con éxito"
            
        return respuesta
    
    @staticmethod
    def actualizarEstudianteUseCase(matricula: str, nuevoNombre: str, nuevoApellidos: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            EstudianteRepository.actualizarEstudianteEnBD(matricula = matricula, nuevoNombre=nuevoNombre, nuevoApellidos=nuevoApellidos)
            respuesta.mensaje = "Estudiante actualizado con exito"
        except Exception as error:
            print("ERROR:actualizarEstudianteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se han podido actualizar los datos del estudiante."
            
        return respuesta
    
    @staticmethod
    def eliminarEstudianteUseCase(matricula: str, grupoId):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        respuesta = EstudianteUseCases.obtenerTodosLosGruposRelacionadosAEstudianteUseCase(estudianteMatricula=matricula)
        if(respuesta.error):
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se han podido eliminar los datos del estudiante."
        elif(respuesta.contenido.__len__() == 1):
            respuesta.contenido = ''
            try:
                EstudianteRepository.eliminarEstudianteEnBD(matricula)
                respuesta.mensaje = "Estudiante eliminado exitosamente"
            except Exception as error:
                print("ERROR:eliminarEstudianteUseCase: ", error)
                respuesta.error = True
                respuesta.mensaje = "Operación fallida, no se han podido eliminar los datos del estudiante."
        else:
            respuesta = EstudianteUseCases.desasignarEstudianteAGrupoUseCase(estudianteMatricula=matricula, grupoId=grupoId)
            if not respuesta.error:
                respuesta.contenido=''
                respuesta.mensaje = "Estudiante eliminado exitosamente del grupo."
        return respuesta

        
    
    @staticmethod
    def asignarEstudianteAGrupoUseCase( estudianteMatricula: str, grupoId: int):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            EstudianteRepository.asignarEstudianteAGrupoEnBD(estudianteMatricula=estudianteMatricula, grupoId=grupoId)
            respuesta.mensaje = "Estudiante asignado a grupo exitosamente."
        except Exception as error:
            print("ERROR:asignarEstudianteAGrupoEnBD: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido asignar grupo al estudiante."

        return respuesta
    
    @staticmethod
    def desasignarEstudianteAGrupoUseCase( estudianteMatricula: str, grupoId: int):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            EstudianteRepository.desasignarEstudianteAGrupoEnBD(estudianteMatricula=estudianteMatricula, grupoId=grupoId)
            respuesta.mensaje = "Estudiante asignado a grupo exitosamente."
        except Exception as error:
            print("ERROR:desasignarEstudianteAGrupoEnBD: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida, no se ha podido desasignar grupo al estudiante."

        return respuesta
        