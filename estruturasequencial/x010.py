#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32
print("A temperatura de Celsius para Fahrenheit é {:.1F}°!".format(fahrenheit))