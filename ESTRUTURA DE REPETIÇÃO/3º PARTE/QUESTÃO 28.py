import math
# VARIAVÉIS
n = 0
s = math.pi
m = 1.0
try:
    n = int(input('DIGITE QUALQUER NÚMERO INTEIRO E POSITIVO E >= 1: '))
    if(n < 1):
        print('O NÚMERO TEM QUE SER POSITIVO E MAIOR OU IGUAL A 1')
    else: 
        if(n % 2 == 0):
          m *= n / math.pi          
        for contador in range(2, n + 1, 2):
             s += math.pi / contador
        for contador1 in range(1, n + 1, 2):
            m *= contador1 / math.pi
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
print(f'A SOMA DE TODOS OS NÚMEROS FOI DE: {s: .5f}')
print(f'A MULTIPLICAÇÃO DE TODOS OS NÚMEROS FOI DE: {m: .5f}')
