from controladores.controladorCurso import ControladorCurso
from controladores.controladorEquipe import ControladorEquipe
from controladores.controladorAluno import ControladorAluno
from controladores.controladorArbitro import ControladorArbitro
from controladores.controladorCampeonato import ControladorCampeonato
from telas.telaSistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.controlador_curso = ControladorCurso(self)
        self.controlador_aluno = ControladorAluno(self)
        self.controlador_equipe = ControladorEquipe(self)
        self.controlador_arbitro = ControladorArbitro(self)
        self.controlador_campeonato = ControladorCampeonato(self)

        self.__tela = TelaSistema()
    
    def abrir_tela(self):
        # Inicia o sistema
        condicao = True
        while condicao:
            '''try:'''
            opcao_tela = self.__tela.tela_inicial()

            # Cadastro de Cursos
            if  opcao_tela == 1:
                self.controlador_curso.abrir_tela()

            if opcao_tela == 2:
                self.controlador_aluno.abrir_tela()
            
            # Cadastro de Equipes
            if  opcao_tela == 3:
                self.controlador_equipe.abrir_tela()
            
            if  opcao_tela == 4:
                self.controlador_arbitro.abrir_tela()
            
            if  opcao_tela == 5:
                self.controlador_campeonato.abrir_tela()

            # Encerra a tela
            elif opcao_tela == 0:
                condicao = False
            '''except Exception as error:
                print(f"\nOcorreu um erro inesperado, você foi direcionado para a tela principal.",
                      f"\nCaso o problema persista, contate um administrador.")
                print(error)'''