

class Tela:
    
    def aguardar_input(self):
        input("Pressione enter para continuar ")

    def solicitar_input(self, mensagem, tipo: type=str, valores_validos: list=[]):
        opcao = input(mensagem+": ")

        while True:
            try:
                if opcao == "0":
                    opcao = int(opcao)
                    break
                elif opcao == 0:
                    break

                if tipo == int:
                    opcao = int(opcao)
                if len(valores_validos) > 0 and opcao not in valores_validos:
                    raise Exception
                break
            except:
                opcao = input("Valor Inválido, tente novamente: ")

        return opcao