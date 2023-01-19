#Quando e quantas vezes a letra 'A' aparece em determinada frase

frase = str(input('\nEscreva uma frase: ')).strip()
frase2 = frase.upper()

print(f'\nNa frase "{frase}", aparecem: {frase2.count("A")} letras "A" ')
print(f'O primeiro "A" na posição: {frase2.find("A")+1} \nO último "A" na posição: {frase2.rfind("A")+1}\n')
