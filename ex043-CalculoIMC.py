print('\033[1;33m-=-=\033[m'*9)
print(' \033[4;31mCalculando Índice de Massa Corporal\033[m')
print('\033[1;33m-=-=\033[m'*9)
peso = float(input('Digite seu peso:(Kg)'))
altura = float(input('Digite sua altura:(M)'))
IMC = peso / altura**2
print(f'Seu IMC é de {IMC:.2f}!')
if IMC < 18.5:
    print('Cuidado! Você está ABAIXO do peso ideal!')
elif 18.5 < IMC < 25:
    print('Parabéns! Você está no PESO IDEAL!')
elif 25 < IMC < 30:
    print('Cuidado! Você está com SOBREPESO!')
elif 30 < IMC  < 35:
    print('Muito Cuidado!Você está com OBESIDADE GRAU I!')
elif 35 < IMC < 40:
    print('Muito Cuidado! Você está com OBESIDADE GRAU II!')
else:
    print('MUITO CUIDADO! Você está com OBESIDADE GRAU III!')
