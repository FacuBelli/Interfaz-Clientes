




def opciones():
    opcion = int(input("\n1.Ver proyeccion anual de IVA\n2.Ver proyeccion mensual de IVA\n3.Cargar datos\n4.Buscar periodo\n¿Que accion quiere visualizar?: "))
    if opcion == 1:
        anual()
    elif opcion == 2:
        mensual()
    elif opcion == 3:
        cargarDatos(columnas, filas)
    else:
        mes = str(input('Ingrese un mes: '))
        anio = str(input('Ingrese un año: '))
        buscarPeriodo(mes,anio)

def anual():
    print(matrizAnual)

def mensual():
    pass
def buscarPeriodo(mes, anio):
    with open('Datos.txt', 'r') as archivo:
        # Iterar sobre las líneas del archivo
        for linea in archivo:
            # Dividir la línea en elementos utilizando la coma como delimitador
            elementos = linea.strip().split(',')
            
            # Verificar si el mes y año coinciden con los parámetros
            if elementos[0] == mes and elementos[1] == str(anio):
                # Imprimir la línea encontrada y salir del bucle
                print('Mes - Año - IVA Compra - IVA Venta - Diferencia')
                for i in range (len(elementos)):
                    print(elementos[i], end = "         ")
                break
        else:
            # Este bloque se ejecuta si el bucle no se rompe, es decir, si no se encontró la línea
            print(f"No se encontró ninguna línea para el mes {mes} del {anio}")
    pass
def cargarDatos(columnas, filas):
    archivoDatos = 'Datos.txt'

    
    matriz = [[0]* columnas for i in range(filas)]
    matriz[0][0] = 'Mes'
    matriz[0][1] = 'Año'
    matriz[0][2] = 'IVA Compras'
    matriz[0][3] = 'IVA Ventas'
    matriz[0][4] = 'Diferencia'

    with open(archivoDatos,'a') as archivo:
        for c in range (1,columnas):
            matriz[c][0] = str(input('Mes: '))
            matriz[c][1] = '2023'
            matriz[c][2] = int(input(f'IVA Compras de {matriz[c][0]}: '))
            matriz[c][3] = int(input(f'IVA Ventas de {matriz[c][0]}: '))
            matriz[c][4] = (matriz[c][2] - matriz[c][3])

            #Esto escribe los datos en el txt

            linea = ','.join(map(str, matriz[c]))
            archivo.write(linea + '\n')

    
    def imprimirmatriz(matriz):
        for f in range(filas):
            for c in range(columnas):
                print("%7s" %matriz[f][c], end=" ")
            print()
    imprimirmatriz(matriz)



# Función para mostrar resultados
# def mostrar_resultados(cliente, iva_mensual, iva_anual):
#     print(f"Cliente: {cliente}")
#     print(f"IVA Mensual: {iva_mensual}")
#     print(f"Proyección Anual de IVA: {iva_anual}")
#     print("\n")

# # Calcular y mostrar resultados para cada cliente
# for cliente, detalles in clientes.items():
#     iva_mensual, iva_anual = calcular_iva(detalles)
#     mostrar_resultados(cliente, iva_mensual, iva_anual)

columnas = 5
filas = 5
matrizAnual = [[0]*columnas for i in range(filas)]


opciones()