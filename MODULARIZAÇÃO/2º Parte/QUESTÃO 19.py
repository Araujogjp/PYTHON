def mercadoria_2(opcao, preco, reajuste):
    reajuste_f = reajuste / 100
    if(opcao == 1):
        preco_f = preco + (preco * reajuste_f)
    else:
        preco_f = preco - (preco * reajuste_f)
    return preco_f

q = 0
while True:
    try:
        q += 1
        preco = float(input(f'DIGITE O VALOR DA {q}º MERCADORIA: '))
        if(preco < 0):
            print('O PREÇO DA MERCADORIA DEVE SER MAIOR OU IGUAL A 0')
        else:
            reajuste = float(input('DIGITE O VALOR DO REAJUSTE: '))
            if(reajuste <= 0):
                print('O REAJUSTE TEM QUE SER MAIOR QUE 0')
            else:
                print('[0] PARA PARAR O PROGRAMA')
                print('[1] PARA ACRÉSCIMO NO VALOR DA MERCADORIA')
                print('[2] PARA DESCONTO NO VALOR DA MERCADORIA')
                opcao = int(input('DIGITE SUA OPÇÃO: '))
                if(opcao < 0 or opcao > 2):
                    print('AS OPÇÕES SÃO: [0, 1 E 2]')
                else:
                    preco_reajustado = mercadoria_2(opcao, preco, reajuste)
                    if(opcao == 0):
                        print('FIM DO PROGRAMA')
                        break
                    elif(opcao == 1):
                        print(f'O VALOR REAJUSTADO FOI DE {preco_reajustado: .2f}')
                    else: 
                        print(f'O VALOR REAJUSTADO FOI DE {preco_reajustado: .2f}')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')