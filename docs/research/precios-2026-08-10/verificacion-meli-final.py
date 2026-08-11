"""
Verificacion de la tabla final de Felipe (11-ago-2026).
1) Los 11 margenes de Shopify.
2) Reconstruccion de los margenes de Mercado Libre y el doble conteo del envio.
"""
IVA = 1.19
def neto(p): return p / IVA

COSTO = {'Puzzle 1000': 7463, 'Puzzle Ninos': 6599, 'Botella': 9651.16, 'Naipes': 3770,
         'Pin': 1147, 'Llavero': 1710, 'Lamina A3': 6261, 'Lamina A2': 8357,
         'Totebag': 5080, 'Libretas': 4200, 'Postales': 1702}
SHOP = {'Puzzle 1000': (27990, .683), 'Puzzle Ninos': (18990, .586), 'Botella': (27990, .590),
        'Naipes': (22990, .805), 'Pin': (5990, .772), 'Llavero': (7990, .745),
        'Lamina A3': (23990, .689), 'Lamina A2': (36990, .731), 'Totebag': (15290, .605),
        'Libretas': (16990, .706), 'Postales': (11990, .831)}
ML = {'Puzzle 1000': (29490, .464), 'Botella': (29490, .394), 'Naipes': (24490, .575),
      'Lamina A3': (25990, .523), 'Lamina A2': (39990, .561), 'Pin': (6490, .599),
      'Llavero': (8990, .583), 'Totebag': (16490, .482), 'Libretas': (18990, .558)}
UMBRAL_ML, ENV = 19990, 3250

print('1. MARGENES DE SHOPIFY')
malos = 0
for p, (pr, dicho) in SHOP.items():
    n = neto(pr); m = (n - COSTO[p]) / n
    ok = abs(m - dicho) < 0.003
    malos += not ok
    print(f'  {p:<14}{pr:>8,}  calculo {m:>6.1%}  dice {dicho:>6.1%}  {"OK" if ok else "REVISAR"}')
print(f'  -> {len(SHOP)-malos} de {len(SHOP)} cuadran\n')

print('2. MERCADO LIBRE: comision implicita segun cuanto envio se reste')
print(f'   (bajo ${UMBRAL_ML:,} no hay obligacion de envio gratis, asi que no cargan envio)')
for p, (pr, m) in ML.items():
    n = neto(pr); paga = pr >= UMBRAL_ML
    c_media = (n - COSTO[p] - (ENV / 2 if paga else 0) - m * n) / pr
    c_full  = (n - COSTO[p] - (ENV     if paga else 0) - m * n) / pr
    print(f'  {p:<14}{pr:>8,}  dice {m:>6.1%}  | media {c_media:>6.1%}  completo {c_full:>6.1%}')

print('\n3. MARGEN CORREGIDO restando el envio completo (solo los sobre el umbral)')
for p, (pr, m) in ML.items():
    if pr < UMBRAL_ML: continue
    n = neto(pr)
    com = (n - COSTO[p] - ENV / 2 - m * n) / pr     # comision implicita de su propio calculo
    real = (n - COSTO[p] - ENV - pr * com) / n
    print(f'  {p:<14} {m:>6.1%} -> {real:>6.1%}  ({(real-m)*100:>5.1f} puntos)')

print('\n4. BRECHA DE MARGEN ENTRE CANALES')
br = sorted(((SHOP[p][1] - m, p) for p, (pr, m) in ML.items()))
for d, p in br:
    print(f'  {p:<14} {d*100:>5.1f} puntos')
print(f'  -> rango real {br[0][0]*100:.1f} a {br[-1][0]*100:.1f}; Felipe lo describe como "12 a 20"')

print('\n5. PUZZLE DE NINOS EN MERCADO LIBRE (mismo precio que Shopify, no traspasa nada)')
n = neto(18990)
for com in (0.12, 0.145, 0.17):
    print(f'  comision {com:.1%}: margen {(n-6599-ENV-18990*com)/n:.1%}')
