#Sorteio de alunos em ordem de apresentação
import random

nome = [input('\nNome do primeiro aluno: '), input('Nome do segundo aluno: '),input('Nome do terceiro aluno: '),input('Nome do último aluno: ')]

print(f'\nAlunos a apresentar: {random.sample(nome,4)}!')
