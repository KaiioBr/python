numeros = []
for i in range(5):
    temp = float(input(f"Digite uma temperatura: "))
    numeros.append(temp)
maiortemp = max(numeros)
menortemp = min(numeros)
media = sum(numeros)/len(numeros)
print(f"Maior temperatura obtida {maiortemp}° ")
print(f"Menor temperatura obtida {menortemp}° ")
print(f"A media das temperaturas foi {media:.1f}° ")