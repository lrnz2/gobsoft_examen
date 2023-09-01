from horarios.data.database.dao.MateriaDao import MateriaDao
from horarios.data.database.entities.MateriaEntity import Materia


class MateriaRepository():
    
    @staticmethod
    def obtenerMateriasPorDocenteDeBD():
        response:list[Materia] = MateriaDao.obtenerMateriasPorDocente()
        return response@staticmethod
    
    def obtenerMateriaDeBD(clave:str):
        response:Materia = MateriaDao.obtenerMateria(clave=clave)
        return response
    
    @staticmethod
    def crearMateriaEnBD(clave: str, nombre: str, creditos:str):
        MateriaDao.crearMateria(clave = clave, nombre = nombre, creditos = creditos)
    
    @staticmethod
    def actualizarMateriaEnBD(clave: str, nuevoNombre: str, nuevoCreditos: str):
        MateriaDao.actualizarMateria(clave = clave, nuevoNombre=nuevoNombre, nuevoCreditos=nuevoCreditos)
    
    @staticmethod
    def eliminarMateriaEnBD(clave: str):
        MateriaDao.eliminarMateria(clave)