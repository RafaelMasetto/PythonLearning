salario = float(input('Qual é o salário do funcionário? '))
aumento1 = (salario * 10) / 100
aumento2 = (salario * 15) / 100
if salario > 1250:
    print(f'O novo salário será {salario+aumento1:.2f}. O aumento foi de {(salario+aumento1)-salario:.2f}.')
else:
    print(f'O novo salário será {salario+aumento2:.2f}. O aumento foi de {(salario+aumento2)-salario:.2f}.')
