import math


def areacirculo(raio):
    return (math.pi * (raio ** 2))


raio = float(input("Digite o raio do círculo: "))
print("Área do círculo: {}".format(areacirculo(raio)))