def processar_notas():
    notas = []
    quantidade_alunos = 8

    print(f"--- Coleta de Notas ({quantidade_alunos} alunos) ---")
    

    for i in range(quantidade_alunos):
        while True: 
            try:
                nota = float(input(f"Digite a nota do {i+1}º aluno: "))
                notas.append(nota)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número (ex: 7.5).")


    media_turma = sum(notas) / len(notas)


    notas_acima_media = [nota for nota in notas if nota > media_turma]

    print("\n" + "="*30)
    print("RESULTADOS FINAIS")
    print("="*30)
    print(f"Média aritmética da turma: {media_turma:.2f}")
    print(f"Notas que ficaram acima da média: {notas_acima_media}")

processar_notas()