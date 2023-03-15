print('\033[1;33m-=-=\033[m'*8)
print('   \033[4;31mAnalisador de Triângulos\033[m')
print('\033[1;33m-=-=\033[m'*8)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
seg = [s1, s2, s3]
seg.sort()
if seg[0] + seg[1] > seg[2]:
    print('Os segmentos acima FORMAM um triângulo!')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo!')
