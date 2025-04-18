# QUESTÃO 14 DA LISTA
def estacionamento(HH_ENTRADA, MM_ENTRADA, HH_SAIDA, MM_SAIDA):
    preco = 7.0
    
    MINUTOS_ENTRADA = HH_ENTRADA * 60 + MM_ENTRADA
    MINUTOS_SAIDA = HH_SAIDA * 60 + MM_SAIDA

    if(MINUTOS_SAIDA < MINUTOS_ENTRADA):
        MINUTOS_SAIDA +=  24 * 60

    TEMPO_TOTAL_MIN = MINUTOS_SAIDA - MINUTOS_ENTRADA

    if TEMPO_TOTAL_MIN > 24 * 60:
        return None    
    
    HORAS = TEMPO_TOTAL_MIN // 60
    MINUTOS = TEMPO_TOTAL_MIN % 60
    preco_final = preco * HORAS
    return HORAS, MINUTOS, preco_final

try:
    ENTRADA = input('HORARIO DE ENTRADA: HH:MM: ')
    HHMM_ENTRADA = ENTRADA.split(':')
    HH_ENTRADA = int(HHMM_ENTRADA[0])
    MM_ENTRADA = int(HHMM_ENTRADA[1])
    SAIDA = input('HORARIO DE SAÍDA: HH:MM: ')
    HHMM_SAIDA = SAIDA.split(':')
    HH_SAIDA = int(HHMM_SAIDA[0])
    MM_SAIDA =int(HHMM_SAIDA[1])
    if(HH_ENTRADA > 23 or HH_ENTRADA < 0 or HH_SAIDA > 23 or HH_SAIDA < 0):
        print('ERRO: OS VALORES INFORMADOS DOS MINUTOS DEVEM ESTAR ENTRE 0 E 59.')
    elif(MM_ENTRADA < 0  or MM_SAIDA < 0 or MM_ENTRADA > 59 or MM_SAIDA > 59):
        print('ERRO: OS VALORES INFORMADOS DOS MINUTOS DEVEM ESTAR ENTRE 0 E 59.')
    elif(HH_SAIDA < HH_ENTRADA and HH_ENTRADA - HH_SAIDA > 23):
      print('ERRO: O TEMPO MÁXIMO QUE UM VEICULO PODE FICAR NO ESTACIONAMENTO É DE 24 HORAS.')
    else:
        HORAS_F = estacionamento(HH_ENTRADA, MM_ENTRADA, HH_SAIDA, MM_SAIDA)[0]
        MINUTOS_F = estacionamento(HH_ENTRADA, MM_ENTRADA, HH_SAIDA, MM_SAIDA)[1]
        preco_f = estacionamento(HH_ENTRADA, MM_ENTRADA, HH_SAIDA, MM_SAIDA)[2]
        print(f'VOCÊ FICOU NO ESTACIONAMENTO DURANTE {HORAS_F} HORAS(S) E {MINUTOS_F} MINUTOS')
        print(f'VOCÊ PAGARÁ {preco_f}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')