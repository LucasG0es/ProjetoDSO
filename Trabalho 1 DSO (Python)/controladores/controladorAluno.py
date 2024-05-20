from classes.aluno import Aluno
from telas.telaAluno import TelaAluno


class ControladorAluno:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    def encontrar_aluno_por_matricula(self, matricula: int):
        # While que passa pelos alunos, retorna o Aluno com a matrícula informada se existir,
        # se não retorna None
        i = 0
        alunos = self.__alunos
        while i < len(alunos):
            aluno = alunos[i]
            if aluno.matricula == matricula:
                return aluno

            i = i + 1
        return None

    def incluir_aluno(self, nome, cpf, dia, mes, ano, curso, matricula, quantidade_gols):
        # Verifica se o aluno já existe, e caso exista para o código
        if self.encontrar_aluno_por_matricula(matricula) != None:
            return

        # Adiciona o aluno na lista de alunos
        aluno = Aluno(nome=nome, cpf=cpf, dia=dia, mes=mes, ano=ano, curso=curso, matricula=matricula, quantidade_gols=quantidade_gols)
        self.__alunos.append(aluno)

    def excluir_aluno(self, matricula: int):
        # Verifica se o aluno já existe, e caso exista o remove da lista
        aluno = self.encontrar_aluno_por_matricula(matricula)
        if aluno != None:
            self.__alunos.remove(aluno)
            return aluno
        return None
    
    def mostrar_aluno(self, aluno: Aluno):
        if not isinstance(aluno, Aluno):
            return
        
        nascimento = aluno.data_de_nascimento

        dados = {}
        dados['nome'] = aluno.nome
        dados['cpf'] = aluno.cpf
        dados['nascimento'] = str(nascimento["dia"]) + "/" + str(nascimento["mes"]) + "/" + str(nascimento["ano"])
        dados['curso'] = aluno.curso.nome
        dados['matricula'] = aluno.matricula
        dados['gols'] = aluno.quantidade_gols

        self.__tela.mostrar_aluno(dados)

    def listar_alunos(self):
        # Envia os dados do aluno que serão exibidos pela tela
        alunos = self.__alunos
        i = 0
        while i < len(alunos):
            self.mostrar_aluno(alunos[i])

            i = i + 1
    
    def alterar_aluno(self):
        #listar Cursos para o usuario
        self.listar_alunos()

        #Coleta input de um codigo
        matricula = self.__tela.solicitar_input("Matrícula do Aluno")
        aluno = self.encontrar_aluno_por_matricula(matricula)
        continua = matricula != 0 and aluno != None
        
        if continua:
            #Tela de alteração de dados
            condicao_tela_curso = True
            while condicao_tela_curso:
                self.mostrar_aluno(aluno)
                opcao = int(self.__tela.tela_aluno())

                if opcao == 1:
                    nome = self.__tela.solicitar_input("Nome do Aluno")
                    if nome != 0:
                        aluno.nome = nome

                if opcao == 2:
                    controlador_curso = self.__controlador_sistema.controlador_curso
                    
                    controlador_curso.listar_cursos()
                    codigo = int(self.__tela.solicitar_input("Código do Curso do Aluno"))
                    curso = controlador_curso.encontrar_curso_por_codigo(codigo)

                    if codigo != 0:
                        aluno.curso = curso

                elif opcao == 0:
                    condicao_tela_curso = False

    def abrir_tela(self):
        # Inicia o sistema
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # Listar Alunos
            if opcao_tela == 1:

                # Listar Alunos para o usuário
                self.listar_alunos()

                # Coleta input de uma matricula
                self.__tela.aguardar_input()

            # Inclui Aluno
            if opcao_tela == 2:
                continua = True

                # Coleta input de um nome
                if continua:
                    nome = self.__tela.solicitar_input("Nome do Aluno")
                    if nome == 0:
                        continua = False
                
                if continua:
                    cpf = int(self.__tela.solicitar_input("CPF do Aluno"))
                    if cpf == 0:
                        continua = False
                
                if continua:
                    dia = int(self.__tela.solicitar_input("Dia de Nascimento do Aluno"))
                    if dia == 0:
                        continua = False
                
                if continua:
                    mes = int(self.__tela.solicitar_input("Mês de Nascimento do Aluno"))
                    if mes == 0:
                        continua = False
                
                if continua:
                    ano = int(self.__tela.solicitar_input("Ano de Nascimento do Aluno"))
                    if ano == 0:
                        continua = False
                
                if continua:
                    matricula = int(self.__tela.solicitar_input("Matrícula do Aluno"))
                    if matricula == 0:
                        continua = False
                
                if continua:
                    controlador_curso = self.__controlador_sistema.controlador_curso
                    
                    controlador_curso.listar_cursos()
                    codigo = int(self.__tela.solicitar_input("Código do Curso do Aluno"))
                    curso = controlador_curso.encontrar_curso_por_codigo(codigo)
                    if codigo == 0 or curso == None:
                        continua = False
                
                if continua:
                    self.incluir_aluno(nome, cpf, dia, mes, ano, curso, matricula, 0)

            # Altera Aluno
            if opcao_tela == 3:
                self.alterar_aluno()

            # Exclui aluno
            if opcao_tela == 4:

                # Listar Alunos para o usuario
                self.listar_alunos()

                # Coleta input de uma matricula
                matricula = int(self.__tela.solicitar_input("Mátricula do Aluno"))

                if matricula != 0:
                     self.excluir_aluno(matricula=matricula)

            # Encerra a tela
            elif opcao_tela == 0:
                condicao = False
