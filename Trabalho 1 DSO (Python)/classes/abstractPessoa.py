from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, dia: int, mes: int, ano: int):
        self.__nome = None
        self.__cpf = None
        self.__data_de_nascimento = {}

        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(cpf, int):
            self.__cpf = cpf

        if isinstance(dia, int):
            self.__data_de_nascimento["dia"] = dia

        if isinstance(mes, int):
            self.__data_de_nascimento["mes"] = mes

        if isinstance(ano, int):
            self.__data_de_nascimento["ano"] = ano

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome