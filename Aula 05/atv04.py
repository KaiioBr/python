# Recebe os dois números inteiros do usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Identifica qual é o menor e qual é o maior número
menor = min(num1, num2)
maior = max(num1, num2)

print(f"\nOs números inteiros compreendidos entre {menor} e {maior} são:")

# O range começa no número seguinte ao menor e vai até um número antes do maior
for i in range(menor + 1, maior):
    print(i, end=" ") # O end=" " faz com que os números sejam impressos na mesma linha
    
print() # Apenas para quebrar a linha no final