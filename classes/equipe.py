from classes.aluno import Aluno
from classes.curso import Curso


class Equipe:
    def __init__(self, nome: str, codigo: int, curso: Curso):
        self.__nome = None
        self.__curso = None
        self.__codigo = None
        self.__alunos = []

        if isinstance(nome, str):
            self.__nome = nome
        
        if isinstance(codigo, int):
            self.__codigo = codigo

        if isinstance(curso, Curso):
            self.__curso = curso

    # Getters

    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def alunos(self):
        return self.__alunos
    
    # Setters

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @curso.setter
    def curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso
    
    # Funções
    
    def incluir_aluno(self, aluno: Aluno):
        # Recebe um aluno e inclui na lista de alunos da equipe
        if isinstance(aluno, Aluno) and aluno not in self.__alunos:
            self.__alunos.append(aluno)
    
    def remover_aluno(self, aluno: Aluno):
        # Recebe um aluno e o remove da equipe, caso ele esteja nela
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)