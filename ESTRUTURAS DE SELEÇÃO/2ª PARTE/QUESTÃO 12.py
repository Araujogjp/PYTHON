try:
  massa = float(input('Digite a sua massa(kg):'))
  altura = float(input(' Digite sua altura(m):'))
  if(massa < 0 or altura <= 0  ):
    print('A massa e altura devem ser maiores que 0')
  else:
    imc = massa / (altura ** 2)
    if(imc < 18.5):
      print(f'O seu grau é: Magreza: {imc:.2f} ')
    elif(imc  >= 18.5 and imc < 25):
      print(f'O seu grau é: Saudável: {imc:.2f}')
    elif(imc > 25 and imc < 30):
      print(f'O seu grau é: Sobrepeso: {imc:.2f}  ')
    elif (imc >= 30 and imc< 35):
      print(f'O seu grau é: Obesidade Grau I: {imc:.2f}')
    elif(imc >= 35 and imc < 40):
      print(f'O seu grau é: Obesidade Grau II: {imc:.2f} )')
    else:
      print(f'O seu grau é: Obesidade Grau III: {imc:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}  ')
