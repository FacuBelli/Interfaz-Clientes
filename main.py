import datetime




def opciones():
    opcion = int(input("\n1.Ver proyeccion anual de IVA\n2.Ver proyeccion mensual de IVA\n3.Cargar datos\n4.Buscar cliente\n¿Que accion quiere visualizar?: "))
    if opcion == 1:
        anual()
    elif opcion == 2:
        mensual()
    elif opcion == 3:
        cargarDatos(columnas, filas)
    else:
        buscarCliente()

def anual():
    print(matrizAnual)

def mensual():
    pass
def buscarCliente():
    pass
def cargarDatos(columnas, filas):

    matriz = [[0]* columnas for i in range(filas)]
    matriz[0][0] = 'Mes'
    matriz[0][1] = 'IVA Compras'
    matriz[0][2] = 'IVA Ventas'
    matriz[0][3] = 'Diferencia'

    for c in range (1,columnas):
        matriz[c][0] = str(input('Mes: '))
        matriz[c][1] = int(input('IVA Compras: '))
        matriz[c][2] = int(input('IVA Ventas: '))
        matriz[c][3] = (matriz[c][1] - matriz[c][2])

        




    
    def imprimirmatriz(matriz):
        for f in range(filas):
            for c in range(columnas):
                print("%7s" %matriz[f][c], end=" ")
            print()
    imprimirmatriz(matriz)

# Estructura de datos básica para representar clientes y transacciones
clientes = {
    "cliente1": {"transacciones": [(datetime.date(2023, 1, 5), 1000.0), (datetime.date(2023, 1, 15), 500.0)]},
    "cliente2": {"transacciones": [(datetime.date(2023, 1, 3), 1500.0), (datetime.date(2023, 1, 20), 800.0)]},
    # Agrega más clientes según sea necesario
}

# Función para calcular el IVA mensual y proyección anual para un cliente
def calcular_iva(cliente):
    iva_mensual = 0.0
    for fecha, monto in cliente["transacciones"]:
        # Asume una tasa de IVA del 10% (puedes ajustarla según las regulaciones locales)
        if fecha.month == datetime.date.today().month:
            iva_mensual += monto * 0.1

    iva_anual = sum(monto * 0.1 for _, monto in cliente["transacciones"])

    return iva_mensual, iva_anual

# Función para mostrar resultados
def mostrar_resultados(cliente, iva_mensual, iva_anual):
    print(f"Cliente: {cliente}")
    print(f"IVA Mensual: {iva_mensual}")
    print(f"Proyección Anual de IVA: {iva_anual}")
    print("\n")

# Calcular y mostrar resultados para cada cliente
for cliente, detalles in clientes.items():
    iva_mensual, iva_anual = calcular_iva(detalles)
    mostrar_resultados(cliente, iva_mensual, iva_anual)

columnas = 4
filas = 4
matrizAnual = [[0]*columnas for i in range(filas)]


opciones()