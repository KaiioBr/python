numeros = [] # Cria uma lista vazia

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero) # Adiciona o número digitado na lista

soma = sum(numeros) # Soma todos os itens da lista
media = soma / 5

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")