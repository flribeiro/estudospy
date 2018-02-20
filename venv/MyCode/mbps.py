def calculatempo(t, v):
    t = t * 8
    v = v * 60
    tem = t / v
    return tem


def main():
    tamarquivo = float(input("Digite o tamanho do arquivo em MB: "))
    vellink = float(input("Digite a velocidade do link em Mbps: "))
    tdown = calculatempo(tamarquivo, vellink)
    print("O download levará cerca de {} minutos.".format(tdown))


if __name__ == "__main__":
    main()