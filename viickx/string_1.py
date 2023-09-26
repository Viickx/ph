nome = str(input("digite seu nome: "))
sobrenome = input("digite seu sobrenome: ")

print("\nTipo de variavel nome:", type(nome))
print("\nTipo de variavel sobrenome:", type(sobrenome))
print(f"\nnome e sobrenome: {nome} {sobrenome}")
print("\no numero de letras do nome é: ", len(nome))
print("\no numero de letras do sobrenome é: ", len(sobrenome))

print("A primeira letra do nome é: ", nome[0])
print("A ultima letra do nome é: ", nome[-1])

print("As 3 primeiras letras: ", nome[0:3])


