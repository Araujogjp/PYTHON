# VARIÁVEIS 
q = 0 # ENUMERAR
try:
  for contador in range(1000, 1501):
    if(contador % 7 == 0 or contador % 13 == 0):
      q += 1
      print(f'{q}º número: {contador}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
