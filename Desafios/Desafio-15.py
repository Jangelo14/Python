#Aula - 07 - Desafio

#Escreva um programa que pergunte a quantidade de Km percorrido por um carro aluga e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado
D = int(input("Quantos dias o carro foi alugado? "))
K = float(input("Quantos km foi utilizado? "))
pago = (D * 60) + (K * 0.15)
print("O total a ser pago é de R$ {:.2f}".format(pago))
