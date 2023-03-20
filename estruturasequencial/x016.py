# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_metro_quadrado = float(input("Insira em metros quadrados da area a ser pintada: "))
litros_necessarios = (area_metro_quadrado/3)
latas_tinta = litros_necessarios/ 18
custo_total = latas_tinta * 80

print("Voce precisa comprar {:.2F} latas de tintas, e preço total da compra é R${:.2F}".format(latas_tinta, custo_total))
