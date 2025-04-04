# QUESTÃO 5 DA LISTA
def primos(n):
    if(n == 2):
        return True
    if(n % 2 == 0):
        return False
    contador = 3
    while(contador * contador <= n):
        if(n % contador == 0):
            return False
        contador += 2
    return True
q = 0
while(q < 5):
    try: 
        q += 1
        n = int(input('DIGITE UM NÚMERO INTEIRO: '))
        if(n < 1):
            print('[N] TEM QUE SER MAIOR OU IGUAL A 1')
        else:
            print(f'{primos(n)}')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')
