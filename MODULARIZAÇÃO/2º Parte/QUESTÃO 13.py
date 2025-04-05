def executar(escolha):
    # SOMATORIO
    if(escolha == 1):
        if(opcao == 1):
            return n1 + n2
        elif(opcao == 2):
            return n1 - n2
        elif(opcao == 3):
            return n1 * n2
        elif(opcao == 4):
            return n1 / n2
        elif(opcao == 5):
            return n1 % n2
        else:
            return n1 // n2
    
    # FIBONACCI
    elif(escolha == 2):
        ultimo = 0 
        penultimo = 1
        soma = 0
        if(n == 0):
            soma += ultimo
        if(n == 1):
            soma += penultimo
        soma += penultimo
        for i in range(2, n + 1):
            proximo = ultimo + penultimo
            soma += proximo
            ultimo = penultimo 
            penultimo = proximo
        return soma 
    
    # MERCADORIA
    else: 
        c_reajuste = preco * (reajuste / 100)
        total = preco - c_reajuste
        return total, c_reajuste

    
try: 
    print('[1] CASO DESEJE ACESSAR A MINI CALCULADORA')
    print('[2] CASO DESEJE CALCULAR OS N PRIMEIROS TERMOS DA SÉRIE DE FIBONACCI')
    print('[3] CASO DESEJE INFORMAR O VALOR DE UMA MERCADORIA E SEU REAJUSTE')
    escolha = int(input('QUAL SUA ESCOLHA?: '))
    if(escolha < 1 or escolha > 3):
        print('ESCOLHA DE [1, 2 OU 3]')
    else: 

        # SOMATORIO
        if(escolha == 1): 
            n1 = int(input('NÚMERO: '))
            if(n1 < 0):
                print('N1 TEM QUE SER POSITIVO')
            else: 
                n2 = int(input('NÚMERO: '))
                if(n2 < 0):
                    print('N2 TEM QUE SER POSITIVO')
                else:
                    print('[1] PARA SOMAR')
                    print('[2] PARA SUBTRAIR')
                    print('[3] PARA MULTIPLICAR')
                    print('[4] PARA DIVIDIR')
                    print('[5] PARA MOD')
                    print('[6] PARA DIV')
                    opcao = int(input('QUAL SUA OPÇÃO?: '))
                    if(opcao < 1 or opcao > 6):
                        print('ERRO DE ENTRADA [1, 6]')
                    else:
                        mini = executar(escolha)
                        print(f'{mini:.2f}')

        # FIBONACCI
        elif(escolha == 2): 
            n = int(input('DIGITE UM NÚMERO: '))
            if(n < 0):
                print('N TEM QUE SER MAIOR OU IGUAL A 0')
            else:
                somatorio = executar(escolha)
                print(f'A SOMA FOI DE: {somatorio}')

        # MERCADORIA
        else: 
            preco = float(input('Digite o preço da mercadoria: '))
            if(preco <= 0):
                print('O preço tem que ser maior que 0')
            else:
                reajuste = float(input('Quanto você quer de reajuste?: '))
                if(reajuste < 0):
                    print('O reajuste tem que ser maior ou igual a 0%')
                else:
                    preco_final = executar(escolha)[0]
                    reajuste_final = executar(escolha)[1]
                    print(f'O preço final foi de {preco_final:.2f}R$')
                    print(f'O reajuste final foi de {reajuste_final:.2f}R$')
except Exception as ERRO_EXCECAO:
   print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')