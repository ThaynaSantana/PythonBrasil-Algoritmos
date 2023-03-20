# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input("Insira sua altura: "))
sexo = str(input("Insira seu sexo, F ou M ? : ")).upper()
if sexo == "F":
  peso_ideal = (62.1 * altura) - 44.7
elif sexo == "M":
  peso_ideal = (72.7 * altura) - 58
else:
  print("Erro - Digite F ou M para inserir o sexo!")
  
print("Seu peso ideial é de {:.2F}Kg".format(peso_ideal))