''' oxo_data é um módulo de dados para um jogo-da-velha. Ele salva e restaura o estado do jogo. Eis suas funções:
        saveGame(game) -> None
        restoreGame() -> game
    Observe que nenhum limite é imposto no tamanho dos dados. A implementação do jogo é responsável por validar todos os
    dados de entrada e/ou saída.'''

import os.path
game_file = '.oxogame.dat'

def _getPath():
    ''' getPath() -> string
    Retorna um caminho válido para o arquivo de dados.
    Tenta usar o caminho da pasta home do usuário, padrão é cwd'''

    try:
        game_path = os.environ['HOMEPATH'] or os.environ['HOME']
        if not os.path.exists(game_path):
            game_path = os.getcwd()
    except (KeyError, TypeError):
        game_path = os.getcwd()
    return game_path


def saveGame(game):
    ''' saveGame(game) -> None
    Salva um objeto game no arquivo de dados na pasta home do usuário. Nenhuma checagem é feita no input, que espera-se
    que seja uma lista de caracteres.'''

    path = os.path.join(_getPath(), game_file)
    with open(path, 'w') as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)


def restoreGame():
    ''' restoreGame() -> game
    Restaura um game a partir do arquivo de dados. O objeto game é uma lista de caracteres.'''

    path = os.path.join(_getPath(), game_file)
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)


def test():
    print('Path = ', _getPath())
    saveGame(list("XO  XO OX"))
    print(restoreGame())


if __name__ == "__main__": test()