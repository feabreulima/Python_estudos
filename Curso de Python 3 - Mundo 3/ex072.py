#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a vinte.
#O programa irá ler um número pelo teclado entre 0 e 20 e mostralo por extenso

contagem = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
print(len(contagem))
while True:
    n = int(input('\nEscolha um número de 0 a 20: '))
    while n not in range(0,21):
        n = int(input('\nErro, tente novamente. Escolha um número de 0 a 20: '))
    print('\n'+contagem[n],'\n')
    break