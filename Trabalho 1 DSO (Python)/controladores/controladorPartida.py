from classes.partida import Partida
from classes.equipe import Equipe
from classes.arbitro import Arbitro
from telas.telaPartida import TelaPartida


class ControladorPartida:
    def __init__(self, controlador_sistema, campeonato):
        self.__partidas = []
        self.__tela = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__campeonato = campeonato

    @property
    def partidas(self):
        return self.__partidas
    
    def encontrar_partida_por_codigo(self, codigo: int):
        # Recebe um codigo
        # Retorna uma partida com o codigo informado se existir
        i = 0
        partidas = self.__partidas
        while i < len(partidas):
            partida = partidas[i]
            if partida.codigo == codigo:
                return partida

            i = i + 1
        return None

    def incluir_partida(self, codigo: int, arbitro: Arbitro):
        # Recebe dados para uma nova partida
        # Cria uma nova partida com os dados informados se o código já não estiver em uso
        if not (isinstance(arbitro, Arbitro) and isinstance(codigo, int)) or self.encontrar_partida_por_codigo(codigo) != None:
            return

        partida = Partida(codigo=codigo, arbitro=arbitro)
        self.__partidas.append(partida)
    
    def excluir_partida(self,codigo):
        # Recebe um codigo
        # Remove uma partida da lista com o codigo se essa partida existir
        partida = self.encontrar_partida_por_codigo(codigo)
        if partida != None:
            self.__partidas.remove(partida)

    def mostrar_partida(self,partida):
        # envia os dados de uma partida para a tela exibir
        if not isinstance(partida, Partida):
            return

        equipes = partida.equipes
        if len(equipes) == 0:
            nomes = "Indefinido"
            placar = "0 x 0"
        elif len(equipes) == 1:
            nomes = equipes[0].nome
            placar = "0 x 0"
        elif len(equipes) == 2:
            nomes = equipes[0].nome + " x " + equipes[1].nome
            placar = str(partida.gols[equipes[0]]) + " x " + str(partida.gols[equipes[1]])

        retorno_resultado = partida.calcula_resultado()
        if retorno_resultado == None:
            resultado = "Indefinido"
        elif len(retorno_resultado) > 1:
            resultado = "Empate"
        elif len(retorno_resultado) == 1:
            resultado = "Vitória "+retorno_resultado[0].nome


        dados = {}
        dados["equipes"] = nomes
        dados["placar"] = placar
        dados["resultado"] = resultado
        dados["arbitro"] = partida.arbitro.nome
        dados["codigo"] = partida.codigo

        self.__tela.mostrar_partida(dados)
        
    def listar_partidas(self, partidas = None):
        # Encaminha todas as equipes da lista para a exibição da tela
        if partidas == None:
            partidas = self.__partidas
            
        i = 0
        while i < len(partidas):
            self.mostrar_partida(partidas[i])

            i = i + 1
        
    def alterar_partida(self):
        # Acessa uma partida para editar
        self.listar_partidas()

        codigo = int(self.__tela.solicitar_input("Código da Partida"))
        partida = self.encontrar_partida_por_codigo(codigo)
        continua = codigo != 0 and partida != None
        
        if continua:           
            condicao_tela_equipe = True
            while condicao_tela_equipe:
                self.mostrar_partida(partida)
                opcao = int(self.__tela.tela_partida())

                if opcao == 1:
                    continua = True
                    controlador_equipe = self.__controlador_sistema.controlador_equipe
                    controlador_aluno = self.__controlador_sistema.controlador_aluno

                    if continua:
                        controlador_equipe.listar_equipes(partida.equipes)

                        codigo = int(self.__tela.solicitar_input("Codigo da Equipe"))
                        equipe = controlador_equipe.encontrar_equipe_por_codigo(codigo)
                        if codigo == 0 or equipe not in partida.equipes:
                            continua = False
                    
                    if continua:
                        controlador_equipe.listar_alunos_equipe(equipe)

                        matricula = int(self.__tela.solicitar_input("Matricula do Aluno que Marcou o Gol"))
                        aluno = controlador_aluno.encontrar_aluno_por_matricula(matricula)
                        if matricula == 0 or aluno not in equipe.alunos:
                            continua = False
                    
                    if continua:
                        partida.adicionar_gol(equipe=equipe, aluno=aluno)
                
                elif opcao == 2:
                    controlador_arbitro = self.__controlador_sistema.controlador_arbitro

                    controlador_arbitro.listar_arbitros()

                    codigo = int(self.__tela.solicitar_input("Codigo do Arbitro"))
                    arbitro = controlador_arbitro.encontrar_arbitro_por_codigo(codigo)
                    if codigo != 0:
                        partida.arbitro = arbitro
                
                elif opcao == 3:
                    controlador_equipe = self.__controlador_sistema.controlador_equipe
                    equipes_campeonato = self.__campeonato.equipes

                    controlador_equipe.listar_equipes(equipes_campeonato)

                    codigo = int(self.__tela.solicitar_input("Codigo da Equipe"))
                    equipe = controlador_equipe.encontrar_equipe_por_codigo(codigo)
                    if codigo != 0 and equipe in equipes_campeonato:
                        partida.incluir_equipe(equipe)
                
                elif opcao == 4:
                    controlador_equipe = self.__controlador_sistema.controlador_equipe

                    controlador_equipe.listar_equipes(partida.equipes)

                    codigo = int(self.__tela.solicitar_input("Codigo da Equipe"))
                    equipe = controlador_equipe.encontrar_equipe_por_codigo(codigo)
                    if codigo != 0:
                        partida.remover_equipe(equipe)
                
                elif opcao == 0:
                    condicao_tela_equipe = False
            
    def abrir_tela(self):
        # Inicia o menu de partidas
        condicao = True
        while condicao:
            opcao_tela = self.__tela.tela_inicial()

            # Listar Partidas
            if  opcao_tela == 1:
                self.listar_partidas()

                self.__tela.aguardar_input()

            # Incluir Partida
            if  opcao_tela == 2:

                codigo = int(self.__tela.solicitar_input("Código da Partida"))
                continua = codigo != 0

                if continua:
                    controlador_arbitro = self.__controlador_sistema.controlador_arbitro

                    controlador_arbitro.listar_arbitros()

                    cpf_arbitro = int(self.__tela.solicitar_input("CPF do Arbitro"))
                    arbitro = controlador_arbitro.encontrar_arbitro_por_cpf(cpf_arbitro)
                    continua = cpf_arbitro != 0

                if continua:
                    self.incluir_partida(codigo=codigo, arbitro=arbitro)

            # Acessar Partida
            if  opcao_tela == 3:
                self.alterar_partida()

            # Excluir Partida
            if  opcao_tela == 4:
                self.listar_partidas()

                codigo = int(self.__tela.solicitar_input("Código da Partida"))
                continua = codigo != 0

                if continua:
                    self.excluir_partida(codigo=codigo)

            # Retornar
            elif opcao_tela == 0:
                condicao = False