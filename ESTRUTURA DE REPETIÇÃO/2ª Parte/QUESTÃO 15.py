#DECLARAR VARIÁVEIS
n = 0.0
q = 0
negativo = 0
positivo = 0
porcentagem_positivo = 0.0
porcentagem_negativo = 0.0
total = 0
try:
    while True:
        q += 1 # ENUMERAR
        n = float(input(f'Digite qualquer número real, positivo ou negativo ou digite [0] para parar o programa -> {q}ª Número: '))
        if(n > 0):
            positivo += 1
        else:
            negativo += 1
        if(n == 0):
            print('FIM DO PROGRAMA')
            break
        else:
            total = positivo + negativo
            if(total != 0):
                porcentagem_positivo = (positivo / total) * 100
                porcentagem_negativo = (negativo / total) * 100
    print(f'A porcentagem de número positivos é de: {porcentagem_positivo:.2f}%')
    print(f'A porcentagem de número negativos é de: {porcentagem_negativo:.2f}%')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
