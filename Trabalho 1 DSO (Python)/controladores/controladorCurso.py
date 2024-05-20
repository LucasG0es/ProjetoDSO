from classes.curso import Curso
from telas.telaCurso import TelaCurso


class ControladorCurso:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__tela = TelaCurso()
        self.__controlador_sistema = controlador_sistema
    
    def encontrar_curso_por_codigo(self, codigo: int):
        # While que passa pelos cursos, retorna o Curso com o codigo informado se existir,
        # se não retorna None
        i = 0
        cursos = self.__cursos
        while i < len(cursos):
            curso = cursos[i]
            if curso.codigo == codigo:
                return curso

            i = i + 1
        return None

    def incluir_curso(self, nome: str, codigo: int):
        # Verifica se o curso já existe, e caso exista para o código
        if not (isinstance(nome,str) and isinstance(codigo, int)) or self.encontrar_curso_por_codigo(codigo) != None:
            return

        # Adiciona o curso na listar de cursos
        curso = Curso(nome=nome, codigo=codigo)
        self.__cursos.append(curso)

    
    def excluir_curso(self, codigo: int):
        # Verifica se o curso já existe, e caso exista o remove da lista
        cursos = self.__cursos
        curso = self.encontrar_curso_por_codigo(codigo)
        if curso != None:
            cursos.remove(curso)
            return curso
        return None

    def listar_cursos(self):
        # Envia os dados do curso que serão exibidos pela tela
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
        #listar Cursos para o usuario
        self.listar_cursos()

        #Coleta input de um codigo
        codigo = self.__tela.informar_codigo()
        curso = self.encontrar_curso_por_codigo(codigo)
        continua = codigo != 0 and curso != None
        
        if continua:
            #Tela de alteração de dados
            condicao_tela_curso = True
            while condicao_tela_curso:
                dados = {}
                dados["nome"] = curso.nome
                dados["codigo"] = curso.codigo

                self.__tela.mostrar_curso(dados)
                opcao = int(self.__tela.tela_curso())

                if opcao == 1:
                    nome = self.__tela.informar_nome()
                    if nome != 0:
                        curso.nome = nome
                
                elif opcao == 0:
                    condicao_tela_curso = False
    
    def abrir_tela(self):
        # Inicia o sistema
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # listarr Cursos
            if  opcao_tela == 1:

                #listarr Cursos para o usuario
                self.listar_cursos()

                #Coleta input de um codigo
                self.__tela.aguardar_input()

            # incluir Curso
            if  opcao_tela == 2:

                #Coleta input de um codigo
                codigo = self.__tela.informar_codigo()
                continua = codigo != 0

                #Coleta input de um nome
                if continua:
                    nome = self.__tela.informar_nome()
                    continua = nome != 0

                if continua:
                    self.incluir_curso(nome=nome, codigo=codigo)

            # Editar Curso
            if  opcao_tela == 3:
                self.alterar_curso()

            # excluir Curso
            if  opcao_tela == 4:

                #listarr Cursos para o usuario
                self.listar_cursos()

                #Coleta input de um codigo
                codigo = self.__tela.informar_codigo()
                continua = codigo != 0

                if continua:
                    self.excluir_curso(codigo=codigo)

            # Encerra a tela
            elif opcao_tela == 0:
                condicao = False