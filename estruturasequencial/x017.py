# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area_metro_quadrado = float(input("Insira em metros quadrados da area a ser pintada: "))
litros_necessarios = area_metro_quadrado / 6
latas_tinta_18 = litros_necessarios / 18
latas_tinta_3e6 = litros_necessarios / 3.6
sobra = 0
# Menor que 18L, fica mais barato comprar galoes de 3.6 litros
if litros_necessarios < 18:
    latas_economicas = litros_necessarios / 3.6
# Maior que 18L, fica mais barato comprar as latas de tintas 18 litros
elif litros_necessarios >= 18:
    if litros_necessarios % 18 == 0:
        latas_economicas = litros_necessarios / 18
    else:
        latas_economicas = litros_necessarios / 18
        sobra = (litros_necessarios % 18) / 3.6

# Resultado
print("""
- Quantidade de tinta a ser comprada: {:.0F}L
- Temos 3 situações para comprar a quantidade de tinta necessaria
1. Comprar apenas latas de 18 litros: > {:.0F} latas
2. Comprar apenas galões de 3,6 litros: > {:.0F} galões
3. Misturar latas de 18 litros e galões de 3,6 litros:
    Para {:.0F}L de tintas, precisa comprar:
    Latas 18L > {:.0F} latas
    Galões 3,6L > {:.0F} galões
""".format(litros_necessarios, latas_tinta_18, latas_tinta_3e6, litros_necessarios, latas_economicas, sobra))