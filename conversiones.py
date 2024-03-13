import sys
from tabulate import tabulate

sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
valor_a_convertir = float(sys.argv[4])

diccionario = {
    'Sol peruano': valor_a_convertir * sol_peruano,
    'Peso Argentino': valor_a_convertir * peso_argentino,
    'Dólar Americano': valor_a_convertir * dolar_americano
}

# Crear una lista de tuplas para tabular los resultados
tabla_resultados = [(moneda, valor) for moneda, valor in diccionario.items()]

# Imprimir la tabla utilizando tabulate
print(tabulate(tabla_resultados, headers=['Moneda', 'Valor Convertido'], tablefmt='pretty'))
