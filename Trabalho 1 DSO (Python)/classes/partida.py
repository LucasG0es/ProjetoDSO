from classes.equipe import Equipe
from classes.aluno import Aluno
from classes.arbitro import Arbitro

class Partida:
    def __init__(self, codigo: int, arbitro: Arbitro):
        self.__codigo = None
        self.__arbitro = None
        self.__gols = {}
        self.__equipes = []

        if isinstance(codigo, int):
            self.__codigo = codigo
        
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro
            arbitro.numero_de_partidas = arbitro.numero_de_partidas + 1
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def arbitro(self):
        return self.__arbitro

    @property
    def gols(self):
        return self.__gols
    
    @property
    def equipes(self):
        return self.__equipes

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @arbitro.setter
    def arbitro(self, arbitro):
        if isinstance(arbitro, Arbitro):
            if self.__arbitro != None:
                self.__arbitro.numero_de_partidas = self.__arbitro.numero_de_partidas - 1

            self.__arbitro = arbitro
            arbitro.numero_de_partidas = arbitro.numero_de_partidas + 1

    def incluir_equipe(self,equipe):
        if isinstance(equipe,Equipe) and len(self.__equipes) < 2:
            self.__equipes.append(equipe)
            self.__gols[equipe] = 0
    
    def remover_equipe(self,equipe):
        if equipe in self.__equipes:
            self.__equipes.remove(equipe)
            self.__gols.pop(equipe)
    
    def adicionar_gol(self,equipe: Equipe, aluno: Aluno):
        if equipe not in self.__equipes or not isinstance(aluno, Aluno):
            return

        self.__gols[equipe] = self.__gols[equipe] + 1
        aluno.quantidade_gols = aluno.quantidade_gols + 1
    
    def calcula_resultado(self):
        if len(self.__equipes) < 2:
            return None

        gols = self.__gols

        if gols[self.__equipes[0]] == gols[self.__equipes[1]]:
            return self.__equipes

        elif gols[self.__equipes[0]] > gols[self.__equipes[1]]:
            return [self.__equipes[0]]
        
        elif gols[self.__equipes[0]] < gols[self.__equipes[1]]:
            return [self.__equipes[1]]