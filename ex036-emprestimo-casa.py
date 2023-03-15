valor = float(input('Digite o valor da casa: R$').strip())
salario = float(input('Digite o valor salário do comprador: R$').strip())
anos = int(input('Digite em quantos anos será pago: ').strip())
parcelas = anos * 12
parcela_valor = valor / parcelas
print(f'Para pagar uma casa de R${valor:.2f} em {anos:} a prestação será de R${parcela_valor:.2f}.')
if parcela_valor > (salario * 30) / 100:
    print(f'Empréstimo \033[1;31mNEGADO\033[m.')
else:
    print(f'Empréstimo \033[1;32mAPROVADO\033[m.')
