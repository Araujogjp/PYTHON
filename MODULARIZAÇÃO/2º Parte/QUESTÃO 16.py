import math
def tempot(horas):
    segundos = horas * 3600
    horas_f = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas_f, minutos, segundos

q = 0
while(q < 2):
    try:
        q += 1
        horas = float(input('DIGITE O TEMPO EM HORAS: '))
        if(horas < 0):
            print('O TEMPO QUE SER IGUAL OU MAIOR QUE 0')
        else:
            horas_fim = math.floor(tempot(horas)[0])
            minutos_f = math.floor(tempot(horas)[1])
            segundos_f = math.ceil(tempot(horas)[2])
            print(f'O TEMPO FOI DE {horas_fim} HORAS + {minutos_f} MINUTOS + {segundos_f} SEGUNDOS')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DEEXCEÇÃO: {ERRO_EXCECAO}')
print('.')