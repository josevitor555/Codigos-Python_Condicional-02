#questão 2
nomePescador = str(input('Informe o nome do pescador: '))
peso_Peixe = float(input('Informe o peso em kilo: '))

kiloExcedido = 10

if (peso_Peixe > kiloExcedido):
  multa = (peso_Peixe - 10) * 1.50
  print(f'Você foi multado: R$ {round(multa, 2)}')
else:
  print(f'{nomePescador} não foi multado.')