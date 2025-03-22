try:
    print('OS NÚMEROS MÚLTIPLOS DE 3 NO INTERVALO DE [3, 100] SÃO:')
    q = 0
    for contador in range(3, 100 + 1):
        if (contador % 3 == 0):
            q += 1
            print(f'{q}º número: {contador}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
