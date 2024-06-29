from classes.equipe import Equipe
from persistencia.dao import DAO


class EquipeDAO(DAO):
    def __init__(self):
        super().__init__(datasource="equipes.pkl")

    def add(self, obj):
        if isinstance(obj, Equipe):
            super().add(key=obj.codigo, obj=obj)