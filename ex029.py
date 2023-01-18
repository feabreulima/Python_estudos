#Leia a velocidade de um carro e analise se a velocidade é maior que 80km/h e multe R$ 7,00 a cada km/h a cima do permitido

car = int(input('\nVelocidade atual do seu carro em Km/h: '))

multa = ((car - 80) * 7)

if car <= 80:
    print('Você não levou multa.\n')
else:
    print(f'Você passou a {car} Km/h e levou uma multa de R$ {multa:.2f}\n')