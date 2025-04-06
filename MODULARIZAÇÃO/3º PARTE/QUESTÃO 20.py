def contracheque(salario_bruto, numero_dependentes):
    inss = salario_bruto * 0.11
    plano_saude = salario_bruto * 0.02
    total_descontos = inss + plano_saude
    salario_liquido = salario_bruto - total_descontos
    salario_minimo = 1518
    vale_dependentes = 0.05 * salario_bruto * numero_dependentes
    vale_alimentacao = salario_minimo + vale_dependentes

    return salario_liquido, total_descontos, vale_alimentacao

q = 0
while (q < 1):
    try:
        print('DESCONTOS')
        print('INSS: 11% Salário Bruto;')
        print('Plano de Saúde: 2% Salário Bruto;')
        print('BENEFÍCIOS:')
        print('Vale Alimentação: R: Salário Mínimo + 5% Salário Bruto por dependente.')
        q += 1
        salario_bruto = float(input('DIGITE O SALÁRIO BRUTO: '))
        if(salario_bruto <= 0):
            print('O SALÁRIO BRUTO DEVE SER MAIOR QUE 0')
        else:
            numero_dependentes = int(input('QUANTOS DEPENDENTES O TRABALHADOR POSSUI?: '))
            if(numero_dependentes < 0):
                print('O NÚMERO DE DEPENDENTES DEVE SER MAIOR OU IGUAL A 0')
            else:
                salario_final = contracheque(salario_bruto, numero_dependentes)[0]
                descontos_totais = contracheque(salario_bruto, numero_dependentes)[1]
                vale_final = contracheque(salario_bruto, numero_dependentes)[2]
                print(f'O SALÁRIO FINAL FOI DE {salario_final:.2f}')
                print(f'O VALE ALIMENTAÇÃO FINAL FOI DE {vale_final:.2f}')
                print(f'O TOTAL DE DESCONTOS FOI DE {descontos_totais}')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')