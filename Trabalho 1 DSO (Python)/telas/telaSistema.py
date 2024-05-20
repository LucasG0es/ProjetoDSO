

class TelaSistema:

    def tela_inicial(self):
        print()
        print("----- Menu de Cursos -----")
        print("Escolha uma opção")
        print("1 - Cadastro de Cursos")
        print("2 - Cadastro de Alunos")
        print("3 - Cadastro de Equipes")
        print("4 - Cadastro de Arbitros")
        print("0 - Encerrar")
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 4:
            opcao = input("Opção invalida, tente novamente ou aperte 0 para retornar: ")

        return opcao