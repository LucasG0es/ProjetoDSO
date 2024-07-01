from classes.partida import Partida
from persistencia.dao import DAO


class PartidaDAO(DAO):
    def __init__(self):
        super().__init__(datasource="partidas.pkl")

    def add(self, obj):
        if isinstance(obj, Partida):
            super().add(key=obj.codigo, obj=obj)