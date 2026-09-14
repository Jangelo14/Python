#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas:
#O nome com todas as letras minusculas:
#Quantas letras ao todo (sem considerar os espaços):
#Quantas letras tem o primeiro nome:
nome = str(input("Digite seu nome completo: ")).strip()
print("Nome com todas as letras maiusculas: {}".format(nome.upper()))
print("Nome com todas as letras minusculas: {}".format(nome.lower()))
print("Quantidade de letras sem espaços: {}".format(len(nome.replace(" ", ""))))
print("Quantidade de letras sem espaços: {}".format(len(nome) - nome.count(" "))) #metodo alternativo
print("Quantidade de letras no primero nome: {}".format(len(nome.split()[0])))
print("Seu primeiro nome tem: {}".format(nome.find(' '))) #metodo alternativo