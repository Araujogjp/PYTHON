print('Para que a soma seja feita os números devem ser entre 10 e 90, devem ser divididos por 5 e o resto seja 2')
try:
    # DECLARAR VARIÁVEIS
    n = 0
    contador = 0
    soma = 0
    informar = int(input('Digite quantas números você quer informar: '))
    if(informar <= 0):
        print('FIM DO PROGRAMA')
    else:
        while(contador < informar):
            contador += 1
            n = int(input(f'{contador}ª número: '))
            if(n <= 0):
                print('FIM DO PROGRAMA')
                break
            else:
                if(n >= 10 and n <= 90):
                    if(n % 5 == 2):
                        soma += n
        print(f'A soma é de: {soma}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
