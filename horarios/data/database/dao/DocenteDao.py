

from horarios.data.database.entities.DocenteEntity import Docente

class DocenteDao():

    @staticmethod
    def obtenerDocentes():
        return Docente.objects.all()
    
    @staticmethod
    def obtenerDocente(matricula:str):
        return Docente.objects.get(matricula = matricula)
    
    @staticmethod
    def crearDocente(matricula: str, nombre: str, apellidos:str):
        Docente(matricula = matricula, nombre = nombre, apellidos = apellidos).save()
    
    @staticmethod
    def actualizarDocente(matricula: str, nuevoNombre: str, nuevoApellidos: str):
        Docente.objects.filter(matricula = matricula).update(nombre =nuevoNombre, apellidos = nuevoApellidos)

    @staticmethod
    def eliminarDocente(matricula: str):
        Docente.objects.get(matricula = matricula).delete()
    