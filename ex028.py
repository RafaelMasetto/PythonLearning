import random
import time
print('\033[4;31m-=-\033[m' * 19)
print(f'\033[4;31m Vou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[4;31m-=-\033[m' * 19)
rand = random.randint(0, 5) # Faz o computador sortear o número
num = int(input(f'Em que número eu pensei? '))
print(f'\033[1;32mPROCESSANDO...')
time.sleep(2)
if num == rand:
    print(f'\033[1;34mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\033[1;33mGANHEI! Eu pensei no número {rand} e não no {num}!')
