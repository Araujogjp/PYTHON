try:
    print('OS NÚMEROS MÚLTIPLOS DE 11 NO INTERVALO DE [200, 100], SUA SOMA E SUA MÉDIA É DE:')
    q = 0  # ENUMERAR
    soma = 0
    media = 0
    for contador in range(200, 100, -1):  # CONTADOR
        if (contador % 11 == 0):
            q += 1
            soma += contador
            media = soma / q
            print(f'{q}º número: {contador}')
    print(f'A soma é de: {soma}')
    print(f'A média é de: {media}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
