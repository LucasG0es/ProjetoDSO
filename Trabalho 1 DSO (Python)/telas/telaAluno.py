

class TelaAluno:

    def tela_inicial(self):
        print()
        print("----- Menu de Alunos -----")
        print("Escolha uma opção")
        print("1 - Listar Alunos")
        print("2 - Incluir Aluno")
        print("3 - Editar Aluno")
        print("4 - Excluir Aluno")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao

    def tela_aluno(self):
        print()
        print("Escolha a alteração desejada")
        print("1 - Alterar Nome")
        print("2 - Alterar Curso")
        print("0 - Retornar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 2:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao
    
    def aguardar_input(self):
        input("Aperte enter para continuar ")

    def solicitar_input(self, nome_informacao):
        opcao = input(nome_informacao+": ")

        return opcao
    
    def mostrar_aluno(self, dados: dict):
        nome = dados["nome"]
        cpf = dados["cpf"]
        nascimento = dados["nascimento"]
        curso = dados["curso"]
        matricula = dados["matricula"]
        gols = dados["gols"]

        print()
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Data de Nascimento: {nascimento}")
        print(f"Curso: {curso}")
        print(f"Matrícula: {matricula}")
        print(f"Gols: {gols}")
        print()