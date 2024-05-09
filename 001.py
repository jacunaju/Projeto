gpa = float(input("Qual é sua nota no GPA?: "))
top10 = str(input("Você está no top 10% da sua turma? Responda com sim ou não: "))
trabVoluntario = int(input("Quantas horas de trabalho voluntario você tem?: "))

if gpa >= 3.5 or (top10 == "sim" or trabVoluntario >= 100):
    print("voce foi aprovado!!!!!!!")
else:
    print("voce foi reprovado :(")