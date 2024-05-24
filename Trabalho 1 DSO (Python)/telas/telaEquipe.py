

class TelaEquipe:

    def tela_inicial(self):
        print()
        print("----- Menu de Equipes -----")
        print("Escolha uma opção")
        print("1 - Listar Equipes")
        print("2 - Incluir Equipe")
        print("3 - Editar Equipe")
        print("4 - Excluir Equipe")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = int(input("Opção invalida, tente novamente ou aperte 0 para retornar: "))

        return opcao
    
    def tela_equipe(self):
        print()
        print("Escolha a alteração desejada")
        print("1 - Alterar Nome")
        print("2 - Alterar Curso")
        print("3 - Incluir Aluno")
        print("4 - Remover Aluno")
        print("5 - Listar Alunos")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 5:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def aguardar_input(self):
        input("Aperte enter para continuar ")
    
    def solicitar_input(self, nome_informacao):
        opcao = input(nome_informacao+": ")
        return opcao
    
    def mostrar_equipe(self, dados: dict):
        nome = dados["nome"]
        curso = dados["curso"]
        codigo = dados["codigo"]

        print()
        print(f"Nome: {nome}")
        print(f"Curso: {curso}")
        print(f"Codigo: {codigo}")
        print()