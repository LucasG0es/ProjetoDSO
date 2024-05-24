

class TelaCampeonato:

    def tela_inicial(self):
        print()
        print("----- Menu de Campeonatos -----")
        print("Escolha uma opção")
        print("1 - Listar Campeonatos")
        print("2 - Incluir Campeonato")
        print("3 - Acessar Campeonato")
        print("4 - Excluir Campeonato")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def tela_campeonato(self):
        print()
        print("Escolha a opção desejada")
        print("1 - Placar das Equipes")
        print("2 - Histórico de Partidas")
        print("3 - Acessar Equipes")
        print("4 - Acessar Partidas")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao

    def tela_equipes(self):
        print()
        print("----- Menu de Equipes do Campeonato -----")
        print("1 - Listar Equipes")
        print("2 - Incluir Equipe")
        print("3 - Remover Equipe")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def aguardar_input(self):
        input("Aperte enter para continuar ")
    
    def solicitar_input(self, nome_informacao):
        opcao = input(nome_informacao+": ")
        return opcao
    
    def mostrar_campeonato(self, dados: dict):
        nome = dados["nome"]
        codigo = dados["codigo"]

        print()
        print(f"Equipes: {nome}")
        print(f"Codigo: {codigo}")
        print()
    
    def mostrar_equipe_campeonato(self, dados: dict):
        nome = dados["nome"]
        curso = dados["curso"]
        pontuacao = dados["pontuacao"]
        saldo_gols = dados["saldo gols"]
        gols_tomados = dados["gols tomados"]


        print()
        print(f"Equipe: {nome}")
        print(f"Curso: {curso}")
        print(f"Pontos: {pontuacao}")
        print(f"Saldo de Gols: {saldo_gols}")
        print(f"Gols Tomados: {gols_tomados}")
        print()