import PySimpleGUI as sg


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
    
    def criar_curso(self):
        
        button_size = (25,1)
        titulo = "Adicionar um Curso"

        layout = [
            [sg.T(titulo, font='_ 14', justification='c', expand_x=True)],
            [sg.Text(text="", size = (0,2))],
            [sg.Text(text="Nome", size=(5,1)), sg.Input(key="Nome", size=(30,1)), sg.Text(text="", size=(5,1))],
            [sg.Text(text="Codigo", size=(5,1)), sg.Input(key="Codigo", size=(30,1)), sg.Text(text="", size=(5,1))],
            [sg.Text(text="", size = (0,2))],
            [sg.Submit(),sg.Cancel()]
        ]

        self.__window = sg.Window(titulo, element_justification="c", size=(600,600)).Layout(layout)

        button, values = self.__window.Read()
        self.__window.close()
        
        if button == "Cancel":
            return 0
        return values
    
    def mostrar_curso(self, dados: dict):
        nome = dados["nome"]
        codigo = dados["codigo"]

        print()
        print(f"Nome: {nome}")
        print(f"Codigo: {codigo}")
        print()