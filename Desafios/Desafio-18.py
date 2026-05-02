#Aula 08 - Utilizando Modulo

#Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
ang = float(input("Digite o valor do angulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print("o angulo de {:.2f}º, tem seu seno de {:.2f}, o cosseno de {:.2f} e sua tangente é {:.2f}".format(ang, sen, cos, tan))