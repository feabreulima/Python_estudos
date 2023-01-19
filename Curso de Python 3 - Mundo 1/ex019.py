#Sorteio de alunos
import random

nome = [input('\nNome do primeiro aluno: '), input('Nome do segundo aluno: '),input('Nome do terceiro aluno: '),input('Nome do último aluno: ')]

print(f'\nO aluno escolhido foi {random.choice(nome)}!')