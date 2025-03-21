print('Escolha uma moeda: Real (R$), Dolar (US$) ou Libra (£)')
try:
  valor = float(input('Digite um valor:'))
  if(valor < 0):
    print('O valor deve ser maior que 0')
  else:
    moeda = int(input('Digite [0] para converter Real (R$) para Dólar e Libra, \n'
                      'digite [1] caso queira converter Dólar (US$) para Real e Libra ou digite \n'
                      '[2] caso queira converter Libra (£) para Real e Dolar: '))
    if(moeda != 0 and moeda > 2):
      print('[0] para REAL, [1] para DOLAR e [2] para LIBRA')
    else:
      if (moeda == 0):
        real_dolar = valor * 0.1733463
        real_libra = valor * 0.1341274
        print(f'Você tem: {real_dolar:.2f}US$')
        print(f'Você tem: {real_libra:.2f}£')
      elif (moeda == 1):
        dolar_real = valor * 5.7687992
        dolar_libra = valor * 0.7738141
        print(f'Você tem: {dolar_real:.2f} R$')
        print(f'Você tem: {dolar_libra:.2f} £')
      else:
        libra_real = valor * 7.4555982
        libra_dolar = valor * 1.2923
        print(f'Você tem: {libra_real:.2f}R$ ')
        print(f'Você tem: {libra_dolar:.2f}US$  ')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
