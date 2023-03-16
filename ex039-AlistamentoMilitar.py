from datetime import date
ano = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print(f'''Quem nasceu em {ano} tem {idade} anos em {date.today().year}.
Está na hora de se alistar.''')
elif idade < 18:
    print(f'''Quem nasceu em {ano} tem {idade} anos em {date.today().year}.
Faltam {18-idade} anos para o alistamento.
Seu alistamento será em {ano+18}.''')
else:
    print(f'''Quem nasceu em {ano} tem {idade} anos em {date.today().year}.
Você já deveria ter se alistado há {idade-18} anos.
Seu alistamento deveria ter sido em {date.today().year - (idade-18)}''')
