
from horarios.data.database.entities.ClaseEntity import Clase
from horarios.data.repositories.ClaseRepository import ClaseRepository

from horarios.domain.model.RespuestaOperacion import RespuestaOperacion
from horarios.domain.MateriaUseCases import MateriaUseCases
from horarios.domain.DocenteUseCases import DocenteUseCases
from horarios.domain.GrupoHasUseCases import GrupoHasUseCases
from horarios.domain.GrupoUseCases import GrupoUseCases

class ClaseUseCases():
    
    
    @staticmethod
    def obtenerContadorMateriaEnClasesDeBD(materiaClave:str, docenteMatricula:str) -> list[Clase]:
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: int = ClaseRepository.obtenerContadorMateriaEnClasesDeBD(materiaClave=materiaClave, docenteMatricula=docenteMatricula)
        except Clase.DoesNotExist as error:
            print("ERROR:obtenerClasesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
        except Exception as error:
            print("ERROR:obtenerClasesUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"
        return respuesta
    
    
    @staticmethod
    def obtenerClaseUseCase(docente, materia, hora, dia):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: Clase = ClaseRepository.obtenerClaseDeBD(docente=docente, materia=materia, hora=hora, dia=dia)
        except Clase.DoesNotExist as error:
            print("ERROR:obtenerClaseUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
        except Exception as error:
            print("ERROR:obtenerClaseUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"

        return respuesta
      
    @staticmethod
    def obtenerClasePorIdUseCase(claseId):
        respuesta: RespuestaOperacion = RespuestaOperacion()

        try:
            respuesta.contenido: Clase = ClaseRepository.obtenerClaseDeBD(claseId=claseId)
        except Clase.DoesNotExist as error:
            print("ERROR:obtenerClaseUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "No hay registros"
        except Exception as error:
            print("ERROR:obtenerClaseUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Ha ocurrido un error en el sistema"

        return respuesta
    
    @staticmethod
    def crearClaseUseCase( materiaClave:str, docenteMatricula:str, grupoId:str, hora: str, dia:str, materiaNuevaClave="", materiaNombre:str="", materiaCreditos:str=""):

        respuestaOperacionCrearMateria:RespuestaOperacion = None
        if(materiaClave == "crear-nueva-materia"):
            respuestaOperacionCrearMateria = MateriaUseCases.crearMateriaUseCase(clave=materiaNuevaClave, nombre = materiaNombre, creditos = materiaCreditos)
            if (respuestaOperacionCrearMateria.error):
                return respuestaOperacionCrearMateria
            materiaClave = materiaNuevaClave
            
        respuestaOperacionObtenerMateria:RespuestaOperacion = MateriaUseCases.obtenerMateriaUseCase(clave=materiaClave)
        if(respuestaOperacionObtenerMateria.error):
            return respuestaOperacionCrearMateria
        
        respuestaOperacionObtenerDocente:RespuestaOperacion = DocenteUseCases.obtenerDocenteUseCase(matricula = docenteMatricula)
        if(respuestaOperacionObtenerDocente.error):
            return respuestaOperacionObtenerDocente
        
        respuestaOperacionCrearClase: RespuestaOperacion = RespuestaOperacion()
        try:
            ClaseRepository.crearClaseEnBD(
                docente = respuestaOperacionObtenerDocente.contenido,
                materia = respuestaOperacionObtenerMateria.contenido,
                hora = hora,
                dia = dia)
            respuestaOperacionCrearClase.mensaje = "Clase creada con exito"
        except Exception as error:
            print("ERROR:crearClaseUseCase: ", error)
            respuestaOperacionCrearClase.error = True
            respuestaOperacionCrearClase.mensaje = "Operación fallida"

        respuestaOperacionObtenerGrupo = GrupoUseCases.obtenerGrupoUseCase(grupoId=grupoId)
        if(respuestaOperacionObtenerGrupo.error):
            return respuestaOperacionObtenerGrupo
        
        respuestaOperacionObtenerClase = ClaseUseCases.obtenerClaseUseCase(
            docente = respuestaOperacionObtenerDocente.contenido,
            materia = respuestaOperacionObtenerMateria.contenido,
            hora = hora,
            dia = dia
            )
        if(respuestaOperacionObtenerClase.error):
            return respuestaOperacionObtenerClase

        respuestaOperacionAsignarClaseAGrupo:RespuestaOperacion = GrupoHasUseCases.asignarClaseAGrupoUseCase(
            grupo = respuestaOperacionObtenerGrupo.contenido,
            clase = respuestaOperacionObtenerClase.contenido
        )

        if respuestaOperacionAsignarClaseAGrupo.error:
            ClaseUseCases.eliminarClaseUseCase(respuestaOperacionObtenerClase.contenido.id)
            return respuestaOperacionAsignarClaseAGrupo
        print("Exiting::", respuestaOperacionCrearClase)
        return respuestaOperacionCrearClase
    
    
    @staticmethod
    def actualizarClaseUseCase(claseId:str, materiaClaveActual, materiaClaveNueva: str, nuevaMateriaClave, nuevaMateriaNombre, nuevaMateriaCreditos):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        if (materiaClaveActual == materiaClaveNueva):
            respuesta.mensaje = "No se detectaron cambios"
            return respuesta
        
        if(materiaClaveNueva == "crear-nueva-materia"):
            respuestaOperacionCrearMateria = MateriaUseCases.crearMateriaUseCase(
                clave = nuevaMateriaClave,
                nombre=nuevaMateriaNombre,
                creditos=nuevaMateriaCreditos )
            if(respuestaOperacionCrearMateria.error):
                return respuestaOperacionCrearMateria
            materiaClaveNueva = nuevaMateriaClave
        
        respuestaOperacionObtenerMateria:RespuestaOperacion = MateriaUseCases.obtenerMateriaUseCase(clave=materiaClaveNueva)
        if(respuestaOperacionObtenerMateria.error):
            return respuestaOperacionObtenerMateria
        
        try:
            ClaseRepository.actualizarClaseEnBD(
                claseId = claseId, 
                materia = respuestaOperacionObtenerMateria.contenido)
            respuesta.mensaje = "Clase actualizada con exito"
        except Exception as error:
            print("ERROR:actualizarClaseUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"
            
        return respuesta
    
    @staticmethod
    def eliminarClaseUseCase(id: str, materiaClave, docenteMatricula):
        respuesta: RespuestaOperacion = RespuestaOperacion()
        respuestaObtenerMateriaContador:RespuestaOperacion = ClaseUseCases.obtenerContadorMateriaEnClasesDeBD(materiaClave=materiaClave, docenteMatricula=docenteMatricula)
        if(respuestaObtenerMateriaContador.contenido <= 1):
            respuestaOperacionEliminarMateria = MateriaUseCases.eliminarMateriaUseCase(materiaClave)
            if(respuestaOperacionEliminarMateria.error):
                respuesta.error = True
                respuesta.mensaje = "Operación fallida"
                return respuesta
            respuesta.mensaje = "Clase eliminada exitosamente"
            return respuesta
        try:
            ClaseRepository.eliminarClaseEnBD(id=id)
            respuesta.mensaje = "Clase eliminada exitosamente"
        except Exception as error:
            print("ERROR:eliminarClaseUseCase: ", error)
            respuesta.error = True
            respuesta.mensaje = "Operación fallida"

        return respuesta

        