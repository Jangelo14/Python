#Aula - 07 - Desafio

#Faça um programa que leia a largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²
larg = float(input("Informe a largura da parede: "))
alt = float(input("informe a altura da parede: "))
area = larg * alt
tinta = area / 2
print("Para pintar uma area de {}m², será necessário {} litros de tinta".format(area, tinta))