import os

positivos = []
negativos = []

for x in range(10):
    valor = int(input("Digite um número: "))
    os.system("cls") 
    if(valor>=0):
        positivos.append(valor)
    else:
        negativos.append(valor)
        
qpositivo = len(positivos)
qnegativos = len(negativos)
print(f"Quantidade de números positivos: {qpositivo}")
print(f"Quantidade de números negativos: {qnegativos}")
soma = sum(positivos)
print(f"Soma dos números positivos: {soma}")