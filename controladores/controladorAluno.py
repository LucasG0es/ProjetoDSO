from classes.aluno import Aluno
from telas.telaAluno import TelaAluno
from persistencia.alunoDao import AlunoDAO


class ControladorAluno:
    def __init__(self, controlador_sistema):
        self.__dao_alunos = AlunoDAO()
        self.__tela = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    # Funções

    def encontrar_aluno_por_matricula(self, matricula: int):
        # Recebe uma matrícula
        # Caso exista um aluno com a matricula informada, retorna esse aluno
        i = 0
        alunos = self.__dao_alunos.get_all()
        while i < len(alunos):
            aluno = alunos[i]
            if aluno.matricula == matricula:
                return aluno

            i = i + 1
        return None

    def incluir_aluno(self, nome, cpf, dia, mes, ano, curso, matricula, quantidade_gols):
        # Recebe os dados de um novo aluno caso a matricula já não esteja cadastrada, inclui esse aluno na lista de alunos
        if self.encontrar_aluno_por_matricula(matricula) != None:
            return

        aluno = Aluno(nome=nome, cpf=cpf, dia=dia, mes=mes, ano=ano, curso=curso, matricula=matricula, quantidade_gols=quantidade_gols)
        self.__dao_alunos.add(aluno)

    def excluir_aluno(self, matricula: int):
        # Recebe uma matricula, se a matricula estiver presente em um dos alunos da lista, remove ele da lista
        aluno = self.encontrar_aluno_por_matricula(matricula)
        if aluno != None:
            self.__dao_alunos.remove(matricula)
        return None
    
    def mostrar_aluno(self, aluno: Aluno):
        # Recebe um aluno, e encaminha os dados dele para a tela fazer a exibição
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
    
    def lista_alunos(self):
        retorno = []
        alunos = self.__dao_alunos.get_all()
        i = 0
        while i < len(alunos):
            aluno = alunos[i]
            nascimento = aluno.data_de_nascimento
            string_nascimento = str(nascimento["dia"]) + "/" + str(nascimento["mes"]) + "/" + str(nascimento["ano"])
            atual = [aluno.nome, aluno.cpf, aluno.curso.nome, string_nascimento, aluno.matricula, aluno.quantidade_gols]
            retorno.append(atual)

            i = i + 1
        return retorno

    def abrir_tela(self):
        # Inicia o menu de cadastro de alunos
        condicao = True
        while condicao:
            tela = self.__tela.tela_inicial(self.lista_alunos())
            opcao_tela = tela[0]

            # Inclui Aluno
            if opcao_tela == 2:
                lista_cursos = self.__controlador_sistema.controlador_curso.lista_cursos()
                dados = self.__tela.formulario_aluno(lista_cursos=lista_cursos)
                
                if dados != None:
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
