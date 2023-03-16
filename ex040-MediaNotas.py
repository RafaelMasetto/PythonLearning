nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno:'))
nota3 = float(input('Digite a terceira nota do aluno'))
media = (nota1+nota2+nota3) / 3
if media < 5:
    print(f'A média do aluno foi {media:.1f}. Portanto ele está REPROVADO.')
elif 7 > media >= 5:
    print(f'A média do aluno foi {media:.1f}. Portanto ele está em RECUPERAÇÃO.')
else:
    print(f'A média do aluno foi {media:.1f}. Portanto ele está APROVADO.')
