from classes.equipe import Equipe
from classes.curso import Curso
from telas.telaEquipe import TelaEquipe
from persistencia.equipeDao import EquipeDAO


class ControladorEquipe:
    def __init__(self, controlador_sistema):
        self.__dao_equipes = EquipeDAO()
        self.__tela = TelaEquipe()
        self.__controlador_sistema = controlador_sistema
    
    def encontrar_equipe_por_codigo(self, codigo: int):
        # Recebe um codigo
        # Retorna um curso com o codigo informado, se existir
        i = 0
        equipes = self.__dao_equipes.get_all()
        while i < len(equipes):
            equipe = equipes[i]
            if equipe.codigo == codigo:
                return equipe

            i = i + 1
        return None

    def incluir_equipe(self, nome: str, curso: Curso, codigo: int):
        # Recebe dados para uma nova equipe
        # Se o codigo informado já não pertencer a uma equipe, inclui essa equipe na lista

        if not (isinstance(nome, str) and isinstance(curso, Curso) and isinstance(codigo, int)) or self.encontrar_equipe_por_codigo(codigo) != None:
            return

        equipe = Equipe(nome=nome, curso=curso, codigo=codigo)
        self.__dao_equipes.add(equipe)
    
    def excluir_equipe(self,codigo):
        # Recebe um codigo, e remove uma equipe com esse codigo, se existir
        equipe = self.encontrar_equipe_por_codigo(codigo)
        if equipe != None:
            self.__dao_equipes.remove(equipe)
        
    def listar_equipes(self, equipes=None):
        # Encaminha os codigos de cada equipe para a exibição da tela
        if equipes == None:
            equipes = self.__dao_equipes.get_all()
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
        # Encaminha os dados de cada aluno dentro de uma equipe para ser exibido pela tela
        alunos = equipe.alunos
        controlador_aluno = self.__controlador_sistema.controlador_aluno
        i = 0
        while i < len(alunos):
            controlador_aluno.mostrar_aluno(alunos[i])

            i = i + 1
        
    def alterar_equipe(self):
        # Acessa uma equipe para editar
        self.listar_equipes()

        codigo = int(self.__tela.solicitar_input("Código da Equipe"))
        equipe = self.encontrar_equipe_por_codigo(codigo)
        continua = codigo != 0 and equipe != None
        
        if continua:           
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
                    controlador_aluno = self.__controlador_sistema.controlador_aluno
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
        # Inicia o menu de equipes
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # Listar Equipes
            if  opcao_tela == 1:
                self.listar_equipes()

                self.__tela.aguardar_input()

            # Incluir Equipe
            if  opcao_tela == 2:

                codigo = int(self.__tela.solicitar_input("Código da Equipe"))
                continua = codigo != 0

                if continua:
                    nome = nome = self.__tela.solicitar_input("Nome da Equipe")
                    continua = nome != 0
                
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
                self.listar_equipes()

                codigo = int(self.__tela.solicitar_input("Código da Equipe"))
                continua = codigo != 0

                if continua:
                    self.excluir_equipe(codigo=codigo)

            # Encerra a tela
            elif opcao_tela == 0:
                condicao = False