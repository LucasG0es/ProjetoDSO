from telas.tela import Tela
import PySimpleGUI as sg


class TelaAluno(Tela):
    
    def __init__(self):
        self.__window = None
    
    def tela_inicial(self, data):

        button_size = (25,1)
        headings = ["Aluno","CPF", "Curso", "Nascimento", "Matrícula", "Gols"]

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
        
        if len(values["Tabela"]) > 0:
            return [button, data[values["Tabela"][0]][1]]
        else:
            return [button]
    
    def formulario_aluno(self, lista_cursos, nome="", cpf="", dia="", mes="", ano="", curso="", matricula=""):
        
        edit_form = cpf != ""

        texto_erro = ""

        while True:
            button_size = (25,1)
            titulo = "Adicionar Aluno"
            if edit_form:
                titulo = "Editar Aluno"

            layout = [
                [sg.T(titulo, font='_ 14', justification='c', expand_x=True)],
                [sg.Text(text="", size = (0,2))],
                [sg.Text(text="Nome", size=(15,1), justification="r"), 
                    sg.Input(key="Nome", default_text=nome, size=(30,1)), 
                    sg.Text(text="", size=(15,1))],
                [sg.Text(text="CPF", size=(15,1), justification="r"),
                    sg.Input(key="CPF", disabled=edit_form, disabled_readonly_background_color="darkgrey", default_text=cpf, size=(30,1)),
                    sg.Text(text="", size=(15,1))],
                [sg.Text(text="Matricula", size=(15,1), justification="r"),
                    sg.Input(key="Matricula", disabled=edit_form, disabled_readonly_background_color="darkgrey", default_text=matricula, size=(30,1)),
                    sg.Text(text="", size=(15,1))],
                [sg.Text(text="Data de Nascimento", size=(15,1)),
                    sg.Input(key="Dia", disabled=edit_form, disabled_readonly_background_color="darkgrey", default_text=dia, size=(2,1)),
                    sg.Input(key="Mês", disabled=edit_form, disabled_readonly_background_color="darkgrey", default_text=mes, size=(2,1)),
                    sg.Input(key="Ano", disabled=edit_form, disabled_readonly_background_color="darkgrey", default_text=ano, size=(4,1)),
                    sg.Text(text="", size=(30,1))],
                [sg.Table(values=lista_cursos, headings=["Curso"], max_col_width=40, background_color='grey', col_widths=30,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='center',
                    num_rows=10,
                    key="Curso")],
                [sg.Text(text="", size=(15,1)),sg.Text(text=texto_erro, size=(30,1), justification="center", text_color="Red"), sg.Text(text="", size=(15,1))],
                [sg.Submit(),sg.Cancel()]
            ]

            self.__window = sg.Window(titulo, element_justification="c", size=(600,600)).Layout(layout)

            button, values = self.__window.Read()
            self.__window.close()
            
            # Retornar
            if button == "Cancel" or button == None:
                return