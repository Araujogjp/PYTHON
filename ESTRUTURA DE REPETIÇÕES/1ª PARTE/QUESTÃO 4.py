try:
    print('de todos os números PARES E ÍMPARES')
    qpar = 0
    qimpar = 0
    somapar = 0
    somaimpar = 0
    for contador in range(10, 100):
        if(contador % 2 == 0):
            qpar += 1
            somapar += contador
            print(f'{qpar}ª número par: {contador}')
        else:
            qimpar += 1
            somaimpar += contador
            print(f'{qimpar}ª número ímpar: {contador}')
    print(f'A soma de todos os pares é de: {somapar}')
    print(f'A soma de todos os impares é de: {somaimpar}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
