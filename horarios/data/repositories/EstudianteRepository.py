
from horarios.data.database.dao.EstudianteDao import EstudianteDao
from horarios.data.database.entities.EstudianteEntity import Estudiante

class EstudianteRepository():
    @staticmethod
    def obtenerTodosLosGruposRelacionadosAEstudianteDeBD(estudianteMatricula):
        return EstudianteDao.obtenerTodosLosGruposRelacionadosAEstudiante(estudianteMatricula=estudianteMatricula)
    @staticmethod
    def obtenerEstudiantesPorGrupoDeBD(grupoId) -> list[Estudiante] :
        return EstudianteDao.obtenerEstudiantesPorGrupo(grupoId = grupoId)
    
    @staticmethod
    def crearEstudianteEnBD( matricula: str, nombre: str, apellidos:str):
        EstudianteDao.crearEstudiante(matricula = matricula, nombre = nombre, apellidos = apellidos)
    
    @staticmethod
    def actualizarEstudianteEnBD( matricula: str, nuevoNombre: str, nuevoApellidos: str):
        EstudianteDao.actualizarEstudiante(matricula = matricula, nuevoNombre=nuevoNombre, nuevoApellidos=nuevoApellidos)

    @staticmethod
    def eliminarEstudianteEnBD( matricula: str):
        EstudianteDao.eliminarEstudiante(matricula)
    
    @staticmethod
    def asignarEstudianteAGrupoEnBD( estudianteMatricula: str, grupoId: int):
        EstudianteDao.asignarEstudianteAGrupo(estudianteMatricula=estudianteMatricula, grupoId=grupoId)
    
    @staticmethod
    def desasignarEstudianteAGrupoEnBD( estudianteMatricula: str, grupoId: int):
        EstudianteDao.desasignarEstudianteAGrupo(estudianteMatricula=estudianteMatricula, grupoId=grupoId)