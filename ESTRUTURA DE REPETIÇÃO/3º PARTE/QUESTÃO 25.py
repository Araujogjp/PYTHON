import math 
# VARIAVÉIS
idade = 0
massa = 0
taxa = 0.0
contador = 0
verificacao = 0
while(contador < 2):
    try:
        contador += 1
        print('DIGITE [1] CASO O PACIENTE SEJA DIABÉTICO E [0] CASO O PACIENTE NÃO SEJA DIABÉTICO ')
        verificacao = int(input(f'O {contador}º PACIENTE É DIABÉTICO?: '))
        if(verificacao < 0 or verificacao > 1):
            print('[1] CASO SEJA DIABÉTICO [0] CASO NÃO SEJA')
            contador -= 1
        else:
            idade = int(input(f'DIGITE A IDADE DO {contador}º PACIENTE: '))
            if(idade < 1 or idade > 100):
                print('A IDADE DEVE SER ENTRE 1 ANO A 100 ANOS')
                contador -= 1
            else:
                massa = float(input(f'DIGITE A MASSA DO {contador}º PACIENTE '))
                if(massa <= 0 or massa > 200):
                    contador -=1 
                    print('A MASSE DEVE ESTAR ENTRE 0.1 A 200 KG')
                else:
                    if(verificacao == 0):
                        taxa = math.sqrt(0.98 * (massa ** 2)) / (1.08 * idade)
                        print(f'A TAXA MÉDIA DE GLICOSE DO {contador}º PACIENTE É DE: {taxa: .2f}')
                    else:
                        taxa = math.sqrt(massa ** 2) / (0.93 * idade)
                        print(f'A TAXA MÉDIA DE GLICOSE DO {contador}º PACIENTE É DE: {taxa: .2f}')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')