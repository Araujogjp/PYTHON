# QUESTÃO 2 DA LISTA
def paresimpares(n, opcao):
    resultado = 1 
    for contador in range(1, n + 1):
        if opcao == 0 and contador % 2 == 0:
            resultado *= contador
        elif opcao == 1 and contador % 2 != 0:
            resultado *= contador
    return resultado
q = 0
while(q < 5):
    try:
        q += 1
        print('OPÇÃO [0] CASO DESEJE A MULTIPLICAÇÃO DE TODOS OS PARES NÚMEROS ENTRE [1, N]')
        print('OPÇÃO [1] CASO DESEJE A MULTIPLICAÇÃO DE TODOS OS ÍMPARES NÚMEROS ENTRE [1, N]')
        opcao = int(input('DIGITE SUA OPÇÃO: '))
        if(opcao < 0 or opcao > 1):
           print('[0] PARA MULTIPLICAR TODOS OS PARES E [1] PARA MULTIPLICAR TODOS OS ÍMPARES')
        else:
           n = int(input('DIGITE UM NÚMERO INTEIRO: '))
           if(n <= 0):
               print('O NÚMERO DIGITADO TEM QUE SER MAIOR QUE 0')
           else:
               resultado = paresimpares(n, opcao)
               print(f'O RESULTADO FOI: {resultado}')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')
