somatorio = 0

while True:
    num = int(input("Digite um número: "))
    
    if num == 0:
        break
    
    somatorio += num  # Acumula o valor de num em somatorio
    
print(f"A soma dos números digitados é: {somatorio}")