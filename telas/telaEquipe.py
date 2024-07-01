import PySimpleGUI as sg


class TelaEquipe:

    def __init__(self):
        self.__window = None
    
    def tela_inicial(self, data):

        button_size = (25,1)
        headings = ["Equipe", "Codigo"]

        layout = [
            [sg.T('Menu de Equipes', font='_ 14', justification='c', expand_x=True)],
            [sg.Text(text="", size = (0,2))],
            [sg.Table(values=data, headings=headings, max_col_width=40, expand_x=True, background_color='grey',
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='center',
                    num_rows=20,
                    key="Tabela")],
            [sg.Button(button_text="Editar Equipe", key=3, size=button_size), sg.Button(button_text="Excluir Equipe", key=4, size=button_size)],
            [sg.Text(text="", size = (0,2))],
            [sg.Button(button_text="Adicionar Equipe", key=2, size=button_size)],
            [sg.Button(button_text="Retornar", key=0, size=button_size)]
        ]

        self.__window = sg.Window('Gerenciador de Campeonatos', element_justification="c", size=(600,600)).Layout(layout)

        button, values = self.__window.Read()
        self.__window.close()
        
        if button == None:
            return [0]
        return [button, data[values["Tabela"][0]][1]]

    def tela_equipe(self):
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
    
    def formulario_equipe(self, nome="", codigo=""):

        texto_erro = [sg.Text(text="", size = (0,2))]

        while True:
            button_size = (25,1)
            titulo = "Adicionar uma Equipe"

            layout = [
                [sg.T(titulo, font='_ 14', justification='c', expand_x=True)],
                [sg.Text(text="", size = (0,2))],
                [sg.Text(text="Nome", size=(5,1)), sg.Input(key="Nome", default_text=nome, size=(30,1)), sg.Text(text="", size=(5,1))],
                [sg.Text(text="Codigo", size=(5,1)), sg.Input(key="Codigo", default_text=codigo, size=(30,1)), sg.Text(text="", size=(5,1))],
                texto_erro,
                [sg.Submit(),sg.Cancel()]
            ]

            self.__window = sg.Window(titulo, element_justification="c", size=(600,600)).Layout(layout)

            button, values = self.__window.Read()
            self.__window.close()
            
            if button == "Cancel":
                return
            try:
                values["Codigo"] = int(values["Codigo"])
                return values
            except:
                nome = values["Nome"]
                codigo = values["Codigo"]
                texto_erro = [sg.Text(text="", size=(5,1)),sg.Text(text="Código deve ser númerico", size=(30,1), justification="center", text_color="Red"), sg.Text(text="", size=(5,1))]
    
    def mostrar_equipe(self, dados: dict):
        nome = dados["nome"]
        curso = dados["curso"]
        codigo = dados["codigo"]

        print()
        print(f"Nome: {nome}")
        print(f"Curso: {curso}")
        print(f"Codigo: {codigo}")
        print()