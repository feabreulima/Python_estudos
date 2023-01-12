#Caracteristicas primitvas de um valor

x = input('Digite algo: ')

print('Capslock?' , x.isupper()) #Verifica se está em Maiúsculo

print('É alfanumérico?' , x.isalnum()) #Verifica se está em Alfanumérico

print('É alfabético?' , x.isalpha()) #Verifica se é Alfabetico

print('Os caracteres são dígitos?' , x.isdigit()) #Verifica se é os caracteres são dígitos

print('São caracteres decimais?' , x.isdecimal()) #Verifica se todos caracteres são decimais

print('São caracteres numéricos?' , x.isnumeric()) #Verifica se os caracteres são numéricos

print('É uma string válida?' , x.isidentifier()) #Verifica se a string for um identificador válido no Python

print('Está em minusculo?' , x.islower()) #Verifica se está em minúsculo

print('Todos ou caracteres são impimiveis ou está vazio?' , x.isprintable()) #Verifica se todos os caracteres da string forem imprimíveis ou se a string estiver 

print('É um espaço em branco?' , x.isspace()) #Verifica se houver apenas caracteres de espaço em branco na string

print('É uma sequência com título?' , x.istitle()) #Verifica se a sequência for uma sequência com título

