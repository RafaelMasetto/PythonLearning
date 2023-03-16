num = int(input('Digite um número inteiro qualquer para converter: '))
print('''Agora escolha qual a base para conversão:
[1] converter para Binário.
[2] converter para Octal.
[3] converter para Hexadecimal.''')
escolha = int(input('Sua escolha: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if escolha == 1:
    print(f'O número {num} convertido para Binário é igual a {binario[2:]}.')
elif escolha == 2:
    print(f'O número {num} convertido para Octal é igual a {octal[2:]}.')
elif escolha == 3:
    print(f'O número {num} convertido para Hexadecimal é igual a {hexadecimal[2:]}.')
else:
    print('Opção Inválida. Tente novamente.')
