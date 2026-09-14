#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input("qual seu nome? ")).strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper())) #utilizando o operador "in" para verificar se dentro da string, possui determinada palavra