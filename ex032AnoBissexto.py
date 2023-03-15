from datetime import date
from time import sleep
print(f'Vamos descobrir se um ano é bissexto?')
sleep(1)
ano = int(input(f'Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == int('0'):
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
