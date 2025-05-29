# CRIAR / RESETAR LISTAS
agenda = []
contatos = []

# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if (len(nome) <= 2):
        print('O NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return nome

def lerEmail():
  while True:
    try:
      email = input('EMAIL: ')
      if (len(email) <= 5):
        print('ERRO, TENTE NOVANENTE')
      else:
        break
    except:
      print('ERRO')
  return email
    
def lerWhatsapp():
  while True:
    try:
      whatsapp = input('WhatsApp: ')
      if (len(whatsapp) < 11 or len(whatsapp) > 11):
        print('ERRO, TENTE NOVAMENTE')
      else:
        break
    except:
      print('ERRO')
  return whatsapp


# MENU: PROGRAMA PRINCIPAL (MAIN)
while True:
  try:
    print('MENU:')
    print('[DIGITE 0 PARA CADASTRAR UM USUÁRIO]')
    print('[DIGITE 1 PARA PESQUISAR DADOS DO USUÁRIO]')
    print('[DIGITE 2 PARA ATUALIZAR DADOS DO WHATSAPP DE UM USUÁRIO]')
    print('[DIGITE 3 PARA DELETAR UM CONTATO DA AGENDA]')
    print('[DIGITE QUALQUER TECLA PARA PARAR O PROGRAMA]')
    opcao = int(input('OPÇÃO: '))
    if opcao == 0:
      print(f'ENTRE COM OS DADOS DO {len(agenda) + 1}º USUÁRIO')
      nome = lerNome()
      email = lerEmail()
      whatsapp = lerWhatsapp()
      contatos = [nome, email, whatsapp]
      agenda.append(contatos)
    elif opcao == 1:
      print('PRIMEIRO RELATÓRIO')
      while True:
        print('Nome do usuário desejado ', end = ' ')
        dados_usuario = input('')
        lista_dados = [valor[0] for valor in (agenda)]
        try:
          indice = lista_dados.index(dados_usuario)
          print(f'DADOS DO {indice + 1}º CONTATO DA AGENDA')
          print(f'NOME: {agenda[indice][0]}')
          print(f'EMAIL: {agenda[indice][1]}')
          print(f'WhatsApp {agenda[indice][2]}')
          break
        except:
          print('NOME DO USUÁRIO NÃO LOCALIZADO NA AGENDA')
          break
    elif opcao == 2:
      print('SEGUNDO RELATÓRIO')
      while True:
        dados_usuario = input('EMAIL: ')
        lista_dados = [valor[1] for valor in (agenda)]
        try:
          indice = lista_dados.index(dados_usuario)
          novo_what = input('Atualizar número: ')
          if len(novo_what) < 11 or len(novo_what) > 11:
            print('ERRO')
          else:
            agenda[indice][2] = novo_what
            break
        except:
          print('EMAIL NÃO LOCOLIZADO NA AGENDA')
    elif opcao == 3:
      print('TERCEIRO RELATÓRIO')
      dados_usuario = input('Nome do usuário que sera deletado: ')
      lista_dados = [valor[0] for valor in (agenda)]
      try:
        indice = lista_dados.index(dados_usuario)
        agenda.pop(indice)
        print('O USUÁRIO FOI DELETADO')
      except:
        print('Nome do usuário não encontrado')
    else:
      break
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
