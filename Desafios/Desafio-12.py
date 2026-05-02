#Aula - 07 - Desafio

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input("Qual e o preço do produto? R$ "))
novo = preco - (preco*5/100)

print("O produto que custava R$ {:.2f}, irá custar R$ {:.2f}, após receber 5% de desconto".format(preco, novo))