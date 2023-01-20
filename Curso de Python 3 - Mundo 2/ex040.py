#Leia duas notas de um aluno, calcule sua média mostrando se foi aprovado, reprovado ou recuperação

n1 = float(input('\nDigite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

if media < 5:
    print('\nReprovado!\n')
elif media > 5 and media <= 6.9:
    print('\nRecuperação.\n')
else:
    print('\nAPROVADO!\n')