salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print(f'O funcionário que ganhava {salario:.2f}, passa a ganhar {novo:.2f}.')
