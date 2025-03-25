# VARIAVÉIS
pi = 3.14
n = 0
soma = .0
multiplicacao = 0.0
try:
    n = int(input('DIGITE QUALQUER NÚMERO INTEIRO E POSITIVO E >= 1: '))
    if(n < 1):
        print('O NÚMERO TEM QUE SER POSITIVO E MAIOR OU IGUAL A 1')
    else:   
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')