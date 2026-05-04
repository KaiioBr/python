def simular_emprestimo():
    print("--- Simulador de Empréstimo Imobiliário ---")
    
    # Recebe os dados do usuário
    try:
        valor_casa = float(input("Qual o valor da casa a comprar? R$ "))
        salario = float(input("Qual o seu salário atual? R$ "))
        anos_pagar = int(input("Em quantos anos você pretende pagar a casa? "))
    except ValueError:
        print("Erro: Por favor, digite apenas valores numéricos válidos.")
        return

    # Calcula o número de meses e o valor da prestação mensal
    meses_pagar = anos_pagar * 12
    prestacao = valor_casa / meses_pagar
    
    # Calcula qual é o limite de 30% do salário do comprador
    limite_salario = salario * 0.30

    print("\n--- Resultado da Análise ---")
    
    # Verifica a condição de aprovação
    if prestacao > limite_salario:
        print("Infelizmente voce nao pode obter o emprestimo")
        # Linhas extras apenas para mostrar o motivo (opcional)
        print(f"(A prestação de R$ {prestacao:.2f} excede os 30% do seu salário, que é R$ {limite_salario:.2f})")
    else:
        print(f"Valor da prestação: R$ {prestacao:.2f}")
        print("Emprestimo OK")

# Executa o programa
simular_emprestimo()