n1 = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
      'PYTHON', 'CURSO', 'STUDIER', 'PRATICAR')
for cont in n1:
    print(f'\nNa palavra {cont} temos: ', end='')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
