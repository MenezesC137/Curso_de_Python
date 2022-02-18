n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2
if 10 <= media >= 7:
    print('Aprovado!, media {}'.format(media))
elif 6.9 <= media >= 5:
    print('Recuperação!. media {}'.format(media))
elif media < 5:
    print('Reprovado!, media {}'.format(media))
else:
    print('Notas digitadas erradas!')