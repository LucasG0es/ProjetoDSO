

class TelaSistema:

    def tela_inicial(self):
        print()
        print("----- Menu Principal -----")
        print("Escolha uma opção")
        print("1 - Cadastro de Cursos")
        print("2 - Cadastro de Alunos")
        print("3 - Cadastro de Equipes")
        print("4 - Cadastro de Arbitros")
        print("5 - Menu de Campeonatos")
        print("0 - Encerrar")
        print()
        
        opcao = int(input("Escolha uma opção: "))
        while opcao < 0 or opcao > 5:
            opcao = int(input("Opção invalida, tente novamente ou aperte 0 para retornar: "))

        return opcao