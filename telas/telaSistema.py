import PySimpleGUI as sg


class TelaSistema:

    def __init__(self):
        self.__window = None
    
    def tela_inicial(self):

        button_size = (25,1)

        layout = [
            [sg.T('Menu Principal', font='_ 14', justification='c', expand_x=True)],
            [sg.Text(text="", size = (0,2))],
            [sg.Button(button_text="Cursos", key=1, size=button_size)],
            [sg.Button(button_text="Alunos", key=2, size=button_size)],
            [sg.Button(button_text="Equipes", key=3, size=button_size)],
            [sg.Button(button_text="Arbitros", key=4, size=button_size)],
            [sg.Button(button_text="Campeonatos", key=5, size=button_size)]
        ]

        self.__window = sg.Window('Gerenciador de Campeonatos', element_justification="c", size=(600,600)).Layout(layout)

        button, values = self.__window.Read()
        self.__window.close()
        
        if button == None:
            return 0
        return button