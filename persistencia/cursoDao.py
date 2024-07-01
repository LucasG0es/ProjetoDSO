from classes.curso import Curso
from persistencia.dao import DAO


class CursoDAO(DAO):
    def __init__(self):
        super().__init__(datasource="cursos.pkl")

    def add(self, obj):
        if isinstance(obj, Curso):
            super().add(key=obj.codigo, obj=obj)