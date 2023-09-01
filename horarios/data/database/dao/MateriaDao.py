

from horarios.data.database.entities.MateriaEntity import Materia

class MateriaDao():
    
    @staticmethod
    def obtenerMateria(clave: str):
        return Materia.objects.get(clave = clave)
    
    @staticmethod
    def obtenerMateriasPorDocente():
        return Materia.objects.all()
    
    @staticmethod
    def crearMateria(clave:str, nombre:str, creditos:str):
        Materia(clave = clave, nombre = nombre, creditos = creditos).save()
    
    @staticmethod
    def actualizarMateria(clave: str, nuevoNombre: str, nuevoCreditos: str):
        Materia.objects.filter(clave = clave).update(nombre =nuevoNombre, creditos = nuevoCreditos)

    @staticmethod
    def eliminarMateria(clave: str):
        Materia.objects.get(clave = clave).delete()
    