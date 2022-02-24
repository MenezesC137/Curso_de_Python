linha = '-' * 30
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media do {aluno["Nome"]}: '))
print(linha)
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for key, val in aluno.items():
    print(f' - {key} é igual a {val}')
