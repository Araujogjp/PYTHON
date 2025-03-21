try:
    contador = 0
    salario = 0.0
    SM = 998.05
    a = 0
    b = 0
    c = 0
    total = 0
    taxa_a = 0
    taxa_b = 0
    taxa_c = 0

    while (contador < 1000):
        contador += 1
        salario = float(input(f'({contador})ª ENTREVISTADO: Quanto que você ganha: '))
        if (salario < SM):
            print('O valor que você ganha deve ser igual ou maior que o Salário Mínimo que é: [998.05R$]')
            contador = 1
        else:
            if (salario >= SM * 15):
                a += 1
            elif (salario < SM * 15 and salario >= SM * 5):
                b += 1
            else:
                c += 1

    total = a + b + c
    taxa_a = (a / total) * 100
    taxa_b = (b / total) * 100
    taxa_c = (c / total) * 100

    print(f'{taxa_a:.2f}% das pessoas entrevistadas ganham mais que 15 salários mínimos')
    print(f'{taxa_b:.2f}% das pessoas entrevistadas ganham mais que 5 salários mínimos e menos que 15 salários mínimos')
    print(f'{taxa_c:.2f}% das pessoas entrevistadas ganham menos que 5 salários mínimos')

except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
