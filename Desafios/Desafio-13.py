#Aula - 07 - Desafio

#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input("Qual o salario do funcionario? R$ "))
novo = salario + (salario*15/100)

print("O salario R$ {:.2f}, com o aumento de 15%, fica o novo salario de R$ {:.2f}".format(salario, novo))