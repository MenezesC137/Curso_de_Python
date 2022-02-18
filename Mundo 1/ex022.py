nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}.\n'
      'Seu nome em minúsculo é {}.\n'
      'Seu nome tem ao todo {} letras.\n'
      'Seu primeiro nome tem {} letras.'
      .format(nome.upper(),
              nome.lower(),
              len(nome) - nome.count(' '),
              nome.find(' ')))
