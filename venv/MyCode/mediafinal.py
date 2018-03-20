def calculamedia(bim1, bim2, bim3, bim4):
    soma = bim1 + bim2 + bim3 + bim4
    media = soma / 4
    return media


bim1 = float(input("Digite a nota do 1o. bimestre: "))
bim2 = float(input("Digite a nota do 2o. bimestre: "))
bim3 = float(input("Digite a nota do 3o. bimestre: "))
bim4 = float(input("Digite a nota do 4o. bimestre: "))
media = calculamedia(bim1, bim2, bim3, bim4)
print("Média final: {}".format(media))