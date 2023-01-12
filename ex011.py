'''Calcular a área de uma parede e calcular a
quantidade de tinta necessária para pintar a parede,
sabendo que cada litro pinta 2m^2 '''

height = float(input('Insira a altura da parede em metros: '))
width = float(input('Insira a largura da parede em metros: '))
area = (height * width)

p = (area/2)

print(f'Para pintar a parede de {area}m^2 precisará de {p} litros de tinta.')