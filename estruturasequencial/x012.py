# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Insira sua altura em metros: "))
print(altura)
peso_ideal = (72.7 * altura) - 58
print("O peso ideal com base na altura digitada é {:.2F}Kg".format(peso_ideal))