contador = 0 # CONTAR
q = 0 # ENUMERAR
try:
    n = int(input('Digite qualquer número inteiro: '))
    for contador in range(n, n + 51):
        q += 1
        print(f'{q}ª número: {contador}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
