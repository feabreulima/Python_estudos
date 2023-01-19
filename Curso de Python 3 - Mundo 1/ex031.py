#Leia a distância em Km de um cidade e cobre R$ 0,50 por km rodado se a distância for menor que 200, senão cobre R$ 0,45 por Km

Km = float(input('\nQual a distância da viajem em Km? '))

if Km <= 200:
    menorKm = Km * 0.5
    print(f'\nA viajem de {Km} Km custa R$ {menorKm:.2f}')
else:
    maiorKm = Km * 0.45
    print(f'\nA viajem de {Km} Km custa R$ {maiorKm:.2f}')