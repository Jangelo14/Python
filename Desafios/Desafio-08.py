#Aula - 07 - Desafio

#Escreva um programa que leia o valor em metros e exiba o valor convertido em cm e mm

m = float(input("Insira o a distancia em metros: "))

cm = m * 100

mm = m * 1000

print("A distancia em metros é {}m, em centimentos é {}cm e em milimetros é {}mm.".format(m, cm, mm))