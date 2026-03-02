compras = []

while True:
    valor = float(input("Digite o valor do Produto: "))
    if(valor!=0):
        compras.append(valor)
    else:
        break

somatorio = sum(compras)
print(f"O valor total das compras e R$ {somatorio}")