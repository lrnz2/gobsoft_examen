
from horarios.data.database.entities.DocenteEntity import Docente
from horarios.data.repositories.DocenteRepository import DocenteRepository

from horarios.domain.model.RespuestaOperacion import RespuestaOperacion

class DocenteUseCases():
    
    @staticmethod
    def obtenerDocentesUseCase() -> list[Docente]:
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: list[Docente] = DocenteRepository.obtenerDocentesDeBD()
        except Docente.DoesNotExist as error:
            print("ERROR:obtenerDocentesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerDocentesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def obtenerDocenteUseCase(matricula:str) -> Docente:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Docente = DocenteRepository.obtenerDocenteDeBD(matricula=matricula)
        except Docente.DoesNotExist as error:
            print("ERROR:obtenerDocentesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerDocentesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearDocenteUseCase(matricula: str, nombre: str, apellidos:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            DocenteRepository.crearDocenteEnBD(matricula = matricula, nombre = nombre, apellidos = apellidos)
            respuesta.mensaje = "Docente creado con exito"
        except Exception as error:
            print("ERROR:crearDocenteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarDocenteUseCase(matricula: str, nuevoNombre: str, nuevoApellidos: str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            DocenteRepository.actualizarDocenteEnBD(matricula = matricula, nuevoNombre=nuevoNombre, nuevoApellidos=nuevoApellidos)
            respuesta.mensaje = "Docente actualizado con exito"
        except Exception as error:
            print("ERROR:actualizarDocenteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarDocenteUseCase(matricula: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            DocenteRepository.eliminarDocenteEnBD(matricula)
            respuesta.mensaje = "Docente eliminado exitosamente"
        except Exception as error:
            print("ERROR:eliminarDocenteUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        