valor_dia = 60
valor_km = 0.15

km = int(input("Digite a distância em quilômetros: "))
dia = int(input("Digite a quantidade de dias alugado: "))

preco_dia = valor_dia * dia
preco_km = valor_km * km

preco_total = preco_dia + preco_km

print(f"O valor a pagar pelo aluguel do carro foi de: {preco_total:.2f} reais")