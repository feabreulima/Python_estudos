#Converter real para dólar

real = float(input('Quantos R$ há na sua carteira?: '))
dolar = 3.27

res = (real/dolar)

print(f'Com seus R${real} você pode comprar {res:.2f} dólares!')