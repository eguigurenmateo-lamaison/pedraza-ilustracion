"""
Impacto de la Escala de Valor nueva de Felipe sobre todo lo publicado.
Compara contra la lista del 1-ago que sostiene precio-venta.html.
"""
IVA = 1.19
def neto(p): return p / IVA

# Lista del 1-ago sobre la que se construyo precio-venta.html
VIEJO = {
    'Lamina A2 (42x60)': 52990, 'Lamina A3 (33x50)': 40990, 'Puzzle 1000': 29990,
    'Libretas': 18990, 'Llavero': 9990, 'Pins': 7990, 'Totebag': 17990,
    'Postales': 11990, 'Botellas': 32990, 'Naipes': 22990, 'Calcetines': 9990,
}
# Escala nueva (hoja Shopify)
NUEVO = {
    'Lamina A2 (42x60)': (36990, 8357), 'Lamina A3 (33x50)': (23990, 6261),
    'Puzzle 1000': (27990, 7463), 'Puzzle 60': (17990, 6599),
    'Libretas': (18990, 4200), 'Llavero': (7990, 1710), 'Pins': (6500, 1147),
    'Totebag': (14990, 5080), 'Postales': (11990, 1702), 'Botellas': (27990, 9651.16),
    'Naipes': (22990, 3770), 'Calcetines': (9990, 1148), 'Bandanas': (9990, 1080),
}
PRE_ALZA = {  # precio antes del 1-ago, para saber si el alza sigue en pie
    'Lamina A2 (42x60)': 48390, 'Lamina A3 (33x50)': 36980, 'Puzzle 1000': 27290,
    'Libretas': 17490, 'Llavero': 8790, 'Pins': 5490, 'Totebag': 16490,
    'Postales': 10990, 'Botellas': 28990, 'Naipes': 22990, 'Calcetines': 9390,
}

print('=' * 96)
print('1. LO QUE CAMBIO EN EL PRECIO — contra la lista del 1-ago que sostiene la pagina')
print('=' * 96)
print(f"{'Producto':<20}{'1-ago':>9}{'Nuevo':>9}{'Cambio':>9}   {'vs. precio ANTES del alza':<28}")
revertidos = []
for p, (pn, _) in NUEVO.items():
    pv = VIEJO.get(p)
    pre = PRE_ALZA.get(p)
    if pv is None:
        print(f'{p:<20}{"—":>9}{pn:>9,}{"nuevo":>9}   producto que no estaba en la lista')
        continue
    d = pn / pv - 1
    if pre:
        d2 = pn / pre - 1
        estado = f'{d2:+.1%} ' + ('POR DEBAJO del precio de julio' if d2 < 0 else 'sobre julio')
        if d2 <= 0.03: revertidos.append(p)
    else:
        estado = '—'
    print(f'{p:<20}{pv:>9,}{pn:>9,}{d:>8.1%}   {estado}')
print(f'\n-> El alza del 1-ago quedo revertida o casi en {len(revertidos)} de 11 productos: {revertidos}')

print()
print('=' * 96)
print('2. MARGENES REALES, AHORA QUE HAY COSTO DE LOS 13 PRODUCTOS')
print('=' * 96)
print(f"{'Producto':<20}{'Precio':>9}{'Neto':>10}{'Costo':>10}{'Margen $':>11}{'Margen %':>10}  {'piso 60%':<10}")
bajo_piso = []
for p, (pr, c) in sorted(NUEVO.items(), key=lambda x: (neto(x[1][0]) - x[1][1]) / neto(x[1][0])):
    n = neto(pr); m = n - c; pct = m / n
    alerta = 'BAJO PISO' if pct < 0.60 else ('justo' if pct < 0.63 else 'ok')
    if pct < 0.60: bajo_piso.append((p, pct))
    print(f'{p:<20}{pr:>9,}{n:>10,.0f}{c:>10,.0f}{m:>11,.0f}{pct:>9.1%}  {alerta:<10}')
