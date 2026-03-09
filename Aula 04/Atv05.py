senha_valida = [0]

while True:
    senha = input("Digite uma senha de 4 dígitos numéricos: ")
    
    # Verifica se a senha tem exatamente 4 caracteres e se é composta apenas por números
    if len(senha) == 4 and senha.isdigit():
        print("Senha cadastrada com sucesso.")
        break
    else:
        print("Senha inválida. Tente novamente.")
