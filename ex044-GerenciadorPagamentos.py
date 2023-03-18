print('\033[1;33m-=-=\033[m'*9)
print('     \033[4;31mCOVIL DO LOBO - LOJA GAMER\033[m')
print('\033[1;33m-=-=\033[m'*9)
compras = float(input('Valor total das compras: R$'))
dinheiro = compras - ((compras*10)/100)
debito = compras - ((compras*5)/100)
juros = compras + ((compras*10)/100)
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro(10% de desconto)
[ 2 ] à vista no cartão de débito(5% de desconto)
[ 3 ] em até 3x no cartão de crédito
[ 4 ] em 4x ou mais no cartão de crédito(Juros de 10%)''')
while True:
    forma = int(input('Escolha a forma de pagamento: '))
    if forma == 1:
        print(f'''O total a pagar será de R${dinheiro:.2f} com desconto.
Desconto total de {compras-dinheiro:.2f}.''')
        break
    elif forma == 2:
        print(f'''O total a pagar será de R${debito:.2f} com desconto.
Desconto total de {compras-debito:.2f}.''')
        break
    elif forma == 3 or forma == 4:
        parcelas = int(input('Quantas parcelas: '))
        if forma == 3:
            print(f'Sua compra será parcelada em {parcelas}x de R${compras/parcelas:.2f}.')
            break
        else:
            print(f'''Sua compra será parcelada em {parcelas}x de R${juros/parcelas:.2f} COM JUROS.
Sua compra de R${compras:.2f} vai custar R${juros:.2f} no final.''')
            break
    else:
        print('Por favor, digite uma opção válida.')
        continue

