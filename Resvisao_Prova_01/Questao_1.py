def sistema_loja():
    print("--- Sistema de Pagamento ---")
    
    # Recebe o valor do produto
    try:
        valor_produto = float(input("Digite o valor do produto: R$ "))
    except ValueError:
        print("Valor inválido. Por favor, digite apenas números.")
        return

    # Exibe o menu de opções
    print("\n--- Opções de Pagamento ---")
    print("1 - À vista (10% de desconto)")
    print("2 - Parcelado em 2x (sem juros)")
    print("3 - Parcelado em 3x ou mais (juros de 5% ao mês sobre o valor total)")
    
    opcao = input("\nEscolha a forma de pagamento (1, 2 ou 3): ")

    # Lógica baseada na escolha do usuário
    if opcao == '1':
        valor_final = valor_produto - (valor_produto * 0.10)
        print("\n[Resumo da Compra]")
        print("Opção escolhida: 1 - À vista (10% de desconto)")
        print(f"Valor final a pagar: R$ {valor_final:.2f}")

    elif opcao == '2':
        valor_final = valor_produto
        valor_parcela = valor_final / 2
        print("\n[Resumo da Compra]")
        print("Opção escolhida: 2 - Parcelado em 2x (sem juros)")
        print(f"Valor final a pagar: R$ {valor_final:.2f}")
        print(f"Parcelas: 2x de R$ {valor_parcela:.2f}")

    elif opcao == '3':
        try:
            parcelas = int(input("Digite o número de parcelas (3 ou mais): "))
            if parcelas >= 3:
                # O juros é de 5% (0.05) vezes o número de parcelas sobre o valor total
                taxa_juros = 0.05 * parcelas
                valor_juros = valor_produto * taxa_juros
                valor_final = valor_produto + valor_juros
                valor_parcela = valor_final / parcelas
                
                print("\n[Resumo da Compra]")
                print(f"Opção escolhida: 3 - Parcelado em {parcelas}x (com juros de 5% ao mês)")
                print(f"Valor final a pagar: R$ {valor_final:.2f}")
                print(f"Parcelas: {parcelas}x de R$ {valor_parcela:.2f}")
            else:
                print("\nErro: Para parcelar em menos de 3x, reinicie e escolha a opção 1 ou 2.")
        except ValueError:
            print("Número de parcelas inválido. Digite um número inteiro.")

    else:
        print("\nErro: Opção inválida. Escolha 1, 2 ou 3.")

# Executa o programa
sistema_loja()