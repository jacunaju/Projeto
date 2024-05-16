while True:
    senha = input("digite uma senha forte com no minimo 8 caracteres e contendo numero")
    if len(senha) >= 8 and any(char.isdigit()for char in senha) and any(char.isalpha for char in senha):
        print("senha criada com sucesso")
        break
    else:
        print("sua senha  nao atende os requisitos")