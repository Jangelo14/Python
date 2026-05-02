#Aula 06 - Desafios de Tipos Primitivos

#Crie um programa que leia o tipo primitivo e todas as informações possiveis sobre ela

n1 = input("digite algo:")
print("O tipo da variavel é: {}".format(type(n1))) # para descobrir o tipo primitivo
print("Elas estão em maiusculas? {}".format(n1.isupper())) #para saber se todas as letras estão maiusculas
print("Elas estão em minusculas? {}".format(n1.islower())) #para saber se todas as letras estão minusculas
print("É um numero? {}".format(n1.isnumeric())) #para saber se é um numero
print("É Aplhabetico? {}".format(n1.isalpha())) #para saber se é alfabético
print("É Alphanumerico? {}".format(n1.isalnum())) #para descobrir se é um alphanumerico
print("Só tem espaço? {}".format(n1.isspace())) #para saber se só possui espaço
print("Está Capitalizada? {}".format(n1.istitle())) #para saber se está iniciando em maiuscula e as demais em minusculas
