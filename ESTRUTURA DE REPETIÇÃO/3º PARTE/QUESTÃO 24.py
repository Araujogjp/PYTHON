# VARIÁVEIS 
preco = 0.0
reajuste = 0.0
preco_reajustado = 0.0
contador = 0
preco_final = 0.0
while(contador < 50):
    try:
        preco = float(input('DIGITE O PREÇO DA MERCADORIA: '))
        if(preco <= 0):
            print('O PREÇO DEVE SER MAIOR QUE 0')
            contador -= 1
        else:
            reajuste = 0.05 * preco
            if(reajuste > 25.50):
                preco_reajustado = preco - (reajuste * 0.02) 
                print(f'O PREÇO FINAL FOI DE: {preco_reajustado: .2f}R$')
            else:
                preco_final = preco + reajuste
                print(f'O PREÇO FINAL FOI DE: {preco_final: .2f}R$')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')