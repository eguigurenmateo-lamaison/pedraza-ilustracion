"""
Cuanto cuesta al ano la propuesta de Felipe, a volumen constante.
Compara lista vigente (1-ago) contra propuesta, usando el MISMO costo nuevo
en los dos escenarios: asi se aisla la decision de precio del cambio de costo.
"""
IVA = 1.19
def neto(p): return p / IVA

# unidades 18 meses (docs/correcciones-felipe-2026-08-01.md, seccion 2)
U18 = {'Puzzle 1000': 1837, 'Calcetines': 682, 'Naipes': 664, 'Botellas': 320,
       'Pins': 298, 'Llavero': 268, 'Totebag': 164, 'Libretas': 154, 'Postales': 144}
ANUAL = {k: v / 18 * 12 for k, v in U18.items()}

VIGENTE = {'Puzzle 1000': 29990, 'Calcetines': 9990, 'Naipes': 22990, 'Botellas': 32990,
           'Pins': 7990, 'Llavero': 9990, 'Totebag': 17990, 'Libretas': 18990, 'Postales': 11990}
PROPUESTA = {'Puzzle 1000': 27990, 'Calcetines': 9990, 'Naipes': 22990, 'Botellas': 27990,
             'Pins': 6500, 'Llavero': 7990, 'Totebag': 14990, 'Libretas': 18990, 'Postales': 11990}
COSTO = {'Puzzle 1000': 7463, 'Calcetines': 1148, 'Naipes': 3770, 'Botellas': 9651.16,
         'Pins': 1147, 'Llavero': 1710, 'Totebag': 5080, 'Libretas': 4200, 'Postales': 1702}

print('=' * 100)
print('CUANTO CUESTA LA PROPUESTA AL ANO, SI EL VOLUMEN NO CAMBIA')
print('=' * 100)
print(f"{'Producto':<14}{'Unid/ano':>9}{'Vigente':>9}{'Propuesta':>10}{'Margen hoy':>12}"
      f"{'Margen prop.':>13}{'Pierde/unidad':>14}{'Pierde/ano':>13}")
tot = 0; tot_venta_hoy = 0; tot_venta_prop = 0
filas = []
for p in VIGENTE:
    u = ANUAL[p]; c = COSTO[p]
    mv = neto(VIGENTE[p]) - c
    mp = neto(PROPUESTA[p]) - c
    d = (mv - mp) * u
    tot += d
    tot_venta_hoy += neto(VIGENTE[p]) * u
    tot_venta_prop += neto(PROPUESTA[p]) * u
    filas.append((d, p, u, mv, mp))
for d, p, u, mv, mp in sorted(filas, key=lambda x: -x[0]):
    print(f'{p:<14}{u:>9.0f}{VIGENTE[p]:>9,}{PROPUESTA[p]:>10,}{mv:>12,.0f}{mp:>13,.0f}'
          f'{mv-mp:>14,.0f}{d:>13,.0f}')
print(f"\n{'TOTAL':<14}{sum(ANUAL.values()):>9.0f}{'':>19}{'':>25}{'':>14}{tot:>13,.0f}")
print(f'\n-> La propuesta resigna ${tot:,.0f} de utilidad al ano a volumen constante.')
print(f'   (no incluye laminas: no hay unidades desglosadas para ellas)')

print(f'\nVenta neta anual: hoy ${tot_venta_hoy:,.0f} -> propuesta ${tot_venta_prop:,.0f} '
      f'({tot_venta_prop/tot_venta_hoy-1:+.1%})')

margen_hoy = sum((neto(VIGENTE[p]) - COSTO[p]) * ANUAL[p] for p in VIGENTE)
print(f'Utilidad bruta anual: hoy ${margen_hoy:,.0f} -> propuesta ${margen_hoy-tot:,.0f} '
      f'({(margen_hoy-tot)/margen_hoy-1:+.1%})')
print(f'\n-> Para recuperar esa utilidad con mas volumen hay que vender '
      f'{margen_hoy/(margen_hoy-tot)-1:+.1%} mas unidades.')

print()
print('=' * 100)
print('PRODUCTO POR PRODUCTO: DONDE LA BAJA SE JUSTIFICA Y DONDE NO')
print('=' * 100)
print(f"{'Producto':<14}{'Baja':>8}{'Margen prop.':>14}  {'Veredicto'}")
for p in sorted(VIGENTE, key=lambda x: PROPUESTA[x] / VIGENTE[x]):
    baja = PROPUESTA[p] / VIGENTE[p] - 1
    mp = (neto(PROPUESTA[p]) - COSTO[p]) / neto(PROPUESTA[p])
    if baja == 0:
        v = 'sin cambio'
    elif mp < 0.60:
        v = 'NO — cae bajo el piso de 60%'
    elif p == 'Puzzle 1000':
        v = 'NO — borra el colchon del alza (queda +2,4% sobre julio)'
    elif mp >= 0.70:
        v = 'se puede — el margen aguanta'
    else:
        v = 'revisar'
    print(f'{p:<14}{baja:>7.1%}{mp:>13.1%}  {v}')

print()
print('=' * 100)
print('LA ALTERNATIVA: BAJAR SOLO DONDE EL MERCADO LO PIDE')
print('=' * 100)
# Propuesta acotada: laminas si (fuera de esta tabla), pins/llavero/totebag segun margen,
# puzzle y botellas se mantienen.
ACOTADA = dict(VIGENTE)
ACOTADA['Pins'] = 6500       # margen queda 79%: aguanta y estaba +7% sobre mercado
ACOTADA['Llavero'] = 7990    # margen queda 74,5%
costo_acotada = sum((neto(VIGENTE[p]) - neto(ACOTADA[p])) * ANUAL[p] for p in VIGENTE)
print(f'Si se baja solo Pins y Llavero (los dos que aguantan el margen):')
print(f'  cuesta ${costo_acotada:,.0f}/ano en vez de ${tot:,.0f}/ano')
print(f'  se ahorra ${tot-costo_acotada:,.0f} y se evita que 3 productos caigan bajo el piso')
print(f'\nLos tres que la propuesta deja bajo el piso de 60%:')
for p, pr, c in (('Botellas', 27990, 9651.16), ('Totebag', 14990, 5080), ('Puzzle 60', 17990, 6599)):
    n = neto(pr); m = (n - c) / n
    # precio necesario para volver a 60%
    pmin = c / 0.40 * IVA
    print(f'  {p:<10} a ${pr:,} da {m:.1%}. Para llegar al 60% tendria que costar ${pmin:,.0f}')
