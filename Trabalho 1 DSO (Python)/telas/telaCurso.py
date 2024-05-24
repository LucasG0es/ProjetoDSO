

class TelaCurso:

    def tela_inicial(self):
        print()
        print("----- Menu de Cursos -----")
        print("Escolha uma opção")
        print("1 - Listar Cursos")
        print("2 - Incluir Curso")
        print("3 - Editar Curso")
        print("4 - Excluir Curso")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = int(input("Opção invalida, tente novamente ou aperte 0 para retornar: "))

        return opcao
    
    def tela_curso(self):
        print()
        print("Escolha a alteração desejada")
        print("1 - Alterar Nome")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 1:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def aguardar_input(self):
        input("Aperte enter para continuar ")
    
    def informar_codigo(self):
        opcao = int(input("Código do Curso: "))
        while isinstance(opcao, str) and 0 == 1:
            opcao = input("O codigo do curso deve ser um número inteiro: ")

        return int(opcao)

    def informar_nome(self):
        opcao = input("Nome do Curso: ")

        return opcao
    
    def mostrar_curso(self, dados: dict):
        nome = dados["nome"]
        codigo = dados["codigo"]

        print()
        print(f"Nome: {nome}")
        print(f"Codigo: {codigo}")
        print()