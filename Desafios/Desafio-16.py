#Aula 08 - Utilizando Modulo

#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex. Digite o numero 6.127, o numero tem a parte inteira 6
from math import trunc #Fazendo uma importação de um metodo especifico
num = float(input("Digite um valor: "))
print("o valor digitado foi {} e sua parte inteira é {}!".format(num, trunc(num)))