try:
  oz = 35.274
  toneladas = 1000
  verificar = 0
  massa = float(input("Digite a massa: "))
  if (massa <= 0 or verificar < 0 or verificar > 2):
    print("ERRO, A MASSA DEVE SER MAIOR QUE 0 ")
  else:
    verificar = int(input("Informe: [0] para converter Quilograma (Kg) para Onça (Oz) e Tonelada (T) [1] para converter Onça (Oz) para Quilograma (Kg) e Tonelada (T) [2] para converter Tonelada (T) para Quilograma (Kg) e Onça (Oz): "))
    if (verificar  == 0):
      kg_oz = massa * oz
      kg_toneladas = massa / toneladas
      print(f' {massa:.2f} Kg equivale a {kg_oz:.2f} Oz e {kg_toneladas:.2f} T')
    elif (verificar == 1):
      oz_kg = massa / oz
      oz_toneladas = massa / 35274
      print(f' {massa:.2f} Oz equivale a {oz_kg:.2f} Kg e  {oz_toneladas:.2f} T')
    elif (verificar == 2):
      toneladas_kg = massa * toneladas
      toneladas_oz = toneladas_kg * oz
      print(f' {massa:.2f} T equivale a {toneladas_kg:.2f} Kg e  {toneladas_oz:.2f} Oz')
except Exception as ERRO_EXCECAO:
  print (f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
