print('Para que a soma seja feita, os números devem estar entre 10 e 90, ser divisíveis por 5 e ter resto 2.')

try:
    # DECLARAR VARIÁVEIS
    n = 0
    contador = 0
    soma = 0

    while True:
        contador += 1
        n = int(input(f'{contador}ª número: '))

        if n <= 0:
            print('FIM DO PROGRAMA')
            break
        elif 10 <= n <= 90 and n % 5 == 2:
            soma += n

    print(f'A soma é de: {soma}')

except ValueError:
    print('ERRO: Digite apenas números inteiros válidos.')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
