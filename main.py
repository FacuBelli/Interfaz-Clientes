def opciones():
    try:
    
        opcion = int(input("\n1.Cargar compras\n2.Cargar ventas\n3.Generar reporte\n4.Buscar periodo Compras\n5.Buscar periodo Ventas\n6.IVA a pagar Total\n7.Consultar total de un periodo\n¿Que accion quiere visualizar?: "))
        
        #Validacion
        while opcion <= 0 or opcion > 7:
            opcion = int(input("Opcion no correcta. Estas son las opciones posibles:\n1.Cargar compras\n2.Cargar ventas\n3.Generar reporte\n4.Buscar periodo Compras\n5.Buscar periodo Ventas\n6.IVA a pagar Total\n7.Consultar total de un periodo\n¿Que accion quiere visualizar?: "))
        
        #Opciones
        if opcion == 1:
            cargarCompras(matriz,columnas)
        elif opcion == 2:
            cargaVentas(matriz)

        elif opcion == 3:
            generarReporte()
        elif opcion == 4:
            mes = str(input('Ingrese un mes: '))
            anio = str(input('Ingrese un año: '))
            buscarPeriodoCompras(mes,anio)
        elif opcion == 5:
            mes = str(input('Ingrese un mes: '))
            anio = str(input('Ingrese un año: '))
            buscarPeriodoVentas(mes,anio)
        elif opcion == 6:
            verDiferencia()
        elif opcion == 7:
            consultarTotales()

        else:
            print("El programa finalizo")
    except ValueError:
        print('Error, solo se permiten numeros. Intente nuevamente.')
        opciones()



def anual():
    print(matrizAnual)

#Cargar compras
def cargarCompras(matriz,columnas):
    try:

        archivoDatos = 'Compras.txt'

        matriz = [[0]* columnas for i in range(filas)]
        matriz[0][0] = 'Mes'
        matriz[0][1] = 'Año'
        matriz[0][2] = 'IVA Compras'
        with open(archivoDatos,'a') as archivo:
            while True:
                for c in range (1,columnas):
                    matriz[c][0] = input('Mes: ').lower()
                    while matriz[c][0] == '':
                        matriz[c][0] = input('Ingrese un mes valido: ').lower()
                    matriz[c][1] = '2023'
                    matriz[c][2] = (int(input(f'IVA Compras de {matriz[c][0]}: '))*0.21)

                    #Esto escribe los datos en el txt
                    linea = ','.join(map(str, matriz[c]))
                    archivo.write(linea + '\n')
                continuar = input("¿Desea cargar mas datos? (si/no): ")
                continuar=continuar.lower()
                if continuar == "si":
                    continue
                else:
                    break
    
        opciones()
    except ValueError:
        print("Error: Ingrese un dato válido.")
        cargarCompras(matriz,columnas)


#Cargar Ventas
def cargaVentas(matriz):
    try:

        archivoDatos = 'Ventas.txt'

        matriz = [[0]* columnas for i in range(filas)]
        matriz[0][0] = 'Mes'
        matriz[0][1] = 'Año'
        matriz[0][3] = 'IVA Ventas'
        with open(archivoDatos,'a') as archivo:
            while True:
                for c in range (1,columnas):
                    matriz[c][0] = input('Mes: ').lower()
                    while matriz[c][0] == '':
                        matriz[c][0] = input('Ingrese un mes valido: ').lower()
                    matriz[c][1] = '2023'
                    matriz[c][3] = (int(input(f'IVA Ventas de {matriz[c][0]}: '))*0.21)

                    #Esto escribe los datos en el txt
                    linea = ','.join(map(str, matriz[c]))
                    archivo.write(linea + '\n')
                continuar = input("¿Desea cargar mas datos? (si/no): ")
                continuar=continuar.lower()
                if continuar == "si":
                    continue
                else:
                    break
    
        opciones()
    except ValueError:
        print("Error: Ingrese un dato válido.")
        cargarCompras(matriz,columnas)

#Buscar periodo Compras      
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
        print(f"Error: No se encontró el archivo requerido")
    opciones()

#Buscar periodo Ventas
def buscarPeriodoVentas(mes, anio):
    try:
        with open('Ventas.txt', 'r') as archivo:
            for linea in archivo:
                elementos = linea.strip().split(',')
                if elementos[0] == mes and elementos[1] == str(anio):
                    print('Mes - Año - IVA Venta')
                    print(linea)
                    break
            else:
                print(f"No se encontró ninguna línea para el mes {mes} del {anio}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo requerido")
    opciones()


#Calcular iva a pagar
def verDiferencia():
    calcularIVAPagar()
    opciones()

def calcularIVAPagar():
    try:
        archivoCompras = 'Compras.txt'
        archivoVentas = 'Ventas.txt'
        
        ivaCompras = sumarIVACompras(archivoCompras)
        ivaVentas = sumarIVAVentas(archivoVentas)

        diferencia = ivaCompras - ivaVentas

        print(f"IVA a pagar: {diferencia:.2f}")
    except ValueError:
        print("Error: Ingrese un número válido.")


