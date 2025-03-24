try:
    contador = 0
    verificar = 0
    sim = 0
    nao = 0
    emp = 0.0
    desemp = 0.0
    total = 0
    while (contador < 10000):
        contador += 1
        verificar = int(input(f'({contador}) ENTREVISTADO: Digite [0] caso esteja desempregado e [1] caso esteja empregado: '))
        if (verificar > 1 or verificar < 0):
            print('ERRO: [0] caso esteja desempregado e [1] caso esteja empregado')
            contador -= 1
        else:
            if (verificar == 0):
                nao += 1
            else:
                sim += verificar
    print(f'No total há: {nao} pessoas desempregadas')
    print(f'No total há: {sim} pessoas empregadas')
    total = sim + nao
    emp = (sim / total) * 100
    desemp = (nao / total) * 100
    print(f'A porcentagem que corresponder a pessoas empregadas na cidade é de: {emp:.2f}%')
    porcetagem_desemp = (nao / contador) * 100
    print(f'A porcentagem que corresponder a pessoas desempregadas na cidade é de: {desemp:.2f}%')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
