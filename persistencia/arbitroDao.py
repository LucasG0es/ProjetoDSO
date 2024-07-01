from classes.arbitro import Arbitro
from persistencia.dao import DAO


class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__(datasource="arbitros.pkl")

    def add(self, obj):
        if isinstance(obj, Arbitro):
            super().add(key=obj.matricula, obj=obj)