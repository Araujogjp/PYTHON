import math
try:
  segundos = int(input('Digite o tempo de permanência em segundos:'))
  if(segundos < 0):
    print('ERRO')
  else:
    horas = segundos/3600
    minutos = (horas - math.floor(horas)) * 60
    segundos = (minutos - math.floor(minutos)) * 60
    horas = math.floor(horas)
    minutos = math.floor(minutos)
    segundos = math.ceil(segundos)
    print(f'Tempo de permanência do aluno: {horas}hora(s) {minutos}minuto(s) e {segundos} segundo(s)')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
