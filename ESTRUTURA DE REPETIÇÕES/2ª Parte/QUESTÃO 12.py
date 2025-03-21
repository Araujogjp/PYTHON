try:
    # DECLARAR VARIÁVEIS
    q = 0 # ENUMERAR
    c = 0.0 # TEMPERATURA
    media = 0.0 # MEDIA DA TEMPERATURA
    soma = 0.0 # SOMAR AS TEMPERATURAS
    while True:
        q += 1
        c = float(input(f'TEMPERATURA DO {q}ª DIA: '))
        soma += c
        media = soma / q
        # AS TEMPERATURAS FICAM ACIMA DE 28º graus
        if (c <= 28):
            print('FIM DO PROGRAMA')
            print(f'A Média de temperatura foi de: {media:.2f}')
            break
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
