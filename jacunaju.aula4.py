portfolioForte = str(input("seu portifolio é forte? responda com sim ou nao: "))
audicaoExcelente = str(input("qual a navaliaçao da sua audiçao? (excelente, boa, mediana, ruim): "))
AnosTreinamento = int(input("quantos anos de treinamento?: "))

if portfolioForte == "sim" or (audicaoExcelente == "excelente" and AnosTreinamento >= 2):
    print("voce foi admitido")
else:
    print("voce nao foi admitido")