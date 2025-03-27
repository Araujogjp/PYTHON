import math
# VARIAVÉIS
n = 0
s = math.pi
m = 1.0 / math.pi
try:
    n = int(input('DIGITE QUALQUER NÚMERO INTEIRO E POSITIVO E >= 1: '))
    if(n < 1):
        print('O NÚMERO TEM QUE SER POSITIVO E MAIOR OU IGUAL A 1')
    else:   
        for contador in range(0, n, 2):
            if(contador != 0):
             s += math.pi / contador
        for contador1 in range(1, n + 1, 2):
            if(contador != 1):
              m *= contador1 / math.pi
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
print(f'A SOMA DE TODOS OS NÚMEROS FOI DE: {s + math.pi / n: .5f}')
print(f'A MULTIPLICAÇÃO DE TODOS OS NÚMEROS FOI DE: {m * n / math.pi: .5f}')
