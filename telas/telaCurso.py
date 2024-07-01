import PySimpleGUI as sg

class NomeGrande(Exception):
    pass

class NomePequeno(Exception):
    pass

class TelaCurso:

    def __init__(self):
        self.__window = None
    
    def tela_inicial(self, data):

        button_size = (25,1)
        headings = ["Curso", "Codigo"]

        layout = [
            [sg.T('Menu de Cursos', font='_ 14', justification='c', expand_x=True)],
            [sg.Text(text="", size = (0,2))],
            [sg.Table(values=data, headings=headings, max_col_width=40, expand_x=True, background_color='grey',
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='center',
                    num_rows=20,
                    key="Tabela")],
            [sg.Button(button_text="Editar Curso", key=3, size=button_size), sg.Button(button_text="Excluir Curso", key=4, size=button_size)],
            [sg.Text(text="", size = (0,2))],
            [sg.Button(button_text="Adicionar Curso", key=2, size=button_size)],
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
    
    def formulario_curso(self, nome="", codigo=""):
        
        edit_form = codigo != ""

        texto_erro = ""

        while True:
            button_size = (25,1)
            titulo = "Adicionar Curso"
            if edit_form:
                titulo = "Editar Curso"

            layout = [
                [sg.T(titulo, font='_ 14', justification='c', expand_x=True)],
                [sg.Text(text="", size = (0,2))],
                [sg.Text(text="Nome", size=(5,1)), sg.Input(key="Nome", default_text=nome, size=(30,1)), sg.Text(text="", size=(5,1))],
                [sg.Text(text="Codigo", size=(5,1)), sg.Input(key="Codigo", disabled=edit_form, disabled_readonly_background_color="darkgrey", default_text=codigo, size=(30,1)), sg.Text(text="", size=(5,1))],
                [sg.Text(text="", size=(5,1)),sg.Text(text=texto_erro, size=(30,1), justification="center", text_color="Red"), sg.Text(text="", size=(5,1))],
                [sg.Submit(),sg.Cancel()]
            ]

            self.__window = sg.Window(titulo, element_justification="c", size=(600,600)).Layout(layout)

            button, values = self.__window.Read()
            self.__window.close()
            
            # Retornar
            if button == "Cancel" or button == None:
                return
            
            # Retorno de valores
            try:
                if len(values["Nome"]) > 20:
                    raise NomeGrande()
                
                if len(values["Nome"]) < 5:
                    raise NomePequeno()
                
                values["Codigo"] = int(values["Codigo"])
                return values
            
            except NomeGrande:
                texto_erro = "Nome deve ter no máximo 20 carácteres"
            except NomePequeno:
                texto_erro = "Nome deve ter no mínimo 5 carácteres"
            except ValueError:
                texto_erro = "Código deve ser númerico"
            
            finally:
                nome = values["Nome"]
                codigo = values["Codigo"]