#Aula 07 - Operadores Aritméticos

# '+' - Simbolo para Adição
# '-' - Simbolo para Subtração
# '*' - Simbolo para Multiplicação
# '/' - Simbolo para Divisão
# '**' - Simbolo para Potencia
# '//' - Simbolo para Divisão Inteira
# '%' - Simbolo para Resto da Divisão
# '==' - Simbolo para igualdade

#Ordem de precedência
# 1º- () - // Em python não se utiliza [] e nem {} para operadores matematicos
# 2º- **
# 3°- *, /, //, %
# 4°- +, -

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("a soma vale {}, o produto é {}, a divisão é {:.2f}".format(s, m, d))
print("Divisão é {} e a potencia é {}".format(di, e))