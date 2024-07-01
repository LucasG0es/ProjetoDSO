from telas.tela import Tela
import PySimpleGUI as sg


class TelaAluno(Tela):
    
    def __init__(self):
        self.__window = None
    
    def tela_inicial(self, data):

        button_size = (25,1)
        headings = ["Aluno", "Matrícula"]

        layout = [
            [sg.T('Menu de Alunos', font='_ 14', justification='c', expand_x=True)],
            [sg.Text(text="", size = (0,2))],
            [sg.Table(values=data, headings=headings, max_col_width=40, expand_x=True, background_color='grey',
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='center',
                    num_rows=20,
                    key="Tabela")],
            [sg.Button(button_text="Editar Aluno", key=3, size=button_size), sg.Button(button_text="Excluir Aluno", key=4, size=button_size)],
            [sg.Text(text="", size = (0,2))],
            [sg.Button(button_text="Adicionar Aluno", key=2, size=button_size)],
            [sg.Button(button_text="Retornar", key=0, size=button_size)]
        ]

        self.__window = sg.Window('Gerenciador de Campeonatos', element_justification="c", size=(600,600)).Layout(layout)

        button, values = self.__window.Read()
        self.__window.close()
        
        if button == None:
            return [0]
        return [button, data[values["Tabela"][0]][1]]

    def tela_aluno(self):
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
    
    def formulario_aluno(self, nome="", matricula=""):

        texto_erro = [sg.Text(text="", size = (0,2))]

        while True:
            button_size = (25,1)
            titulo = "Adicionar um Aluno"

            layout = [
                [sg.T(titulo, font='_ 14', justification='c', expand_x=True)],
                [sg.Text(text="", size = (0,2))],
                [sg.Text(text="Nome", size=(5,1)), sg.Input(key="Nome", default_text=nome, size=(30,1)), sg.Text(text="", size=(5,1))],
                [sg.Text(text="Matrícula", size=(5,1)), sg.Input(key="Matrícula", default_text=matricula, size=(30,1)), sg.Text(text="", size=(5,1))],
                texto_erro,
                [sg.Submit(),sg.Cancel()]
            ]

            self.__window = sg.Window(titulo, element_justification="c", size=(600,600)).Layout(layout)

            button, values = self.__window.Read()
            self.__window.close()
            
            if button == "Cancel":
                return
            try:
                values["Matrícula"] = int(values["Matrícula"])
                return values
            except:
                nome = values["Nome"]
                matricula = values["Matrícula"]
                texto_erro = [sg.Text(text="", size=(5,1)),sg.Text(text="Código deve ser númerico", size=(30,1), justification="center", text_color="Red"), sg.Text(text="", size=(5,1))]
    
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