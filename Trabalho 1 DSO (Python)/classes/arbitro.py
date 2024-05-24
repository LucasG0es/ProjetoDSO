from classes.abstractPessoa import Pessoa


class Arbitro(Pessoa):
    def __init__(self, nome, cpf, dia, mes, ano):
        super().__init__(nome=nome, cpf=cpf, dia=dia, mes=mes, ano=ano)
        
        self.__numero_de_partidas = 0
    
    # Getters

    @property
    def numero_de_partidas(self):
        return self.__numero_de_partidas

    # Setters

    @numero_de_partidas.setter
    def numero_de_partidas(self, numero_de_partidas):
        if isinstance(numero_de_partidas, int):
            self.__numero_de_partidas = numero_de_partidas
