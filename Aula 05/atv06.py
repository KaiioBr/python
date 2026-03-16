# Pede para o usuário digitar os números separados por espaço
entrada1 = input("Digite os números da PRIMEIRA lista (separados por espaço): ")
entrada2 = input("Digite os números da SEGUNDA lista (separados por espaço): ")

# O .split() separa os números pelo espaço. 
# O comando 'int(x)' converte cada texto digitado para um número inteiro.
lista1 = [int(x) for x in entrada1.split()]
lista2 = [int(x) for x in entrada2.split()]

lista3 = [] # Lista final sem repetições

# Percorre a primeira lista
for item in lista1:
    if item not in lista3: 
        lista3.append(item)

# Percorre a segunda lista
for item in lista2:
    if item not in lista3: 
        lista3.append(item)

# Exibe os resultados
print("\n--- Resultado ---")
print(f"Lista 1 digitada: {lista1}")
print(f"Lista 2 digitada: {lista2}")
print(f"Lista 3 (sem repetições): {lista3}")