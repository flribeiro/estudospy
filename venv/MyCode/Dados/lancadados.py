import time
import sys
from random import randint

def lancadados(lancamentos):
    starttime = time.time()
    results = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }

    count = 0

    while count <= lancamentos:
        dado = randint(1, 6)
        results[str(dado)] += 1
        count += 1

    print("Duração: {}s".format(time.time() - starttime))
    return results

if __name__ == "__main__":
    qtdlancamentos = int(sys.argv[1])
    result = lancadados(qtdlancamentos)
    print(result)
    
