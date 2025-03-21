try:
    # DECLARAR VARIÁVEIS
    q = 0
    contador = 0
    media = 0
    soma = 0
    x = int(input('Digite o valor de (x): '))
    # TRATAMENTO DE ERRO
    if (x <= 0):
        print('O valor de (x) deve ser maior ou igual 1')
    else:
        for contador in range(6, 6 * x + 1):
            if (contador % 6 == 0):
                q += 1
                print(f'{q}ª número: {contador}')
                soma += contador
        media = soma / q
        print(f'A média é de: {media}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
