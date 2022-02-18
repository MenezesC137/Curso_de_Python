n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!\n'
      'Seu  primeiro nome é {}.\n'
      'Seu último nome é {}.'
      .format(nome[0],
              nome[len(nome)-1]))


