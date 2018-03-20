""" CLI User Interface para o jogo-da-velha.
    Usado como programa principal, sem funções reutilizáveis.
"""

import oxo_logic


menu = ["Iniciar um novo jogo",
        "Continuar jogo salvo",
        "Mostrar ajuda",
        "Sair"]


def getMenuChoice(aMenu):
    """ getMenuChoice(aMenu) -> int
        Recebe como input uma lista de strings, mostra como um menu numerado
        e itera até que o usuário selecione um número válido."""

    if not aMenu: raise ValueError('Nenhum conteúdo de menu')
    while True:
        print("\n\n")
        for index, item in enumerate(aMenu, start=1):
            print(index, "\t", item)

        try:
            choice = int(input("\nEscolha uma opção: "))
            if 1 <= choice <= len(aMenu):
                return choice
            else:
                print("Escolha um número entre 1 e ", len(aMenu))
        except ValueError:
            print("Escolha o número de alguma das opções do menu.")


def startGame():
    return oxo_logic.newGame()


def resumeGame():
    return oxo_logic.restoreGame()


def displayHelp():
    print('''
    Iniciar um novo jogo: inicia um novo jogo-da-velha
    Continuar jogo salvo: recupera o último jogo salvo e continua
    Mostrar ajuda: mostra esta página
    Sair: sai da aplicação''')


def quit():
    print("Até logo...")
    raise SystemExit

def executeChoice(choice):
    ''' executeChoice(int) -> None

    Executa a opção escolhida pelo usuário. Se a escolha produz um jogo válido
    então o jogo começa e continua até completar.'''

    dispatch = [startGame, resumeGame, displayHelp, quit]
    game = dispatch[choice-1]()
    if game:
        playGame(game)


def printGame(game):
    display = '''
     1 | 2 | 3        {} | {} | {} 
    -----------      ------------ 
     4 | 5 | 6        {} | {} | {} 
    -----------      ------------
     7 | 8 | 9        {} | {} | {} '''
    print(display.format(*game))


def playGame(game):
    result = ""
    while not result:
        printGame(game)
        choice = input("Quadrante [1-9 ou s para sair]: ")
        if choice.lower()[0] == 's':
            save = input("Salvar o jogo antes de sair? [s/n] ")
            if save.lower()[0] == 's':
                oxo_logic.saveGame(game)
            quit()
        else:
            try:
                cell = int(choice)-1
                if not (0 <= cell <= 8):
                    raise ValueError
            except ValueError:
                print("Escolha um número entre 1 e 9 ou 's' para sair.")
                continue

            try:
                result = oxo_logic.userMove(game, cell)
            except ValueError:
                print("Escolha um quadrante vazio.")
                continue

            if not result:
                result = oxo_logic.computerMove(game)
            if not result:
                continue
            elif result == 'D':
                printGame(game)
                print("Deu empate.")
            else:
                printGame(game)
                print("O vencedor foi ", result, "\n")

def main():
    while True:
        choice = getMenuChoice(menu)
        executeChoice(choice)


if __name__ == "__main__": main()