print(f'\n-> Bajo el piso de 60% que fijo Felipe: {[(p, f"{v:.1%}") for p, v in bajo_piso]}')

print()
print('=' * 96)
print('3. EL PUZZLE: LO QUE DECIA LA PAGINA CONTRA LO QUE PASA AHORA')
print('=' * 96)
m_jul = neto(27290) - 7253          # antes del alza, costo viejo
m_ago = neto(29990) - 7253          # despues del alza, costo viejo  (base de la pagina)
m_hoy = neto(27990) - 7463          # escala nueva
print(f'Julio (antes del alza)   $27.290 - costo $7.253  -> margen ${m_jul:>9,.0f}')
print(f'1-ago (base de la pagina) $29.990 - costo $7.253  -> margen ${m_ago:>9,.0f}   (+{m_ago/m_jul-1:.1%})')
print(f'Escala nueva              $27.990 - costo $7.463  -> margen ${m_hoy:>9,.0f}   ({m_hoy/m_jul-1:+.1%} vs julio)')
print()
print(f'La pagina publica: "aguanta una caida de 12,6%" -> ese colchon era {1-m_jul/m_ago:.1%} y')
print(f'suponia precio $29.990. Con el precio nuevo el colchon real es {1-m_jul/m_hoy:.1%}.')
print('-> El argumento central de la pagina quedo sin base: el precio que defendia ya no existe.')
print(f'\nEl costo del puzzle ademas SUBIO: $7.253 -> $7.463 (+{7463/7253-1:.1%})')

print()
print('=' * 96)
print('4. LAMINAS: LA COMPARACION POR CENTIMETRO CUADRADO SE DA VUELTA')
print('=' * 96)
# A2 = 42x59,4 cm ; A3 = 29,7x42 cm (medidas ISO reales)
casos = [
    ('Pedraza A2 (nuevo)', 36990, 42 * 59.4), ('Pedraza A2 (1-ago)', 52990, 42 * 59.4),
    ('Pedraza A3 (nuevo)', 23990, 29.7 * 42), ('Pedraza A3 (1-ago)', 40990, 29.7 * 42),
    ('Torca 30x42 vigente', 20990, 30 * 42), ('Mappin 50x70', 39900, 50 * 70),
]
for nom, pr, cm2 in sorted(casos, key=lambda x: -x[1] / x[2]):
    print(f'  {nom:<22} ${pr:>7,}  {cm2:>7,.0f} cm2  ->  ${pr/cm2:>6.2f}/cm2')
a2n, a2v = 36990 / (42*59.4), 52990 / (42*59.4)
map_ = 39900 / (50*70); tor = 20990 / (30*42)
a3n, a3v = 23990 / (29.7*42), 40990 / (29.7*42)
print(f'\n  A2 contra Mappin: la pagina dice 1,8x (a $52.990) -> con el precio nuevo es {a2n/map_:.1f}x')
print(f'  A3 contra Torca:  la pagina dice +49% (a $40.990) -> con el precio nuevo es {a3n/tor-1:+.0%}')
print('  -> A los precios nuevos las laminas YA NO estan sobre el mercado. Estan en linea.')
print('  OJO: la pagina llamo "33x50" a la lamina chica; el archivo la llama A3 (29,7x42).')
print('       No es el mismo tamano: 1.650 cm2 contra 1.247 cm2. Hay que confirmar cual es.')

print()
print('=' * 96)
print('5. MERCADO LIBRE: LA DIFERENCIA POR CANAL SE VOLVIO INCOHERENTE')
print('=' * 96)
ML = {'Lamina A2': (56990, 9527.65), 'Puzzle 1000': (28990, 7253.28), 'Libretas': (18990, 7235),
      'Llavero': (10990, 1500), 'Pins': (8990, 915), 'Totebag': (18990, 5500),
      'Postales': (11990, 1823), 'Botellas': (35990, 9651.16), 'Naipes': (24990, 4578.45)}
