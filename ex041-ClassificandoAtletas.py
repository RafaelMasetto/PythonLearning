from datetime import date
ano = int(input('Ano de Nascimento do Atleta: '))
idade = date.today().year - ano
rank = ['MIRIM', 'INFANTIL', 'JUNIOR', 'SÊNIOR', 'MASTER']
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classificação: {rank[0]}.')
elif idade <= 14:
    print(f'Classificação: {rank[1]}.')
elif idade <= 19:
    print(f'Classificação: {rank[2]}.')
elif idade <= 25:
    print(f'Classificação: {rank[3]}.')
else:
    print(f'Classificação: {rank[4]}.')
