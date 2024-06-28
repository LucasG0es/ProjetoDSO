from classes.arbitro import Arbitro
from telas.telaArbitro import TelaArbitro


class ControladorArbitro:
    def __init__(self, controlador_sistema):
        self.__arbitros = []
        self.__tela = TelaArbitro()
        self.__controlador_sistema = controlador_sistema
        
    # Funções

    def encontrar_arbitro_por_cpf(self, cpf: int):
        # Recebe um CPF
        # Retorna um arbitro da lista com o CPF correspondente, ou retorna None
        i = 0
        arbitros = self.__arbitros
        while i < len(arbitros):
            arbitro = arbitros[i]
            if arbitro.cpf == cpf:
                return arbitro
        
            i = i + 1
        return None
    
    def incluir_arbitro(self, nome, cpf, dia, mes, ano):
        # Recebe dados para um novo arbitro
        # Caso o CPF já não esteja cadastrado, adiciona o arbitro na lista de arbitros
        if self.encontrar_arbitro_por_cpf(cpf) != None:
            return
        
        arbitro = Arbitro(nome=nome, cpf=cpf, dia=dia, mes=mes, ano=ano)
        self.__arbitros.append(arbitro)

    def excluir_arbitro(self, cpf: int):
        # Recebe um CPF de um arbitro
        # Caso exista um arbitro com CPF correspondente, remove ele da lista de arbitros
        arbitro = self.encontrar_arbitro_por_cpf(cpf)
        if arbitro != None:
            self.__arbitros.remove(arbitro)
            return arbitro
        return None
    
    def mostrar_arbitro(self, arbitro: Arbitro):
        # Recebe um arbitro, e encaminha os dados dele para a tela exibir
        if not isinstance(arbitro, Arbitro):
            return
        
        nascimento = arbitro.data_de_nascimento
        
        dados = {}
        dados['nome'] = arbitro.nome
        dados['cpf'] = arbitro.cpf
        dados['nascimento'] = str(nascimento["dia"]) + "/" + str(nascimento["mes"]) + "/" + str(nascimento["ano"])
        dados['partidas'] = arbitro.numero_de_partidas

        self.__tela.mostrar_arbitro(dados)
    
    def listar_arbitros(self):
        # Envia todos os alunos da lista de alunos para exibição
        arbitros = self.__arbitros
        i = 0
        while i < len(arbitros):
            self.mostrar_arbitro(arbitros[i])
            
            i = 1 + 1

    def alterar_arbitro(self):
        # Menu para escolher um arbitro, e alterar suas informações editaveis
        self.listar_arbitros()

        cpf = self.__tela.solicitar_input("CPF do Arbitro")
        arbitro = self.encontrar_arbitro_por_cpf(cpf)
        continua = cpf != 0 and arbitro != None
        
        if continua:
            condicao_tela_curso = True
            while condicao_tela_curso:
                self.mostrar_arbitro(arbitro)
                opcao = int(self.__tela.tela_arbitro())

                if opcao == 1:
                    nome = self.__tela.solicitar_input("Nome do Arbitro")
                    if nome != 0:
                        arbitro.nome = nome

                elif opcao == 0:
                    condicao_tela_curso = False
    
    def abrir_tela(self):
        # Inicia o menu de cadastro de arbitros
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()
            
            # Listar Arbitros
            if opcao_tela == 1:
                self.listar_arbitros()
                
                self.__tela.aguardar_input()
            
            # Inclui Arbitro
            if opcao_tela == 2:
                continua = True
                
                # Coleta input de um nome
                if continua:
                    nome = self.__tela.solicitar_input("Nome do Árbitro")
                    if nome == 0:
                        continua = False
                    
                # Coleta input de um CPF
                if continua:
                    cpf = int(self.__tela.solicitar_input("CPF do Árbitro"))
                    if cpf == 0:
                        continua = False
                
                # Coleta input da data de nascimento
                if continua:
                    dia = int(self.__tela.solicitar_input("Dia de Nascimento do Árbitro"))
                    if dia == 0:
                        continua = False
                
                if continua:
                    mes = int(self.__tela.solicitar_input("Mês de Nascimento do Árbitro"))
                    if mes == 0:
                        continua = False
                
                if continua:
                    ano = int(self.__tela.solicitar_input("Ano de Nascimento do Árbitro"))
                    if ano == 0:
                        continua = False
                
                if continua:
                    self.incluir_arbitro(nome, cpf, dia, mes, ano)
            
            # Altera Arbitro
            if opcao_tela == 3:
                self.alterar_arbitro()

            # Exclui Arbitro
            if opcao_tela == 4:
                self.listar_arbitros()
                
                # Coleta input de um CPF
                cpf = int(self.__tela.solicitar_input('CPF do Árbitro'))
                
                if cpf != 0:
                    self.excluir_arbitro(cpf=cpf)
            
            # Encerra a tela
            elif opcao_tela == 0:
                condicao = False
