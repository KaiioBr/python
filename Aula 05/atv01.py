# Lê o peso dos peixes (permite números decimais)
peso = float(input("Digite o peso total dos peixes pescados (em kg): "))

# Variáveis com as regras do estado de São Paulo
limite_peso = 50.0
valor_multa_por_quilo = 4.00

# Verifica se o peso ultrapassou o limite
if peso > limite_peso:
    excesso = peso - limite_peso
    multa = excesso * valor_multa_por_quilo
else:
    excesso = 0.0
    multa = 0.00

# Exibe os resultados com as mensagens adequadas
print("\n--- Relatório de Pesca do João ---")
print(f"Peso total registrado: {peso:.2f} kg")
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Valor da multa a pagar: R$ {multa:.2f}")