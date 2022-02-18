from datetime import date
atual = date.today().year
totma = 0
totme = 0
for cont in range(1, 8):
    nasceu = int(input('Em qual ano a {}ª pessoa nasceu? '.format(cont)))
    idade = atual - nasceu
    if idade >= 18:
        totma += 1
    else:
        totme += 1
print('''Ao todo tivemos {} maiores de idade.
E {} Menores.'''.format(totma, totme))

