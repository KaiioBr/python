import os
import random
nomes = []

for x in range(10):
    n = input(f"Digite o {x+1}º nome: ")
    os.system("cls")
    nomes.append(n)
    
sortudo = random.choice(nomes)
print(f"O aluno sortudo foi: {sortudo}")