# VARIÁVEIS
cartao_vip = 0
cartao_standard = 0
salario = 0.0
total = 0
cadastro = 0
porcentagem_vip = 0.0
porcentagem_standard  = 0.0
print('[0] PARA SAIR DO PROGRAMA')
print('[1] PARA CADASTRAR CLIENTE')
try: 
  while True:
    cadastro = int(input('[0] para sair do Programa ou [1] para Cadastrar: '))
    if(cadastro < 0 or cadastro > 1):
      print('[0] PARA SAIR DO PROGRAMA E [1] PARA CADASTRAR')
    else:
      if(cadastro == 0):
        print('FIM DO PROGRAMA')
        break
      else:
        salario = float(input('Digite o salário do cliente: '))
        if(salario >= 5000):
          cartao_vip += 1
        else: 
          cartao_standard += 1
  total = cartao_vip + cartao_standard
  if(total > 0):
    porcentagem_vip = (cartao_vip / total) * 100
    porcentagem_standard = (cartao_standard / total) * 100
    print(f'A porcentagem de clientes com cartão vip foi de: {porcentagem_vip: .2f}%')
    print(f'A porcentagem de clientes com cartão standard foi de: {porcentagem_standard: .2f}%')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
