

bestseller = str(input("O livro é best seller? Responda com sim ou nao: "))
lançadoHa2Anos = str(input("O livro foi lançado há mais de 2 anos? Responda com sim ou não: "))
quantLivros = int(input("Quantos livros quer comprar? "))
preçoLivro = float(input("Qual o preço de cada livro?: "))
desconto = 0

if lançadoHa2Anos == "sim" or bestseller == "sim":
    desconto += 20
    if quantLivros > 3:
        desconto += 5
    precoFinal = preçoLivro * (1 - desconto / 100) * quantLivros
    print(f"0 preço final com descontos é de R$: {precoFinal: .2f}.")
else:
    print("sem descontos")