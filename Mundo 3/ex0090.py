linha = '-' * 30
aluno = dict()
nome = str(input('Nome: '))
aluno['nome'] = nome
media = float(input(f'Media do {nome}: '))
aluno['media'] = media
print(linha)
for key, val in aluno.items():
    print(f' - {key} é igual a {val}')
if media <= 5:
    print(f' - Situação é igual a Reprovado')
elif 5 > media <= 7:
    print(f' - Situação é igual a Recuperação')
elif 7 > media <= 10:
    print(f' - Situação é igual a Aprovado')
else:
    sit = 'Nota digitada errada'
