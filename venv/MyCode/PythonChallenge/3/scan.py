import sys
import re


def verificaMatch(m):
    padrao = r"[a-z]{1}([A-Z]{3}[a-z]{1}[A-Z]{3})[a-z]{1}"
    encontrado = re.match(padrao, m)
    return encontrado

if __name__ == "__main__":
    resultados = list()
    with open('equality.txt', 'r') as f:
        for line in f:
            r = verificaMatch(line)
            if r:
                resultados.append(r)

    for r in resultados:
        print(r.groups())
