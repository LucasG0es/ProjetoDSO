from classes.curso import Curso
from telas.telaCurso import TelaCurso


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__tela = TelaCurso()
        self.__controlador_sistema = controlador_sistema

    # Funções
    
    def encontrar_curso_por_codigo(self, codigo: int):
        # Recebe um código
        # Retorna um curso com o código informado, se houver
        i = 0
        cursos = self.__cursos
        while i < len(cursos):
            curso = cursos[i]
            if curso.codigo == codigo:
                return curso

            i = i + 1
        return None

    def incluir_curso(self, nome: str, codigo: int):
        # Recebe dados para criar um novo curso, e caso o código não esteja em uso, inclui o curso na lista
        if not (isinstance(nome,str) and isinstance(codigo, int)) or self.encontrar_curso_por_codigo(codigo) != None:
            return

        curso = Curso(nome=nome, codigo=codigo)
        self.__cursos.append(curso)

    
    def excluir_curso(self, codigo: int):
        # Recebe um código
        # Remove um curso com o código informado, se ele existir
        cursos = self.__cursos
        curso = self.encontrar_curso_por_codigo(codigo)
        if curso != None:
            cursos.remove(curso)
            return curso
        return None

    def listar_cursos(self):
        # Coleta os dados de cada curso, e encaminha para a tela exibir
        cursos = self.__cursos
        i = 0
        while i < len(cursos):
            curso = cursos[i]

            nome = curso.nome
            codigo = curso.codigo

            dados = {}
            dados["nome"]=nome
            dados["codigo"]=codigo

            self.__tela.mostrar_curso(dados)

            i = i + 1
    
    def alterar_curso(self):
        # Acessa um curso para editar
        self.listar_cursos()

        codigo = self.__tela.informar_codigo()
        curso = self.encontrar_curso_por_codigo(codigo)
        continua = codigo != 0 and curso != None
        
        if continua:
            condicao_tela_curso = True
            while condicao_tela_curso:
                dados = {}
                dados["nome"] = curso.nome
                dados["codigo"] = curso.codigo

                self.__tela.mostrar_curso(dados)
                opcao = int(self.__tela.tela_curso())

                # Alterar nome
                if opcao == 1:
                    nome = self.__tela.informar_nome()
                    if nome != 0:
                        curso.nome = nome
                
                elif opcao == 0:
                    condicao_tela_curso = False
    
    def abrir_tela(self):
        # Inicia o menu de cursos
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # Lista os Cursos
            if  opcao_tela == 1:
                self.listar_cursos()

                self.__tela.aguardar_input()

            # Inclui um novo curso
            if  opcao_tela == 2:
                dados = self.__tela.criar_curso()
                self.incluir_curso(nome=dados["Nome"], codigo=int(dados["Codigo"]))

            # Editar Curso
            if  opcao_tela == 3:
                self.alterar_curso()

            # Excluir Curso
            if  opcao_tela == 4:
                self.listar_cursos()

                codigo = self.__tela.informar_codigo()
                continua = codigo != 0

                if continua:
                    self.excluir_curso(codigo=codigo)

            # Retorna
            elif opcao_tela == 0:
                condicao = False