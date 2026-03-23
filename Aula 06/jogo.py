import os, random

sorteado = random.randint(1,100)
tentativas = 0

while True:
    numero = int(input("Digite o numero magico: "))
    tentativas = tentativas+1
    os.system('cls || clear')
    if (numero == sorteado):
        print(f"Parabens voce acertou o numero magico em {tentativas} tentativas ! ")
        break
    elif (numero > sorteado):
        print(f"O numero magico e menor que o digitado - {tentativas} tentativas !")
    else:
        print(f"O numero magico e maior que o numero digitado - {tentativas} tentativas !")