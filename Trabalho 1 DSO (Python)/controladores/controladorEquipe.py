from classes.equipe import Equipe
from classes.curso import Curso
from telas.telaEquipe import TelaEquipe


class ControladorEquipe:
    def __init__(self, controlador_sistema):
        self.__equipes = []
        self.__tela = TelaEquipe()
        self.__controlador_sistema = controlador_sistema
    
    def encontrar_equipe_por_codigo(self, codigo: int):
        # While que passa pelos Equipes, retorna a Equipe com o codigo informado se existir,
        # se não retorna None
        i = 0
        equipes = self.__equipes
        while i < len(equipes):
            equipe = equipes[i]
            if equipe.codigo == codigo:
                return equipe

            i = i + 1
        return None

    def incluir_equipe(self, nome: str, curso: Curso, codigo: int):
        # Verifica se o Equipe já existe, e caso exista para o código

        if not (isinstance(nome, str) and isinstance(curso, Curso) and isinstance(codigo, int)) or self.encontrar_equipe_por_codigo(codigo) != None:
            return

        # Adiciona a Equipe na lista de Equipes
        equipe = Equipe(nome=nome, curso=curso, codigo=codigo)
        self.__equipes.append(equipe)
    
    def excluir_equipe(self,codigo):
        equipe = self.encontrar_equipe_por_codigo(codigo)
        if equipe != None:
            self.__equipes.remove(equipe)
        
    def listar_equipes(self, equipes=None):
        # Envia os dados do equipe que serão exibidos pela tela
        if equipes == None:
            equipes = self.__equipes
        i = 0
        while i < len(equipes):
            equipe = equipes[i]

            dados = {}
            dados["nome"] = equipe.nome
            dados["curso"] = equipe.curso.nome
            dados["codigo"] = equipe.codigo

            self.__tela.mostrar_equipe(dados)

            i = i + 1

    def listar_alunos_equipe(self, equipe):
        # Envia os dados do aluno que serão exibidos pela tela
        alunos = equipe.alunos
        controlador_aluno = self.__controlador_sistema.controlador_aluno
        i = 0
        while i < len(alunos):
            controlador_aluno.mostrar_aluno(alunos[i])

            i = i + 1
        
    def alterar_equipe(self):
        #Listar equipes para o usuario
        self.listar_equipes()

        #Coleta input de um codigo
        codigo = int(self.__tela.solicitar_input("Código da Equipe"))
        equipe = self.encontrar_equipe_por_codigo(codigo)
        continua = codigo != 0 and equipe != None
        
        if continua:           
            #Tela de alteração de dados
            condicao_tela_equipe = True
            while condicao_tela_equipe:
                dados = {}
                dados["nome"] = equipe.nome
                dados["curso"] = equipe.curso.nome
                dados["codigo"] = equipe.codigo

                self.__tela.mostrar_equipe(dados=dados)
                opcao = int(self.__tela.tela_equipe())

                if opcao == 1:
                    nome = self.__tela.solicitar_input("Nome da Equipe")
                    if nome != 0:
                        equipe.nome = nome
                
                if opcao == 2:
                    controlador_curso = self.__controlador_sistema.controlador_curso
                    
                    controlador_curso.listar_cursos()
                    codigo = int(self.__tela.solicitar_input("Código do Curso da Equipe"))
                    curso = controlador_curso.encontrar_curso_por_codigo(codigo)

                    if codigo != 0:
                        equipe.curso = curso
                
                elif opcao == 3:
                    controlador_aluno = self.__controlador_sistema.controlador_aluno
                    
                    controlador_aluno.listar_alunos()
                    matricula = int(self.__tela.solicitar_input("Matricula do Aluno"))
                    aluno = controlador_aluno.encontrar_aluno_por_matricula(matricula)

                    if matricula != 0:
                        equipe.incluir_aluno(aluno)
                
                elif opcao == 4:
                    self.listar_alunos_equipe(equipe)

                    matricula = int(self.__tela.solicitar_input("Matricula do Aluno"))
                    aluno = controlador_aluno.encontrar_aluno_por_matricula(matricula)

                    if matricula != 0:
                        equipe.remover_aluno(aluno)
                
                elif opcao == 5:
                    self.listar_alunos_equipe(equipe)

                    self.__tela.aguardar_input()
                
                elif opcao == 0:
                    condicao_tela_equipe = False
            
    def abrir_tela(self):
        # Inicia o sistema
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # Listar Equipes
            if  opcao_tela == 1:

                #Listar Cursos para o usuario
                self.listar_equipes()

                #Aguarda input
                self.__tela.aguardar_input()

            # Incluir Equipe
            if  opcao_tela == 2:

                #Coleta input de um codigo
                codigo = int(self.__tela.solicitar_input("Código da Equipe"))
                continua = codigo != 0

                #Coleta input de um nome
                if continua:
                    nome = nome = self.__tela.solicitar_input("Nome da Equipe")
                    continua = nome != 0
                
                #Coleta input de um curso
                if continua:
                    controlador_curso = self.__controlador_sistema.controlador_curso
                    
                    controlador_curso.listar_cursos()
                    codigo_curso = int(self.__tela.solicitar_input("Código do Curso da Equipe"))
                    curso = controlador_curso.encontrar_curso_por_codigo(codigo_curso)

                    continua = codigo_curso != 0

                if continua:
                    self.incluir_equipe(nome=nome, codigo=codigo, curso=curso)

            # Editar Curso
            if  opcao_tela == 3:
                self.alterar_equipe()

            # Exclui Curso
            if  opcao_tela == 4:

                #Listar Cursos para o usuario
                self.listar_equipes()

                #Coleta input de um codigo
                codigo = int(self.__tela.solicitar_input("Código da Equipe"))
                continua = codigo != 0

                if continua:
                    self.excluir_equipe(codigo=codigo)

            # Encerra a tela
            elif opcao_tela == 0:
                condicao = False