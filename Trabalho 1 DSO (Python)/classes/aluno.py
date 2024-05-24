from classes.abstractPessoa import Pessoa
from classes.curso import Curso


class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: int, dia: int, mes: int, ano: int, curso: Curso, matricula: int, quantidade_gols: int):
        super().__init__(nome=nome, cpf=cpf, dia=dia, mes=mes, ano=ano)
        self.__curso = None
        self.__matricula = None
        self.__quantidade_gols = None

        if isinstance(curso, Curso):
            self.__curso = curso

        if isinstance(matricula, int):
            self.__matricula = matricula

        if isinstance(quantidade_gols, int):
            self.__quantidade_gols = quantidade_gols

    # Getters

    @property
    def curso(self):
        return self.__curso

    @property
    def matricula(self):
        return self.__matricula

    @property
    def quantidade_gols(self):
        return self.__quantidade_gols

    # Setters
    
    @curso.setter
    def curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula

    @quantidade_gols.setter
    def quantidade_gols(self, quantidade_gols):
        if isinstance(quantidade_gols, int):
            self.__quantidade_gols = quantidade_gols
