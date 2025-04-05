# QUESTÃO 11 DA LISTA
def ano(verificar, numero):
    quociente = 0
    resto = 0
    quociente = verificar // numero
    resto = verificar % numero 
    if(verificar % 400 == 0):
        bissexto = 1
    elif(verificar % 4 == 0 and verificar % 100 != 0):
        bissexto = 1
    else:
        bissexto == 0
    return bissexto, quociente, resto
try:
    verificar = int(input('DIGITE UM ANO QUALQUER: '))
    if(verificar <= 0):
        print('O ANO TEM QUE SER MAIOR QUE O')
    else:
        numero = int(input('DIGITE [4, 100 OU 400]: '))
        if(numero != 4 and numero != 100 and numero != 400): 
            print('O NÚMERO TEM QUE SER [4, 100 OU 400]')
        else:
            b = ano(verificar, numero)[0]
            if(b == 1):
                print(f'{verificar} É BISSEXTO')
            else:
                print(f'{verificar} NÃO É BISSEXTO')
            q = ano(verificar, numero)[1]
            r = ano(verificar, numero)[2]
            print(f'O QUOCIENTE DO ANO {verificar} É {q}')
            print(f'O RESTO DO QUOCIENTE DI ANO {verificar} É {r}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')