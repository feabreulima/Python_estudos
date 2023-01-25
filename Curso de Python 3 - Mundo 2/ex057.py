#Leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('\nQual seu sexo? [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('\nTente novamente.')
    sexo = str(input('\nQual seu sexo? [M/F]: ')).upper().strip()[0]
print('Informação registrada com sucesso!\n')
