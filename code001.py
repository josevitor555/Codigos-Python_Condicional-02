#questão 1
produto1 = str(input('Informe um nome do primeiro produto: '))
produto1_Preco = float(input('Informe o preço do primeiro produto: '))

produto2 = str(input('Informe um nome do segundo produto: '))
produto2_Preco = float(input('Informe o preço do segundo produto: '))

menor_preco = 0 # valor padrão

if produto1_Preco != produto2_Preco:
  if produto1_Preco < produto2_Preco:
    menor_preco = produto1_Preco
  else:
    menor_preco = produto2_Preco
else:
  print('Os preços são iguais!')

print(f'O preço do menor produto: {menor_preco}')


# preco1 = R$ 100,00
# preco2 = R$ 200,00

# 1 caso: preco1 < preco2: menor_preco = preco1
# 2 caso: preco2 < preco1: menor_preco = preco2
