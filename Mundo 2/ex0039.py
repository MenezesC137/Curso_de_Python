from datetime import date
atual = date.today().year
sexo = str(input('Qual dos gêneros você se classifica: (F) (M)'))
num1 = int(input('Ano de nascimento:'))
idade = atual - num1
if sexo == 'f':
    print('O Alistamento para o sexo Feminino não e Obrigatorio.')
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(num1, idade, atual))
    print('Já está na hora de se apresentar ao Exercito Brasileiro.')
elif idade <= 17:
    temp = 18 - idade
    print('Quem nasceu em {} tem {} anos em {}.'.format(num1, idade, atual))
    print('Ainda falta {} anos para seu alistamento, que ira ocorre em {}.'
          .format(temp, (atual + temp)))
elif idade >= 19 and idade <= 22:
    temp = idade - 18
    print('Quem nasceu em {} tem {} anos em {}'.format(num1, idade, atual))
    print('Está atrasado para o alistamento que seria no ano {}, mas corre que ainda da tempo.'
          .format(atual - temp))
else:
    print('Considerar que já passou pelo quartel, pois já passou o tempo de tolerancia.')