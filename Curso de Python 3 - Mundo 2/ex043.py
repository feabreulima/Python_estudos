#Leia o peso e altura de uma pessoa, calcule o imc e mostre seu status com base no imc

height = float(input('\nDigite sua altura em Metros: '))
kg = float(input('Digite seu peso em Kg: '))

imc = (kg/height**2)
print(f"\nSeu IMC: {imc:.1f}")

if imc < 18.5:
    print("\nAbaixo do peso!\n")
elif imc > 18.5 and imc < 25:
    print("\nPeso ideal.\n")
elif imc >= 25 and imc <= 30:
    print("\nSobrepeso!\n")
elif imc >= 30 and imc <= 40:
    print("\nObesidade!\n")
else:
    print("\nObseidade mórbida!\n")