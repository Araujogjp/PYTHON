# CRIAR / RESETAR LISTAS
alunos = []
turma = []

# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if len(nome) <= 2:
        print('NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return nome

def lerCurso():
  while True:
    try:
      curso = input('CURSO: ')
      if len(curso) <= 2:
        print('ERRO, TENTE NOVAMENTE')
      else:
        break
    except:
      print('ERRO')
  return curso

def lerMedia():
  while True:
    try:
      media_final = float(input('MÉDIA FINAL: '))
      if media_final < 0:
        print('ERRO, A MÉDIA FINAL NÃO PODE SER MENOR QUE 0')
      else:
        break
    except:
      print('ERRO')
  return media_final

def lerParticipao():
  if opcao == 1:
    return 1
  else:
    return 0

# MENU: PROGRAMA PRINCIPAL (MAIN)
q = 0
print('MENU')
print('[DIGITE [0] CASO DESEJE CADASTRAR UM ALUNO')
print('[DIGITE [1] PARA VER O RELATÓRIO DE PARTICIPAÇÃO NA PESQUISA]')
print('[DIGITE [2] PARA EXIBIR A LISTA DE PESQUISADORES]')
print('[DIGITE [3] EXIBIR O DESEMPENHO ACADÊMICO ACIMA DA MÉDIA GERAL]')
print('[DIGITE [4] PARA O CÁLCULO DE BOLSA DE PESQUISA]')
print('[DIGITE OUTRO NÚMERO QUALQUER PARA SAIR DO PROGRAMA]')

while True:
  try:
    menu = int(input('SUA OPÇÃO: '))
    if menu == 0:
      nome = lerNome()
      curso = lerCurso()
      media_final = lerMedia()
      while True:
        print('[DIGITE [1] CASO PARTICIPOU DA INICIAÇÃO CIENTÍFICA]')
        print('[DIGITE [0] CASO NÃO TENHA PARTICIPADO]')
        opcao = int(input('SUA OPÇÃO: '))
        if opcao < 0 or opcao > 1:
          print('ERRO, TENTE NOVAMENTE')
        else:
          break
      aluno = [nome, curso, media_final, opcao]
      turma.append(aluno)
    elif menu == 1:
      print('RELATÓRIO DE PARTICIPAÇÃO NA PESQUISA')
      try:
        participaram = [aluno for aluno in turma if aluno[3] == 1]
        lista_p = (len(participaram) / len(turma)) * 100
        print(f'A PORCENTAGEM DE ALUNOS QUE PARTICPARAM DA PESQUISA FOI DE: {lista_p:.2f}%')
      except:
        print('NENHUM ALUNO CADASTRADO')
    elif menu == 2:
      participaram = [aluno for aluno in turma if aluno[3] == 1]
      for valor in participaram:
        print(f'NOME: {valor[0]}')
        print(f'CURSO: {valor[1]}')
    elif menu == 3:
      try:
        print('ALUNOS ACIMA DA MÉDIA')
        listaMedia = [valor[2] for valor in turma]
        media = sum(listaMedia) / len(listaMedia)
        superior = [valor for valor in turma if valor[2] > media]
        for valor in superior:
          print(f'NOME: {valor[0]}')
          print(f'CURSO: {valor[1]}')
        if not superior:
          print('NENHUM ALUNO ACIMA DA MÉDIA')
      except:
        print('NENHUM ALUNO CADASTRADO')
    elif menu == 4:
      try:
        print('CÁLCULO DA BOLSA DE PESQUISA')
        participaram = [aluno for aluno in turma if aluno[3] == 1]
        bolsistas = len(participaram)
        print(f'O TOTAL DE BOLSISTAS É DE: {bolsistas}')
        print(f'O TOTAL GASTO EM UM MÊS É DE {bolsistas * 400}')
        print(f'O TOTAL GASTO EM UM ANO É DE: {(bolsistas * 400) * 12}')
        
      except:
        print('NENHUM ALUNO CADASTRADO')
    else:
      print('FIM DO PROGRAMA')
      break
  except:
    print('ERRO')
