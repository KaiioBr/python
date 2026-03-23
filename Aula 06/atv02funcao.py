def contador_letras(x):
    n = x.replace(' ','')
    qletras = len(n)
    print(f"O seu nome {n} tem {qletras} letras ")

nome = input("Digite seu nome ")
contador_letras(nome)