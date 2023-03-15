nome = str(input('Digite seu nome completo: ')).strip()
first = nome.split()
last = first[-1]
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {first[0]}')
print(f'Seu último nome é {last}')
