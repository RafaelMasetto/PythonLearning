velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print(f'\033[0;33m Tenha um bom dia! Dirija com segurança!')
else:
    print(f'\033[0;31mMULTADO! Você excedeu o limite permitido de 80km/h.\n'
          f'Você deve pagar uma multa de R${multa:.2f}!')
    print(f'\033[0;33mTenha um bom dia! Dirija com segurança!')
