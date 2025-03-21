try:
    # DECLARAR VARIÁVEIS GLOBAIS
    q = 0  # ENUMERAR
    soma = 0

    print('Números múltiplos de 3 e não múltiplos de 5')

    for contador in range(9, 90):
        if (contador % 3 == 0 and contador % 5 != 0):
            q += 1
            print(f'{q} Número: {contador}')
            soma += contador

    print(f'A soma de todos os números múltiplos de 3 e não múltiplos de 5 é: {soma}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
