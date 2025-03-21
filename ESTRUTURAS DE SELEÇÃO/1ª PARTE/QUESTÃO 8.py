temperaturaFahrenheit = float(0.0)
temperaturaCelsius = float(0.0)
try:
  tempTipo = int(input("Digite [0] caso deseje informar a temperatura em Celsius (C) ou digite [1] caso deseje informar a temperatura em Fahrenheit (F):"))
  temperatura = float(input('Digite a temperatura em Celsius (C) ou Fahrenheit (F):'))
  if(tempTipo != 0 and tempTipo != 1):
    print('Digite [0] para informar a temperatura em Celsius (C) e digite [1] para informar a temperatura em Fahrenheit (F)')
  else:
    if(tempTipo  == 0):
      temperaturaFahrenheit = (temperatura * 9/5) + 32
      print(f'A temperatura em Fahrenheit (F) é igual a: {temperaturaFahrenheit:.2f}')
    else:
      temperaturaCelsius = (temperatura - 32) * 5/9
      print(f'A temperatura em Celsius (C) é igual a: {temperaturaCelsius:.2f} ')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
