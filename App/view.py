"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog(estructura):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(estructura)

def loadData(catalog, size_videos: int, estructura='ARRAY_LIST'):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog, size_videos)



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar top x videos por vistas")
    print("3- Consultar los videos de un canal")
    print("4- Videos por categoria")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("¿Cual estructura de datos deseas usar para guardar los videos?")
        ha_escogido = False
        while not ha_escogido:
            print("1: Arreglo (Recomendado)")
            print("2: Lista Enlazada")
            escogencia = str(input(""))
            if escogencia == "1":
                ha_escogido = True
                estructura = 'ARRAY_LIST'
            elif escogencia == "2":
                ha_escogido = True
                estructura = 'LINKED_LIST'
            else:
                print("Por favor escoge una de las dos opciones")
        
        print("Cuantos videos desea cargar maximo: ")
        cantidad_datos = int(input(""))
        print("Cargando información de los archivos ....")
        if cantidad_datos >= 375942:
            print("Espera mientras se cargan todos los datos, recuerda que el archivo Large tiene {} videos".format(str(375942)))
        time_1 = time.process_time()
        catalog = initCatalog(estructura)
        loadData(catalog, cantidad_datos)
        time_2 = time.process_time()
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
        print('Milisegundos de carga :{}'.format(str((time_2-time_1)*1000)))
        

    elif int(inputs[0]) == 2:
        n = lt.size(catalog['videos'])
        print("Buscando los TOP ?: ")
        ha_escogido_tamaño = False
        while not ha_escogido_tamaño:
            tamaño = int(input(""))
            if tamaño <= n:
                ha_escogido_tamaño = True
            else:
                print("Recuerda que hay " + str(n) + "libro cargados")
        print("¿Cual algoritmo deseas usar para organizar los videos?")
        ha_escogido_metodo = False
        print("1: Shell Sort (Recomendado)")
        print("2: Selection Sort")
        print("3: Insertion Sort")
        print("4: Quick (Recomendado) Sort")
        print("5: Merge (Recomendado) Sort")
        while not ha_escogido_metodo:
            escogencia = str(input(""))
            if escogencia == "1":
                ha_escogido_metodo = True
                metodo = 'shell'
            elif escogencia == "2":
                ha_escogido_metodo = True
                metodo = 'selection'
            elif escogencia == "3":
                ha_escogido_metodo = True
                metodo = 'insertion'
            elif escogencia == "4":
                ha_escogido_metodo = True
                metodo = 'quick'
            elif escogencia == "5":
                ha_escogido_metodo = True
                metodo = 'merge'
            else:
                print("Por favor escoge una de las tres opciones de algoritmos de ordenamiento")
        print("Organizando datos con {}sort, por favor espera...".format(str(metodo)))
        time_1 = time.process_time()
        mas_vistos = controller.getMostViewed(catalog, tamaño, metodo)
        time_2 = time.process_time()
        posicion_imprimir = 1
        for video in lt.iterator(mas_vistos):
            print(str(posicion_imprimir),":" + "Titulo:" + video["title"] + "Vistas:" + video["views"])
            posicion_imprimir += 1
        
        print('Milisegundos de carga :{}'.format(str((time_2-time_1)*1000)))
        
    
    elif int(inputs[0]) == 3:
        channelname = input("Nombre del canal a buscar: ")
        pass
    
    elif int(inputs[0]) == 4:
        label = input("Categoria a buscar: ")
        pass

    else:
        sys.exit(0)
sys.exit(0)
