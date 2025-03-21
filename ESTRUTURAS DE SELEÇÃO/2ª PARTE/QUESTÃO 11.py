import math
# DICA:
TOTAL_PAGAR  = float(0.0)
TEMPO_TOTAL_MIN  = int(0)
try:
  VALOR = float(input('Digite o valor do estacionamento a cada 30 minutos: '))
  if(VALOR <=0):
    print('O valor deve ser maior que 0')
  else:
    ENTRADA  = input('Horario de entrada: HH:MM:  ')
    HHMM_ENTRADA = ENTRADA.split(':')
    HH_ENTRADA = int(HHMM_ENTRADA[0])
    MM_ENTRADA = int(HHMM_ENTRADA[1])
    SAIDA  = input('Horário de saida: HH:MM: ')
    HHMM_SAIDA = SAIDA.split(":")
    HH_SAIDA  = int(HHMM_SAIDA[0])
    MM_SAIDA = int(HHMM_SAIDA[1])
    if(HH_ENTRADA < 0 or HH_SAIDA < 0 or HH_ENTRADA > 23 or HH_SAIDA > 23):
      print('ERRO: OS VALDRES INFORMADOS DAS HORAS DEVEM ESTAR ENTRE 0 E 23. ')
    elif(MM_ENTRADA < 0  or MM_SAIDA < 0 or MM_ENTRADA > 59 or MM_SAIDA > 59):
      print('ERRO: OS VALORES INFORMADOS DOS MINUTOS DEVEM ESTAR ENTRE 0 E 59.')
    elif(HH_SAIDA < HH_ENTRADA and HH_ENTRADA - HH_SAIDA >= 23):
      print('ERRO: O TEMPO MÁXIMO QUE UM VEICULO PODE FICAR NO ESTACIONAMENTO É DE 24 HORAS.')
    else:
      MINUTOS_ENTRADA  = HH_ENTRADA * 60 + MM_ENTRADA
      MINUTOS_SAIDA = HH_SAIDA * 60 + MM_SAIDA
      if(MINUTOS_SAIDA < MINUTOS_ENTRADA):
        MINUTOS_SAIDA = MINUTOS_SAIDA + 24 * 60
      TEMPO_TOTAL_MIN = MINUTOS_SAIDA - MINUTOS_ENTRADA
      HORAS = TEMPO_TOTAL_MIN // 60
      MINUTOS = TEMPO_TOTAL_MIN % 60
      if(TEMPO_TOTAL_MIN <= 30):
        TOTAL_PAGAR = 0
        print("Você não pagará nada")
      else:
        TOTAL_PAGAR = VALOR * math.ceil(TEMPO_TOTAL_MIN/30)
        print(f'Você terá que pagar: {TOTAL_PAGAR:.2f}R$')
      print(f'O Tempo em que você ficou no estacionamento foi de: {HORAS} horas e {MINUTOS} minutos.')
except  Exception as ERRO_EXCECAO:
  print (f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}  ')
