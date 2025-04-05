# QUESTÃO 12 DA LISTA
import math
def horario(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

q = 0
while(q < 2):
    try:
        q += 1
        segundos = int(input('DIGITE O TEMPO EM SEGUNDOS: '))
        if(segundos < 0):
            print('O TEMPO QUE SER IGUAL OU MAIOR QUE 0')
        else:
            horas_f = math.floor(horario(segundos)[0])
            minutos_f = math.floor(horario(segundos)[1])
            segundos_f = math.ceil(horario(segundos)[2])
            print(f'O TEMPO FOI DE {horas_f} HORAS + {minutos_f} MINUTOS + {segundos_f} SEGUNDOS')
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DEEXCEÇÃO: {ERRO_EXCECAO}')
print('.')