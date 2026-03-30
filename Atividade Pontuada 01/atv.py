import os


# temperaturas = [22.5, 40.2, 18.0, 55.5, 30.1, 45.0]


# print("Lista de temperaturas:")
# for temperatura in temperaturas:
#     print(temperatura)


# print("-" * 20) 

# maior_temp = max(temperaturas)
# menor_temp = min(temperaturas)
# soma_temp = sum(temperaturas)
# qtd_leituras = len(temperaturas)

# print("Relatório do Sensor:")
# print(f"1. A maior temperatura registrada: {maior_temp}")
# print(f"2. A menor temperatura registrada: {menor_temp}")
# print(f"3. A soma de todas as temperaturas: {soma_temp}")
# print(f"4. A quantidade total de leituras: {qtd_leituras}")

# if os.name == 'nt':
#     os.system('cls')
# else:
#     os.system('clear')

# ferramentas = []

# print("=== Almoxarifado: Cadastro de Ferramentas ===")
# print("Instrução: Digite 'sair' quando quiser finalizar o cadastro.\n")

# while True:
#     nova_ferramenta = input("Digite o nome da ferramenta: ")
    

#     if nova_ferramenta.lower() == 'sair':
#         break
        
#     ferramentas.append(nova_ferramenta)


# print("\n" + "-" * 40)
# print("Lista completa de ferramentas cadastradas:")
# print(ferramentas)

import random

nomes = []

print("=== Sistema de Sorteio ===")

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes.sort()

print("\nLista de participantes (em ordem alfabética):")
for nome in nomes:
    print(f"- {nome}")

nome_sorteado = random.choice(nomes)


print("\n" + "=" * 30)
print(f"🎉 O nome sorteado foi: {nome_sorteado} 🎉")
print("=" * 30)