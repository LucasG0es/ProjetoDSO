from classes.curso import Curso
from telas.telaCurso import TelaCurso
from persistencia.cursoDao import CursoDAO


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__dao_cursos = CursoDAO()
        self.__tela = TelaCurso()
        self.__controlador_sistema = controlador_sistema

    # Funções
    
    def encontrar_curso_por_codigo(self, codigo: int):
        # Recebe um código
        # Retorna um curso com o código informado, se houver
        i = 0
        cursos = self.__dao_cursos.get_all()
        while i < len(cursos):
            curso = cursos[i]
            if curso.codigo == codigo:
                return curso

            i = i + 1
        return None
    
    def lista_cursos(self):
        retorno = []
        cursos = self.__dao_cursos.get_all()
        i = 0
        while i < len(cursos):
            curso = cursos[i]
            atual = [curso.nome, curso.codigo]
            retorno.append(atual)

            i = i + 1
        return retorno

    def incluir_curso(self, nome: str, codigo: int):
        # Recebe dados para criar um novo curso, e caso o código não esteja em uso, inclui o curso na lista
        if not (isinstance(nome,str) and isinstance(codigo, int)) or self.encontrar_curso_por_codigo(codigo) != None:
            return

        curso = Curso(nome=nome, codigo=codigo)
        self.__dao_cursos.add(curso)

    def excluir_curso(self, codigo: int):
        # Recebe um código
        # Remove um curso com o código informado, se ele existir
        curso = self.encontrar_curso_por_codigo(codigo)
        if curso != None:
            self.__dao_cursos.remove(codigo)
        return None
    
    def abrir_tela(self):
        # Inicia o menu de cursos
        condicao = True
        while condicao:
            tela = self.__tela.tela_inicial(self.lista_cursos())
            opcao_tela = tela[0]

            # Inclui um novo curso
            if  opcao_tela == 2:
                dados = self.__tela.formulario_curso()
                if dados != None:
                    self.incluir_curso(nome=dados["Nome"], codigo=int(dados["Codigo"]))

            # Editar Curso
            if  opcao_tela == 3:
                curso = self.encontrar_curso_por_codigo(tela[1])
                dados = self.__tela.formulario_curso(nome=curso.nome, codigo=curso.codigo)
                if dados != None:
                    curso.nome = dados["Nome"]
                    self.__dao_cursos.add(self.encontrar_curso_por_codigo(tela[1]))
                

            # Excluir Curso
            if  opcao_tela == 4:
                self.excluir_curso(tela[1])

            # Retorna
            elif opcao_tela == 0:
                condicao = False