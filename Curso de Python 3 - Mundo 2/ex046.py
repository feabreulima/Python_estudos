#Faça uma contagem regressiva de 1 até 10 para o ano novo com espera de 1s
from time import sleep
import emoji

for c in range(1,11):
    print(c)
    sleep(1)
print(emoji.emojize('\n:fireworks: :fireworks: :fireworks: Feliz ano novo!!! :fireworks: :fireworks: :fireworks:\n'))