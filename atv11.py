# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input("digite uma quilometragem: "))
preco1 = km * 0.50
preco2 = km * 0.45
if km <= 200:
    print(f"o valor a ser pago é {preco1}")
else:
    print(f"o valor a ser pago é {preco2}")