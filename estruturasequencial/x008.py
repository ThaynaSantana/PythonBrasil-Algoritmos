# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
dinheiro_porhora = float(input("Quanto voce ganha por hora? : "))
horas_trabalhadas = int(input("Quantas horas voce trabalhou no mês? : "))
salario = (horas_trabalhadas/24) * (dinheiro_porhora*24)
print("Seu salario referencia ao que voce trabalhou no mes é R${:.2F}!".format(salario))