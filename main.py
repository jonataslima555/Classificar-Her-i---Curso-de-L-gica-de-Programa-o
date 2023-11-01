client = input('Digite seu nome: ')
xp = int(input('Digite sua experiência: '))

elo_map = {
    (0, 1000): 'Ferro',
    (1001, 2000): 'Bronze',
    (2001, 5000): 'Prata',
    (6001, 7000): 'Ouro',
    (7001, 8000): 'Platina',
    (8001, 9000): 'Ascendente',
    (9001, 10000): 'Imortal',
    (10001, float('inf')): 'Radiante'
}

elo = None

for xp_range, elo_name in elo_map.items():
    min_xp, max_xp = xp_range
    if min_xp <= xp <= max_xp:
        elo = elo_name
        break

if elo is not None:
    print(f'O Herói de nome {client} está no nível de {elo}')
else:
    print('Experiência fora das faixas especificadas')
