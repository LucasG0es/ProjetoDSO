from classes.campeonato import Campeonato
from persistencia.dao import DAO


class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__(datasource="campeonato.pkl")

    def add(self, obj):
        if isinstance(obj, Campeonato):
            super().add(key=obj.codigo, obj=obj)