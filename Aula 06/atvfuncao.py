import os

def verificar_par_impar(numero):
    if  numero % 2 == 0:
        return "par"
    else:
        return "Impar"
    
# Exemplo de uso
num = int(input("Digite um numero: "))
resultado = verificar_par_impar(num)
print(f"O numero {num} e {resultado}")
