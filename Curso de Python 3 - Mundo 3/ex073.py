#Crie uma tupla com os 20 times colocados do brasileirão. Depois mostre a) os 5 primeiros colocados b) os últimos 4 colocados
#c) uma lista com os times em ordem alfabética d) em que posição está o Fortaleza

tabela = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Atlético-GO','Avaí','Juventude')

print('='*30)
print(f'Times do brasileirão: {tabela}', end='')
print('='*30)
print(f'Os 5 primeiros colocados são {tabela[:5]}')
print('='*30)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('='*30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('='*30)
print(f"A fortaleza está na {tabela.index('Fortaleza')+1}º posição\n")
