frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.\n'
      'A primeira letras A apareceu na posição {}.\n'
      'A última letra A apareceu na posição {}.'
      .format(frase.count('A'),
              frase.find('A')+1,
              frase.rfind('A')+1))
