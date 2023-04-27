# Tuplas com times de futebol


times = ('Palmeiras','Internacional',"Fluminense","Corinthians","Flamengo","Athletico-PR","Atlético-MG","Fortaleza",
         "São Paulo","América-MG","Botafogo","Santos","Goiás","Red Bull Bragantino","Coritiba","Cuiabá",
         'Ceará',' Atlético-GO',' Avaí','Juventude')

print('-=-'*60)
print(f'Lista de times do Brasileirão : {times}')
print('-=-'*60)
print(f'Os 5 primeiros são : {times[0:5]}')
print('-=-'*60)
print(f'Os 4 últimos são : {times[17:]}')
print('-=-'*60)
print(f'Times em ordem alfabética : {sorted(times)}')
print('-=-'*60)
print(f'O flamengo está na {times.index("Flamengo")+1}° posição!')