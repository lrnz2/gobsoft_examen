from horarios.data.database.dao.DocenteDao import DocenteDao
from horarios.data.database.entities.DocenteEntity import Docente

class DocenteRepository():
    
    @staticmethod
    def obtenerDocentesDeBD():
        response:list[Docente] = DocenteDao.obtenerDocentes()
        return response
    
    @staticmethod
    def obtenerDocenteDeBD(matricula:str):
        response:Docente = DocenteDao.obtenerDocente(matricula=matricula)
        return response
    
    @staticmethod
    def crearDocenteEnBD(matricula: str, nombre: str, apellidos:str):
        DocenteDao.crearDocente(matricula = matricula, nombre = nombre, apellidos = apellidos)
    
    @staticmethod
    def actualizarDocenteEnBD(matricula: str, nuevoNombre: str, nuevoApellidos: str):
        DocenteDao.actualizarDocente(matricula = matricula, nuevoNombre=nuevoNombre, nuevoApellidos=nuevoApellidos)
    
    @staticmethod
    def eliminarDocenteEnBD(matricula: str):
        DocenteDao.eliminarDocente(matricula)