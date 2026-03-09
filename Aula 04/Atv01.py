lista = []
positivo = []
negativo = []
quantidadepositivo = 0
quantidadenegativo = 0

numero = 0

for numero in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)
    
    
    if (num > 0):
        positivo.append(num)
        quantidadepositivo += 1   
    else:
        negativo.append(num)
        quantidadenegativo += 1
        
somatorio = sum(positivo)
        
print(f"Números positivos: ", quantidadepositivo)
print(f"Números negativos: ", quantidadenegativo)
print(f"A soma dos numeros positivos:  {somatorio}")
print(f"Números negativos: ", negativo)