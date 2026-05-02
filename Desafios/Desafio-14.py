#Aula - 07 - Desafio

#Faça um programa que converta a temperatura de ºC para °F
C = float(input("Informe a temperatura em Cº: "))
F = ((9*C)/5)+32 #Usando a regra de precedencia, não ha necessidade de usar os parenteses
print("A temperatura em {}°C, ao ser convertido, fica {}°F!".format(C,F))