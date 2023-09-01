
from horarios.data.database.entities.MateriaEntity import Materia
from horarios.data.repositories.MateriaRepository import MateriaRepository

from horarios.domain.model.RespuestaOperacion import RespuestaOperacion

class MateriaUseCases():
    
    @staticmethod
    def obtenerMateriaContador(clave:str) -> Materia:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Materia = MateriaRepository.obtenerMateriaDeBD(clave = clave)
        except Materia.DoesNotExist as error:
            print("ERROR:obtenerMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
        except Exception as error:
            print("ERROR:obtenerMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            
        return respuesta
    
    @staticmethod
    def obtenerMateriaUseCase(clave:str) -> Materia:
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            respuesta.contenido: Materia = MateriaRepository.obtenerMateriaDeBD(clave = clave)
        except Materia.DoesNotExist as error:
            print("ERROR:obtenerMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
        except Exception as error:
            print("ERROR:obtenerMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            
        return respuesta
    
    @staticmethod
    def obtenerMateriasMateriasPorDocenteUseCase() -> list[Materia]:
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: list[Materia] = MateriaRepository.obtenerMateriasPorDocenteDeBD()
        except Materia.DoesNotExist as error:
            print("ERROR:obtenerMateriasUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
            respuesta.contenido = []
        except Exception as error:
            print("ERROR:obtenerMateriasUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
            respuesta.contenido = []

        return respuesta
    
    @staticmethod
    def crearMateriaUseCase(clave: str, nombre: str, creditos:str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            MateriaRepository.crearMateriaEnBD(clave = clave, nombre = nombre, creditos = creditos)
            respuesta.mensaje = "Materia creada con éxito"
        except Exception as error:
            print("ERROR:crearMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta
    
    @staticmethod
    def actualizarMateriaUseCase(clave: str, nuevoNombre: str, nuevoCreditos: str):
        
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            MateriaRepository.actualizarMateriaEnBD(clave = clave, nuevoNombre=nuevoNombre, nuevoCreditos=nuevoCreditos)
            respuesta.mensaje = "Materia actualizada con éxito"
        except Exception as error:
            print("ERROR:actualizarMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarMateriaUseCase(clave: str):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        try:
            MateriaRepository.eliminarMateriaEnBD(clave=clave)
            respuesta.mensaje = "Materia eliminada exitosamente"
        except Exception as error:
            print("ERROR:eliminarMateriaUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        