from classes.equipe import Equipe
from controladores.controladorPartida import ControladorPartida


class Campeonato: 
    def __init__(self, nome: str, codigo: int, controlador_sistema):
        self.__nome = None
        self.__codigo = None
        self.__equipes = []
        self.__controlador_partida = ControladorPartida(controlador_sistema, self)

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, int):
            self.__codigo = codigo
    
    @property
    def controlador_partida(self):
        return self.__controlador_partida

    @property
    def nome(self):
        return self.__nome
        
    @property
    def codigo(self):
        return self.__codigo
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
    
    @property
    def equipes(self):
        return self.__equipes

    def incluir_equipe(self, equipe):
        if isinstance(equipe, Equipe) and equipe not in self.__equipes:
            self.__equipes.append(equipe)
    
    def remover_equipe(self, equipe):
        if equipe in self.__equipes:
            self.__equipes.remove(equipe)
    
    def pontuacao_equipe(self, equipe):
        partidas = self.__controlador_partida.partidas
        pontuacao = 0
        i = 0
        while i < len(partidas):
            partida = partidas[i]
            resultado = partida.calcula_resultado()

            if resultado != None:
                if equipe in resultado:
                    if len(resultado) == 1:
                        pontuacao = pontuacao + 3
                    else:
                        pontuacao = pontuacao + 1

            i = i + 1
        return pontuacao

    def saldo_gols_equipe(self, equipe):
        partidas = self.__controlador_partida.partidas
        gols = 0
        i = 0
        while i < len(partidas):
            partida = partidas[i]

            if equipe in partida.gols:
                gols = gols + partida.gols[equipe]

            i = i + 1
        return gols

    def gols_tomados_equipe(self, equipe):
        partidas = self.__controlador_partida.partidas
        gols_tomados = 0
        i = 0
        while i < len(partidas):
            partida = partidas[i]

            if equipe in partida.equipes and len(partida.equipes) == 2:
                if partida.equipes[0] != equipe:
                    equipeAdversaria = partida.equipes[0]
                if partida.equipes[1] != equipe:
                    equipeAdversaria = partida.equipes[1]
                
                gols_tomados = gols_tomados + partida.gols[equipeAdversaria]

            i = i + 1
        return gols_tomados

    @property
    def equipes_ordenadas(self):
        i = 0
        equipes = []
        while i < len(self.__equipes):
            equipes.append(self.__equipes[i])
            i = i + 1

        def pontuacao(equipe):
            return self.pontuacao_equipe(equipe)
        
        equipes.sort(key=pontuacao, reverse=True)

        return equipes