from controladores.controladorPartida import ControladorPartida
from controladores.controladorSistema import ControladorSistema


class Campeonato: 
    def __init__(self, codigo: int, controlador_sistema: ControladorSistema):
        self.__codigo = None
        self.__controlador_sistema = None

        if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema

        if isinstance(codigo, int):
            self.__codigo = codigo
        
        self.__controlador_partidas = ControladorPartida(controlador_sistema=controlador_sistema, campeonato=self)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo