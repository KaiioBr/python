import os     

while True:
    print("salários até R$ 280,00 (incluindo) : aumento de 20%: ")
    print("salários entre R$ 280,00 e R$ 700,00 : aumento de 15%: ")
    print("salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%: ")
    print("salários de R$ 1500,00 em diante : aumento de 5%: ")
    
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: R$ "))  
    
    if salario < 280:
        aumento = salario * 0.20
        salario_aumento = aumento + salario
        print(f"Salario antes do reajuste: {salario} ")
        print(f"o percentual de aumento aplicado; {0.20} ")
        print(f"o valor do aumento; {aumento} ")
        print(f"o novo salário, após o aumento. {salario_aumento:.2f}")
        break
    elif salario >= 280 and salario < 700:
        aumento = salario * 0.15
        salario_aumento = aumento + salario
        print(f"Salario antes do reajuste: {salario} ")
        print(f"o percentual de aumento aplicado; {0.15} ")
        print(f"o valor do aumento; {aumento} ")
        print(f"o novo salário, após o aumento. {salario_aumento:.2f}")
        break
    elif salario >= 700 and salario < 1500:
        aumento = salario * 0.10
        salario_aumento = aumento + salario
        print(f"Salario antes do reajuste: {salario} ")
        print(f"o percentual de aumento aplicado; {0.10} ")
        print(f"o valor do aumento; {aumento} ")
        print(f"o novo salário, após o aumento. {salario_aumento:.2f}")
        break
    elif salario >= 1500:
        aumento = salario * 0.05
        salario_aumento = aumento + salario
        print(f"Salario antes do reajuste: {salario} ")
        print(f"o percentual de aumento aplicado; {0.05} ")
        print(f"o valor do aumento; {aumento} ")
        print(f"o novo salário, após o aumento. {salario_aumento:.2f}")
        break
    else:
        print("Valor inválido")
        break