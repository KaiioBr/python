# Laco de Repeticao - FOR - While




# while True:
#     print("Migles")


# =====================================


# numero = 0

# while True:
#     numero +=1
#     print(f"Miglues - {numero}")


# =====================================


# nomes = ["Migles", "Kaio","Ana", "Edson", "Rui"]

# for andar in nomes:


# =====================================


numeros = []
for i in range(10):
    number = int(input(f"Digite o {i+1}° Numero: "))
    numeros.append(number)

media = sum(numeros)/len(numeros)
print(f"A media dos numeros doi de {media:.0f}")