print('NÚMEROS MÚLTIPLOS DE N QUE ESTEJAM ENTRE O INTERVALO [limite_inferior e limite_superior]')

q = 0
n = int(input('Digite o valor de n [n >= 2 e inteiro]: '))
if(n < 2):
    print('O valor de N deve ser igual ou maior que 2')
else:
    limite_inf = int(input('Digite o limite_inferior: '))
    if(limite_inf < 2):
        print('O limite_inferior deve ser maior ou igual a 2')
    else:
        limite_superior = int(input('Digite o limite_superior: '))
        if(limite_superior < 2):
            print('O limite_superior deve ser maior ou igual a 2')
        else:
            if(limite_inf <= n):
                if(limite_inf <= limite_superior):
                    for contador in range(limite_inf, limite_superior):
                        if(contador % n == 0):
                            q += 1
                            print(f'{q}° número: {contador}')
