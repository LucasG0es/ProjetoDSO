import PySimpleGUI as sg


class TelaCurso:

    def __init__(self):
        self.__window = None
    
    def tela_inicial(self):

        button_size = (25,1)

        layout = [
            [sg.T('Menu de Cursos', font='_ 14', justification='c', expand_x=True)],
            [sg.Text(text="", size = (0,2))],
            [sg.Button(button_text="Listar", key=1, size=button_size)],
            [sg.Button(button_text="Adicionar Curso", key=2, size=button_size)],
            [sg.Button(button_text="Editar Curso", key=3, size=button_size)],
            [sg.Button(button_text="Excluir Curso", key=4, size=button_size)],
            [sg.Button(button_text="Retornar", key=0, size=button_size)]
        ]

        self.__window = sg.Window('Gerenciador de Campeonatos', element_justification="c", size=(600,600)).Layout(layout)

        button, values = self.__window.Read()
        self.__window.close()
        
        if button == None:
            return 0
        return button

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
            return
        return values
    
    def mostrar_curso(self, dados: dict):
        nome = dados["nome"]
        codigo = dados["codigo"]

        print()
        print(f"Nome: {nome}")
        print(f"Codigo: {codigo}")
        print()