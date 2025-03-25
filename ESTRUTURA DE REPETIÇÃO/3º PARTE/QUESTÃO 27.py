# VARIÁVEIS
n = 0.0
positivos = 0
positivos_total = 0.0
negativos = 0
negativos_total = 0.0
media_positivos = 0.0
media_negativos = 0
q = 0
while True:
    try:
        q += 1
        print('[0] PARA PARAR O PROGRAMA')
        n = float(input(f'{q}º NÚMERO - POSITIVO OU NEGATIVO: '))
        if(n == 0):
            print('FIM DO PROGRAMA')
            break
        else:
            if(n < 0):
                negativos_total += n
                negativos += 1
            else: 
                positivos_total += n
                positivos += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
if(negativos_total == 0):
    print('NENHUM NÚMERO NEGATIVO FOI INFORMADO')
else:
    media_negativos = negativos_total / negativos
    print(f'A MÉDIA DOS NÚMEROS NEGATIVOS FOI DE {media_negativos: .2f}')
if(positivos_total == 0):
    print('NENHUM NÚMERO POSITIVO FOI INFORMADO')
else:
    media_positivos = positivos_total / positivos
    print(f'A MÉDIA DOS NÚMEROS POSITIVOS FOI DE {media_positivos: .2f}')

