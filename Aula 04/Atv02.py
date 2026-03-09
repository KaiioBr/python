import random

nomes = []
no = 0
for no in range(10):
    identidas = str(input("Digite um nome: "))
    nomes.append(identidas)

sorte = random.choice(nomes)
print(f"O melhor rap geek é : {sorte}")