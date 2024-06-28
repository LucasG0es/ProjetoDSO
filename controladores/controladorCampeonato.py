from telas.telaCampeonato import TelaCampeonato
from classes.campeonato import Campeonato
from classes.equipe import Equipe


class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        self.__campeonatos = []
        self.__tela = TelaCampeonato()
        self.__controlador_sistema = controlador_sistema
    
    # Getters
    @property
    def campeonatos(self):
        return self.__campeonatos

    # Funções
    def encontrar_campeonato_por_codigo(self, codigo: int):
        # Recebe um código, e retorna um campeonato com o codigo correspondente se existir
        i = 0
        campeonatos = self.__campeonatos
        while i < len(campeonatos):
            campeonato = campeonatos[i]
            if campeonato.codigo == codigo:
                return campeonato

            i = i + 1
        return None

    def incluir_campeonato(self, nome: str, codigo: int):
        # Recebe dados para um novo campeonato e caso o código já não esteja em uso, adiciona ele na lista de campeonatos
        if not (isinstance(codigo, int) and isinstance(nome, str)) or self.encontrar_campeonato_por_codigo(codigo) != None:
            return

        campeonato = Campeonato(nome=nome, codigo=codigo, controlador_sistema=self.__controlador_sistema)
        self.__campeonatos.append(campeonato)
    
    def excluir_campeonato(self, codigo: int):
        # Recebe um codigo de campeonato e caso exista um campeonato com o codigo correspondente, remove ele da lista
        campeonato = self.encontrar_campeonato_por_codigo(codigo)
        if campeonato != None:
            self.__campeonatos.remove(campeonato)
        
    def mostrar_campeonato(self, campeonato):
        # Encaminha dados de um campeonato para a exibição da tela
        if not isinstance(campeonato, Campeonato):
            return

        dados = {}
        dados["nome"] = campeonato.nome
        dados["codigo"] = campeonato.codigo

        self.__tela.mostrar_campeonato(dados)
    
    def mostrar_equipe_campeonato(self, equipe: Equipe, campeonato: Campeonato):
        # Encaminha dados de uma equipe para exibição da tela
        if not (isinstance(equipe, Equipe) and isinstance(campeonato, Campeonato)):
            return

        dados = {}
        dados["nome"] = equipe.nome
        dados["curso"] = equipe.curso.nome
        dados["pontuacao"] = campeonato.pontuacao_equipe(equipe)
        dados["saldo gols"] = campeonato.saldo_gols_equipe(equipe)
        dados["gols tomados"] = campeonato.gols_tomados_equipe(equipe)
              
        self.__tela.mostrar_equipe_campeonato(dados)
    
    def listar_campeonatos(self):
        # Chama a função de exibir campeonato, para cada campeonato na lista
        campeonatos = self.__campeonatos
        i = 0
        while i < len(campeonatos):
            self.mostrar_campeonato(campeonatos[i])

            i = i + 1
        
    def exibir_placar(self, campeonato: Campeonato):
        # Exibe as equipes no campeonato, ordenadas pela quantidade de pontos
        equipes = campeonato.equipes_ordenadas()
        i = 0
        while i < len(equipes):
            self.mostrar_equipe_campeonato(campeonato=campeonato, equipe=equipes[i])
            i = i + 1
    
    def exibir_historico_partidas(self, campeonato: Campeonato):
        # Exibe as partidas do campeonato, ordenadas da mais nova para a mais antiga
        controlador_partida = campeonato.controlador_partida
        partidas_nova = []
        i = 0
        while i < len(controlador_partida.partidas):
            partidas_nova.append(controlador_partida.partidas[i])
            i = i + 1

        controlador_partida.listar_partidas(partidas_nova.sort(reverse=True))
        
    def alterar_equipes_campeonato(self, campeonato: Campeonato):
        # Inicia uma tela para editar as equipes do campeonato
        if not isinstance(campeonato, Campeonato):
            return

        condicao_tela = True
        while condicao_tela:
            controlador_equipe = self.__controlador_sistema.controlador_equipe
            opcao = int(self.__tela.tela_equipes())

            if opcao == 1:
                controlador_equipe.listar_equipes(campeonato.equipes)

                self.__tela.aguardar_input()
            
            if opcao == 2:
                controlador_equipe.listar_equipes()

                codigo = int(self.__tela.solicitar_input("Codigo da Equipe"))
                equipe = controlador_equipe.encontrar_equipe_por_codigo(codigo)
                if codigo != 0:
                    campeonato.incluir_equipe(equipe)
            
            if opcao == 3:
                controlador_equipe.listar_equipes(campeonato.equipes)

                codigo = int(self.__tela.solicitar_input("Codigo da Equipe"))
                equipe = controlador_equipe.encontrar_equipe_por_codigo(codigo)
                if codigo != 0:
                    campeonato.remover_equipe(equipe)
            
            if opcao == 0:
                condicao_tela = False
    
    def alterar_campeonato(self):
        # Inicia uma tela para acessar um campeonato
        self.listar_campeonatos()

        codigo = int(self.__tela.solicitar_input("Código do Campeonato"))
        campeonato = self.encontrar_campeonato_por_codigo(codigo)
        continua = codigo != 0 and campeonato != None

        if continua:
            condicao_tela = True
            while condicao_tela:
                self.mostrar_campeonato(campeonato)
                opcao = int(self.__tela.tela_campeonato())

                if opcao == 1:
                    self.exibir_placar(campeonato)

                    self.__tela.aguardar_input()
                
                elif opcao == 2:
                    self.exibir_historico_partidas(campeonato)

                    self.__tela.aguardar_input()
                
                elif opcao == 3:
                    self.alterar_equipes_campeonato(campeonato)
                
                elif opcao == 4:
                    campeonato.controlador_partida.abrir_tela()
                
                elif opcao == 0:
                    condicao_tela = False
    
    def abrir_tela(self):
        # Inicia o menu de campeonatos
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # Lista os campeonatos
            if opcao_tela == 1:
                self.listar_campeonatos()

                self.__tela.aguardar_input()
            
            # Inclui um novo campeonato
            if opcao_tela == 2:
                codigo = int(self.__tela.solicitar_input("Código do Campeonato"))
                continua = codigo != 0

                if continua:
                    nome = self.__tela.solicitar_input("Nome do Campeonato")
                    continua = nome != 0
                
                if continua:
                    self.incluir_campeonato(nome, codigo)
            
            # Acessa um campeonato
            if opcao_tela == 3:
                self.alterar_campeonato()
            
            # Remove um campeonato
            if opcao_tela == 4:
                codigo = int(self.__tela.solicitar_input("Código do Campeonato"))
                continua = codigo != 0

                if continua:
                    self.excluir_campeonato(codigo)
            
            # Retorna
            if opcao_tela == 0:
                condicao = False