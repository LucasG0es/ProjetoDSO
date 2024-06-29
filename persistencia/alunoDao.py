from classes.aluno import Aluno
from persistencia.dao import DAO


class AlunoDAO(DAO):
    def __init__(self):
        super().__init__(datasource="alunos.pkl")

    def add(self, obj):
        if isinstance(obj, Aluno):
            super().add(key=obj.matricula, obj=obj)