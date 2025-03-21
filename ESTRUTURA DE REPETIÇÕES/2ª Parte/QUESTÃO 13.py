import numpy as np

# VARIÁVEIS
print('DIGITE [1] CASO SEJA DO SEXO MASCULINO OU DIGITE [2] CASO SEJA DO SEXO FEMININO')
maior_altura_masc = -1 * np.inf
maior_altura_fem = -1 * np.inf
sexo = 0
contador = 0
media = 0.0
homem = 0 
mulher = 0
homem_1_82 = 0
mulher_1_82 = 0
porcentagem_homens_maiorque_1_82 = 0.0
porcentagem_mulheres_maiorque_1_82 = 0.0

try:
    while(contador < 4):
        contador += 1
        sexo = int(input(f'{contador}° ENTREVISTADO -> DIGITE [1] CASO SEJA HOMEM OU [2] CASO SEJA MULHER: '))
        if(sexo != 1 and sexo != 2):
            print('TECLA [1] CASO SEJA HOMEM OU TECLA [2] CASO SEJA MULHER')
            contador -= 1
        else:
            altura = float(input('DIGITE SUA ALTURA: '))
            if(altura < 1 or altura > 3):
                print('A ALTURA DEVE ESTAR ENTRE [1...3] metros')
                contador -= 1
            else:
                media += altura 
                if(sexo == 1):
                    homem += 1
                    if(altura > maior_altura_masc):
                        maior_altura_masc = altura
                    if(altura > 1.82):
                        homem_1_82 += 1
                else:
                    mulher += 1
                    if(altura > maior_altura_fem):
                        maior_altura_fem = altura
                    if(altura > 1.82):
                        mulher_1_82 += 1
    media /= contador 
    if(maior_altura_masc < 0):
        print('NENHUMA ALTURA MASCULINA FOI INFORMADA ')
    else:
        print(f'MAIOR ALTURA HOMEM: {maior_altura_masc:.2f}')
    if(maior_altura_fem < 0):
        print('NENHUMA ALTURA FEMININA FOI INFORMADA ')
    else:
        print(f'MAIOR ALTURA MULHER: {maior_altura_fem:.2f}')
    print(f'A média foi de: {media:.2f}')
    if(homem_1_82 > 0 and homem > 0):
        porcentagem_homens_maiorque_1_82 = (homem_1_82 / homem) * 100
    if(mulher_1_82 > 0 and mulher > 0):
        porcentagem_mulheres_maiorque_1_82 = (mulher_1_82 / mulher) * 100
    print(f'A porcentagem de homens maiores que 1.82 é de: {porcentagem_homens_maiorque_1_82:.2f}%')
    print(f'A porcentagem de mulheres maiores que 1.82 é de: {porcentagem_mulheres_maiorque_1_82:.2f}%')

except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
