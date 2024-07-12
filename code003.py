#questão 3
nome = str(input('Informe seu nome: '))
idadeParticipante = int(input('Informe sua idade: '))

if (idadeParticipante >= 5 and idadeParticipante <= 7):
  temp = 'Infantil A'
  categoria = temp
elif (idadeParticipante >= 8 and idadeParticipante <= 11):
  temp = 'Infantil B'
  categoria = temp
elif (idadeParticipante >= 12 and idadeParticipante <= 13):
  temp = 'Juvenil A'
  categoria = temp
elif (idadeParticipante >= 14 and idadeParticipante <= 17):
  temp = 'Juvenil B'
  categoria = temp
elif (idadeParticipante >= 18):
  temp = 'Maiores de 18 anos'
  categoria = temp

print(f'{nome} é da categoria {categoria}')
