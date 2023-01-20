#Leia o ano de nascimento de um atleta e mostre a categoria dele com base na idade

import datetime

anonasc = int(input('\nEm que ano você nasceu? '))
idade = datetime.date.today().year - anonasc

if idade <= 9:
    print("\nCategoria: Mirim\n")
elif idade > 9 and idade <= 14:
    print("\nCategoria: Infantil\n")
elif idade > 14 and idade <= 19:
    print("\nCategoria: Junior\n")
elif idade == 20:
    print("\nCategoria: Sênior\n")
else:
    print("\nCategoria: MASTER\n")