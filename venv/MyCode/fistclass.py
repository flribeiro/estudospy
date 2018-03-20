__author__ = "Fabrício L. Ribeiro"


class MinhaClasse(object):
    num_instancias = 0

    def __init__(self, valor):
        self.__valor = valor
        MinhaClasse.num_instancias += 1


def function():
    pass


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


def teste():
    pass
