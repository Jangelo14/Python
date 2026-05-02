#Aula - 07 - Desafio

#crie um programa que leia um numero e mostre seu dobro, seu triplo e sua raiz quadrada

n = int(input("digite um numero: "))

d = n * 2

t = n * 3

r = n ** (1/2)

print("O dobro do numero é {}.\n seu triplo é {}\n E sua raiz quadrada é {:.2f}".format(d, t, r))