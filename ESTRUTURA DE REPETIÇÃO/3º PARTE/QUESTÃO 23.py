import numpy as np
# VARIÁVEIS 
menor_tempo = np.inf
tempo_de_prova = 0.0
inscricao = 0
contador = 0
vencedor = 0
while(contador < 4):
    try:
        contador += 1
        inscricao = int(input('Nº DE INSCRIÇÃO: '))
        if(inscricao <= 0):
            print('O NÚMERO DA INSCRIÇÃO DEVE SER MAIOR QUE 0')
        else:
            tempo_de_prova = float(input('QUAL FOI O TEMPO DE PROVA (em minutos): '))
            if(tempo_de_prova <= 0 ):
                print('O TEMPO DE PROVA DEVE SER MAIOR QUE 0')
                contador -= 1
            if(tempo_de_prova < menor_tempo):
                menor_tempo = tempo_de_prova
                vencedor = inscricao
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
print(f'O VENCEDOR FOI O ATLETA DE NÚMERO DE INSCRIÇÃO -> {vencedor} - E O SEU TEMPO FOI DE -> {menor_tempo: .2f} MINUTOS.')