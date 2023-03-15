print('\033[1;33m-=-=\033[m'*8)
print('   \033[4;31mAnalisador de Triângulos\033[m')
print('\033[1;33m-=-=\033[m'*8)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if (s2-s3) < s1 < s2+s3 and (s1-s3) < s2 < s1+s3 and (s1-s2) < s3 < s1+s2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
