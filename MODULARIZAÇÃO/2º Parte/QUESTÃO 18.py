# QUESTÃO 15 DA LISTA
def progessao_pg(a, q, n):
    an = a * q ** (n - 1)
    sn = (a * (q ** n - 1)) / (q - 1)
    return an, sn

quantidade = 0
while(quantidade < 1):
    try:
        quantidade += 1
        a = int(input('Digite o valor do primeiro termo da pg: '))
        if(a <= 0):
            print('O PRIMEIRO TERMO DA PG TEM QUE SER MAIOR QUE 0')
        else:
            q = float(input('Digite a Razão da pg: '))
            if(q <= 0):
                print('A RAZAÕ DA PG TEM QUE SER MAIOR QUE 0')
            else:
                n = int(input('Digite o número de termos da pg: '))
                if(n <= 0):
                    print('O NÚMERO DE TERMOS DA PG TEM QUE SER MAIOR QUE 0')
                else:
                    enesimo = progessao_pg(a, q, n) [0]
                    soma = progessao_pg(a, q, n) [1]
                    print(f'O enésimo termo da pg foi o número: {enesimo}')
                    print(F'A soma da pg foi de: {soma}')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}') 