def sumarIVACompras(archivo):
    try:
        with open(archivo, 'r') as archivo_iva:
            iva_total = 0
            next(archivo_iva)  # Saltar la primera línea con encabezados
            for linea in archivo_iva:
                elementos = linea.strip().split(',')
                iva_total += float(elementos[2])  # Sumar el IVA de compras 
        return iva_total
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")


#Sumar IVA VENTAS
def sumarIVAVentas(archivo):
    try:
        with open(archivo, 'r') as archivo_iva:
            iva_total = 0
            next(archivo_iva)  # Saltar la primera línea con encabezados
            for linea in archivo_iva:
                elementos = linea.strip().split(',')
                iva_total += float(elementos[3])  # Sumar el IVA de Ventas
        return iva_total
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")

#Consultar Totales de un periodo
def consultarTotales():

    try:
        while True:
            mes = str(input('Ingrese el mes para consultar totales: ').lower())
            anio = str(input('Ingrese el año para consultar totales: '))

            if validarMes(mes):
                iva_compras = sumarIVAComprasPeriodo('Compras.txt', mes, anio)
                iva_ventas = sumarIVAVentasPeriodo('Ventas.txt', mes, anio)

                print(f"Total IVA Compras en {mes} del {anio}: {iva_compras:.2f}")
                print(f"Total IVA Ventas en {mes} del {anio}: {iva_ventas:.2f}")
                break
            else:
                print("Error: Mes inválido. Ingrese un mes válido.")
        
    except ValueError:
        print("Error: Ingrese un dato válido.")

    opciones()

#Validacion del mes ingresado
def validarMes(mes):
    meses_validos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return mes in meses_validos
# Funciones que me ayudan para sumar IVA en un periodo específico
def sumarIVAComprasPeriodo(archivo, mes, anio):
    try:
        with open(archivo, 'r') as archivo_iva:
            iva_total = 0

            for linea in archivo_iva:
                elementos = linea.strip().split(',')
                if elementos[0] == mes and elementos[1] == str(anio):
                    iva_total += float(elementos[2])  # Sumar el IVA de compras
        return iva_total
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")



def sumarIVAVentasPeriodo(archivo, mes, anio):
    try:
        with open(archivo, 'r') as archivo_iva:
            iva_total = 0
            for linea in archivo_iva:
                elementos = linea.strip().split(',')
                if elementos[0] == mes and elementos[1] == str(anio):
                    iva_total += float(elementos[3])  # Sumar el IVA de ventas
        return iva_total
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")
        return 0
    except Exception as e:
        print(f"Error inesperado: {e}")
        return 0



#Generar reporte
def generarReporte():
    try:
        mes = str(input('Ingrese el mes para generar el reporte: ').lower())
        anio = str(input('Ingrese el año para generar el reporte: '))

        with open('Reporte.txt', 'w') as archivo_reporte:
            archivo_reporte.write('Mes - Año - IVA Compras - IVA Ventas\n')

            iva_compras = sumarIVAComprasPeriodo('Compras.txt', mes, anio)
            iva_ventas = sumarIVAVentasPeriodo('Ventas.txt', mes, anio)

            linea_reporte = f'{mes} - {anio} - {iva_compras:.2f} - {iva_ventas:.2f}\n'
            archivo_reporte.write(linea_reporte)

        print(f"Reporte generado exitosamente en Reporte.txt")
    except ValueError:
        print("Error: Ingrese un dato válido.")
    opciones()
#Opcion XX
def cargarDatos(columnas, filas):
    archivoDatos = 'Datos.txt'

    matriz = [[0]* columnas for i in range(filas)]
    matriz[0][0] = 'Mes'
    matriz[0][1] = 'Año'
    matriz[0][2] = 'IVA Compras'
    matriz[0][3] = 'IVA Ventas'
    matriz[0][4] = 'Diferencia'
    with open(archivoDatos,'a') as archivo:
        while True:
            for c in range (1,columnas):
                matriz[c][0] = 'agosto'#str(input('Mes: ').lower())
                matriz[c][1] = '2023'
                matriz[c][2] = 234 #int(input(f'IVA Compras de {matriz[c][0]}: '))
                matriz[c][3] = 234 #int(input(f'IVA Ventas de {matriz[c][0]}: '))
                matriz[c][4] = (matriz[c][2] - matriz[c][3])
                #Esto escribe los datos en el txt
                linea = ','.join(map(str, matriz[c]))
                archivo.write(linea + '\n')
            continuar = input("¿Desea cargar mas datos? (si/no): ")
            continuar=continuar.lower()
            if continuar == "si":
                continue
            else:
                break

        opciones()




columnas = 5
filas = 5
matriz = [[0]* columnas for i in range(filas)]
matriz[0][0] = 'Mes'
matriz[0][1] = 'Año'
matriz[0][2] = 'IVA Compras'
matriz[0][3] = 'IVA Ventas'
matriz[0][4] = 'Diferencia'
opciones()