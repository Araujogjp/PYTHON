# VARIÁVEIS
salario = 0.0
salario_fundamental = 0.0
salario_medio = 0.0
salario_superior = 0.0
media_fundamental = 0.0
media_medio = 0.0
media_superior = 0.0
fundamental = 0
medio = 0
superior = 0
grau = 0
contador = 0
print('----- NÍVEL DE ESCOLARIEDADE -----')
print(' DIGITE [O] PARA -> FUNDAMENTAL ')
print(' DIGITE [1] PARA -> MEDIO ')
print(' DIGITE [2] PARA -> SUPERIOR ')
while(contador < 10000):
    try:
        contador += 1
        salario = float(input(f'{contador}º ENTREVISTADO - QUAL É O SEU SALÁRIO?: '))
        if(salario < 0):
            print('O SALÁRIO DEVE SER MAIOR OU IGUAL A 0')
            contador -= 1
        else:
            grau = int(input(f'{contador}º ENTREVISTADO - QUAL É O SEU GRAU DE ESCOLARIEDADE?: '))
            if(grau < 0 or grau > 2):
                print('[0] PARA FUNDAMENTAL, [1] PARA MÉDIO E [2] PARA SUPERIOR')
                contador -= 1
            else:
                if(grau == 0):
                        salario_fundamental += salario
                        fundamental += 1
                elif(grau == 1):
                        salario_medio += salario
                        medio += 1
                else:
                    salario_superior += salario
                    superior += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
media_fundamental = salario_fundamental / fundamental
media_medio = salario_medio / medio
media_superior = salario_superior / superior
print(f'A Média salarial de pessoas com grau de escolariedade fundamental é de: {media_fundamental: .2f}R$ ')
print(f'A Média salarial de pessoas com grau de escolariedade médio é de: {media_medio: .2f}R$ ')
print(f'A Média salarial de pessoas com grau de escolariedade superior é de: {media_superior: .2f}R$ ')