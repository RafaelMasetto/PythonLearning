dist = int(input('Qual é a distância da sua viagem? '))
curta = dist * 0.5
longa = dist * 0.45
print(f'Você está prestes a começar uma viagem de {dist:.1f}KM')
if dist <= 200:
    print(f'E o preço da sua passagem será de R${curta:.2f}')
else:
    print(f'E o preço da sua passagem será de R${longa:.2f}')
