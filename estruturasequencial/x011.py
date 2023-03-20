#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
primeiro = int(input("Digite primeiro numero: "))
segundo = int(input("Digite segundo numero: "))
terceiro = int(input("Digite terceiro numero: "))
equacao1 = (primeiro*2) * segundo/2
equacao2 = (primeiro*3) + terceiro
equacao3 = terceiro**3
print("- A mutiplicação do dobro {}  a metade de {} é {}!".format(primeiro,segundo,equacao1))
print("- A soma do triplo {} com {} é {}!".format(primeiro,terceiro,equacao2))
print("- {} elevado ao cubo é {}!".format(terceiro,equacao3))