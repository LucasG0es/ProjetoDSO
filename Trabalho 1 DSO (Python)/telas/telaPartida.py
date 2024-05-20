

class TelaPartida:

    def tela_inicial(self):
        print()
        print("----- Menu de Cursos -----")
        print("Escolha uma opção")
        print("1 - Listar Partidas")
        print("2 - Incluir Partida")
        print("3 - Editar Partida")
        print("4 - Excluir Partida")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def tela_partida(self):
        print("Escolha a alteração desejada")
        print("1 - Adicionar Gol")
        print("2 - Alterar Arbitro")
        print("3 - Incluir Equipe")
        print("4 - Remover Equipe")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def aguardar_input(self):
        input("Aperte enter para continuar ")
    
    def solicitar_input(self, nome_informacao):
        opcao = input(nome_informacao+": ")
        return opcao
    
    def mostrar_partida(self, dados: dict):
        equipes = dados["equipes"]
        placar = dados["placar"]
        resultado = dados["resultado"]
        arbitro = dados["arbitro"]
        codigo = dados["codigo"]

        print()
        print(f"Equipes: {equipes}")
        print(f"Placar: {placar}")
        print(f"Resultado: {resultado}")
        print(f"Arbitro: {arbitro}")
        print(f"Codigo: {codigo}")
        print()