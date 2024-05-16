rendaMensal = float(input("Qual sua renda mensal?: "))
score = float(input("Qual seu score?: "))
fiadorscore = float(input("Qual é o score do fiador?: "))

if rendaMensal >= 2000 and score >= 600 or (fiadorscore >= 700):
    print("Você foi aprovado! Parabéns!!!!")
else:
    print("Você foi desaprovadinho :(")