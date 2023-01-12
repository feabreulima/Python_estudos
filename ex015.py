#Aluguel de carros

dias = int(input('Digite quantos dias esse carro foi alugado: '))
kmrodados = float(input('\nDigite quantos km foram rodados com o carro: '))

price = ((dias*60) + (kmrodados*0.15))

print(f'O total a pagar por {dias} dias e {kmrodados} Km rodados é: R$ {price:.2f}')