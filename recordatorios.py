from tabulate import tabulate

recordatorios = [
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
    ['2021-01-02', '06:00', 'Empezar el año'],
    ['2021-07-16', '13:00', 'No hacer nada es feriado'],
    ['2021-09-18', '16:00', 'Ramadas'],
    ['2021-12-25', '00:00', 'Navidad']
]

cena_navidad = ['2021-12-24', '22:00', 'Cena de Navidad']
cena_ano_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo']

recordatorios.append(cena_navidad)
recordatorios.append(cena_ano_nuevo)

# Ordenar la lista de recordatorios por la columna fecha
#La función lambda toma cada sublista x y devuelve x[0], que es la fecha. Por lo tanto, sorted ordenará la lista de recordatorios 
#basándose en la fecha.
recordatorios_ordenados = sorted(recordatorios, key=lambda x: x[0])

# Imprimir la tabla ordenada utilizando tabulate
print(tabulate(recordatorios_ordenados, headers=['Fecha', 'Hora', 'Tarea'], tablefmt='pretty'))