SHOP = {'Lamina A2': 36990, 'Puzzle 1000': 27990, 'Libretas': 18990, 'Llavero': 7990,
        'Pins': 6500, 'Totebag': 14990, 'Postales': 11990, 'Botellas': 27990, 'Naipes': 22990}
print(f"{'Producto':<14}{'Shopify':>9}{'ML':>9}{'Brecha $':>10}{'Brecha %':>10}")
for p, (pml, _) in ML.items():
    ps = SHOP[p]
    print(f'{p:<14}{ps:>9,}{pml:>9,}{pml-ps:>10,}{pml/ps-1:>9.1%}')
print('\n-> La regla acordada era "ML entre $1.000 y $4.000 sobre la tienda propia".')
print('   Hoy va de $1.000 (puzzle) a $20.000 (lamina A2). No hay regla: hay dispersion.')
print('   Y el puzzle, con $1.000 de brecha, es el caso que la pagina ya marcaba como')
print('   insuficiente: hacen falta $6.700-$8.600 solo para igualar el margen del canal propio.')

print()
print('=' * 96)
print('6. LOS DOS ARCHIVOS SE CONTRADICEN EN EL COSTO DEL MISMO PRODUCTO')
print('=' * 96)
COMP = {'Lamina A2': (8357, 9527.65), 'Puzzle 1000': (7463, 7253.28), 'Libretas': (4200, 7235),
        'Llavero': (1710, 1500), 'Pins': (1147, 915), 'Totebag': (5080, 5500),
        'Postales': (1702, 1823), 'Botellas': (9651.16, 9651.16), 'Naipes': (3770, 4578.45)}
print(f"{'Producto':<14}{'hoja Shopify':>14}{'hoja ML':>12}{'diferencia':>12}{'':>4}")
for p, (cs, cm) in COMP.items():
    d = cm / cs - 1
    marca = '  <-- fuerte' if abs(d) > 0.15 else ''
    print(f'{p:<14}{cs:>14,.0f}{cm:>12,.0f}{d:>11.1%}{marca}')
print('\n-> El mismo producto no puede costar distinto segun donde se venda: el costo es de compra,')
print('   no de canal. Las diferencias de flete/comision van despues, no dentro del costo.')

print()
print('=' * 96)
print('7. LO QUE PASA CON EL TICKET Y EL ENVIO GRATIS')
print('=' * 96)
baja_media = sum(NUEVO[p][0] / VIEJO[p] - 1 for p in VIEJO if p in NUEVO) / len([p for p in VIEJO if p in NUEVO])
aov_nuevo = 37900 * (1 + baja_media)
print(f'Baja promedio simple de la lista: {baja_media:+.1%}')
print(f'Ticket promedio hoy $37.900 -> proyectado ${aov_nuevo:,.0f} si la mezcla no cambia 🟡')
print(f'Umbral de envio gratis $50.000: faltaba 32%, ahora faltaria {50000/aov_nuevo-1:.0%}')
print('-> El envio gratis queda todavia mas lejos del pedido promedio. O baja el umbral,')
print('   o la escalera por cantidad pasa a ser la unica forma de cruzarlo.')
print()
print(f'Escalera con el precio nuevo del puzzle ($27.990):')
for u, desc in ((1, 0), (2, 9000), (2, 6000), (3, 15000)):
    br = 27990 * u - desc
    cruza = 'SI' if br >= 50000 else 'no'
    print(f'  {u} puzzle(s) - ${desc:>6,} de descuento = ${br:>7,}  cruza envio gratis: {cruza}')
print('-> Con $9.000 de descuento 2 puzzles quedan en $46.980 y YA NO cruzan el umbral.')
print('   La correccion que hicimos (de $10.000 a $9.000) deja de servir con el precio nuevo.')
