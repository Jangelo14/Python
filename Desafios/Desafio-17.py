#Aula 08 - Utilizando Modulo

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input("Qual o valor do cateto oposto? "))
ca = float(input("Qual o valor do cato adjacente? "))

#Resolvendo sem utilizar o modulo
#hi = (co ** 2 + ca ** 2) ** (1/2)

#print("O valor da hipotenusa vai ser {:.2f}".format(co, ca, hi))

#Resolvendo utilizando o modulo
hi = hypot(co, ca)
print("O valor da hipotenusa vai ser {:.2f}".format(hi))