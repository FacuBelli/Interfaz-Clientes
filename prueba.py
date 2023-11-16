def opciones():
    try:
        opcion = int(input("\n1.Cargar compras\n2.Cargar ventas\n3.Cargar datos\n4.Buscar periodo\n5.Cancelar\n¿Qué acción quiere visualizar?: "))
        
        while opcion <= 0 or opcion > 5:
            opcion = int(input("Opción no correcta. Estas son las opciones posibles:\n1.Cargar compras\n2.Cargar ventas\n3.Cargar datos\n4.Buscar periodo\n¿Qué acción quiere visualizar?: "))

        if opcion == 1:
            cargarCompras()
        elif opcion == 2:
            cargaVentas()
        elif opcion == 3:
            cargarDatos()
        elif opcion == 4:
            mes = str(input('Ingrese un mes: '))
            anio = str(input('Ingrese un año: '))
            buscarPeriodoCompras(mes, anio)
        elif opcion == 5:
            verDiferencia()
        else:
            print("El programa finalizó")
    except ValueError:
        print("Error: Ingrese un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def cargarCompras():
    try:
        archivoDatos = 'Compras.txt'
        matriz = [['Mes', 'Año', 'IVA Compras']]

        with open(archivoDatos, 'a') as archivo:
            while True:
                mes = str(input('Mes: ').lower())
                anio = '2023'
                iva_compras = int(input(f'IVA Compras de {mes}: ')) * 0.21

                matriz.append([mes, anio, iva_compras])

                linea = ','.join(map(str, matriz[-1]))
                archivo.write(linea + '\n')

                continuar = input("¿Desea cargar más datos? (si/no): ").lower()
                if continuar != "si":
                    break
    except ValueError:
        print("Error: Ingrese un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    opciones()

def cargaVentas():
    try:
        archivoDatos = 'Ventas.txt'
        matriz = [['Mes', 'Año', 'IVA Ventas']]

        with open(archivoDatos, 'a') as archivo:
            while True:
                mes = str(input('Mes: ').lower())
                anio = '2023'
                iva_ventas = int(input(f'IVA Ventas de {mes}: ')) * 0.21

                matriz.append([mes, anio, iva_ventas])

                linea = ','.join(map(str, matriz[-1]))
                archivo.write(linea + '\n')

                continuar = input("¿Desea cargar más datos? (si/no): ").lower()
                if continuar != "si":
                    break
    except ValueError:
        print("Error: Ingrese un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    opciones()

def buscarPeriodoCompras(mes, anio):
    try:
        with open('Compras.txt', 'r') as archivo:
            for linea in archivo:
                elementos = linea.strip().split(',')
                if elementos[0] == mes and elementos[1] == str(anio):
                    print('Mes - Año - IVA Compra')
                    print(linea)
                    break
            else:
                print(f"No se encontró ninguna línea para el mes {mes} del {anio}")
    except FileNotFoundError:
        print("Error: No se encontró el archivo Compras.txt.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def verDiferencia():
    print("Función no implementada")

def cargarDatos():
    try:
        archivoDatos = 'Datos.txt'
        matriz = [['Mes', 'Año', 'IVA Compras', 'IVA Ventas', 'Diferencia']]

        with open(archivoDatos, 'a') as archivo:
            while True:
                mes = 'agosto'
                anio = '2023'
                iva_compras = 234
                iva_ventas = 234
                diferencia = iva_compras - iva_ventas

                matriz.append([mes, anio, iva_compras, iva_ventas, diferencia])

                linea = ','.join(map(str, matriz[-1]))
                archivo.write(linea + '\n')

                continuar = input("¿Desea cargar más datos? (si/no): ").lower()
                if continuar != "si":
                    break

        opciones()

    except ValueError:
        print("Error: Ingrese un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

columnas = 5
filas = 5
opciones()
