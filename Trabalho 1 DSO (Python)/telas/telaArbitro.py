

class TelaArbitro:

    def tela_inicial(self):
        print("----- Menu de Arbitro -----")
        print("Escolha uma opção")
        print("1 - Listar Arbitros")
        print("2 - Incluir Arbitro")
        print("3 - Alterar Arbitro")
        print("4 - Excluir Arbitro")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def tela_arbitro(self):
        print("Escolha a alteração desejada")
        print("1 - Alterar Nome")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 1:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def aguardar_input(self):
        input("Aperte enter para continuar ")

    def solicitar_input(self, nome_informacao):
        opcao = input(nome_informacao+": ")

        return opcao
    
    def mostrar_arbitro(self, dados: dict):
        nome = dados["nome"]
        cpf = dados["cpf"]
        nascimento = dados["nascimento"]
        partidas = dados["partidas"]

        print()
        print(f"Nome: {nome}")
        print(f"cpf: {cpf}")
        print(f"Data de Nascimento: {nascimento}")
        print(f"Número de partidas: {partidas}")
        print()
