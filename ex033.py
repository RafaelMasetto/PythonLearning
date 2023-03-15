n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
if n1 > n2 and n1 > n3:
    print(f'O maior valor digitado foi {n1}.')
elif n2 > n1 and n2 > n3:
    print(f'O maior valor digitado foi {n2}.')
else:
    print(f'O maior valor digitado foi {n3}.')
if n1 < n2 and n1 < n3:
    print(f'O menor valor digitado foi {n1}.')
elif n2 < n1 and n2 < n3:
    print(f'O menor valor digitado foi {n2}.')
else:
    print(f'O menor vlaor digitado foi {n3}.')
