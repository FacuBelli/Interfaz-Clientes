def opciones():
    try:
    
        opcion = int(input("\n1.Cargar compras\n2.Cargar ventas\n3.Cargar datos\n4.Buscar periodo\n5.Cancelar\n¿Que accion quiere visualizar?: "))
        
        #Validacion
        while opcion <= 0 or opcion > 5:
            opcion = int(input("Opcion no correcta. Estas son las opciones posibles:\n1.Cargar compras\n2.Cargar ventas\n3.Cargar datos\n4.Buscar periodo\n¿Que accion quiere visualizar?: "))
        
        #Opciones
        if opcion == 1:
            cargarCompras(matriz,columnas)
        elif opcion == 2:
            cargaVentas(matriz)
        elif opcion == 3:
            cargarDatos(columnas, filas)
        elif opcion == 4:
            mes = str(input('Ingrese un mes: '))
            anio = str(input('Ingrese un año: '))
            buscarPeriodoCompras(mes,anio)
        elif opcion == 5:
            verDiferencia()
            pass
        else:
            print("El programa finalizo")
    except ValueError:
        print('Error, solo se permiten numeros. Intente nuevamente.')
        opciones()



def anual():
    print(matrizAnual)

#Opcion 1
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


#Opcion 2
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
                    matriz[c][3] = (int(input(f'IVA Compras de {matriz[c][0]}: '))*0.21)

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

#Opcion 3        
def buscarPeriodoCompras(mes, anio):
    try:
        with open('pindongo.txt', 'r') as archivo:
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
    except Exception as e:
        print(f"Error inesperado: {e}")
        opciones()

#Opcion 4
def verDiferencia():
    pass



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