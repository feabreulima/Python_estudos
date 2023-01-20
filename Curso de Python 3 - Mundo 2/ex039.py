#Leia o ano de nascimento de um jovem e mostre se ele ainda vai prestar o serviço militar ou ja esta na hora ou não e mostre o tempo que falta ou que passou do prazo
import datetime

anonasc = int(input('\nEm que ano você nasceu? '))

anoatual = (datetime.date.today().year - anonasc)
faltam = str(anoatual - 18)


if anoatual < 18:
    print(f"\nFaltam \033[4;32m{faltam.replace('-','')}\033[m ano(s) para você se \033[1;42malistar\033[m!\n")
    
elif anoatual == 18:
    print(f"\nEstá na hora de se \033[4;32malistar\033[m!!!\n")
    
else:
    print(f"\nVocê passou {anoatual-18} anos do prazo para se alistar!\n")
