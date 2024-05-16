ExpPython = int(input(f"Digite quantos anos tem de exp em python: "))
ExpMachine = int(input("Digite quantos anos tem de exp em Machine Learning: "))
diplomaMestrado = str(input("Possui diploma? Responda com sim ou não: "))

if ExpPython >= 3 and (ExpMachine >= 2 or diplomaMestrado == "sim"):
    print("Você foi aprovado")
else:
   print("Você não foi aprovado")
