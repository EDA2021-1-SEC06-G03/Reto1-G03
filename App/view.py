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

def loadData(catalog, estructura='ARRAY_LIST'):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def sub_lista(catalog['videos'],tamaño):
    

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
                estructura = 'SINGLE_LINKED_LIST'
            else:
                print("Por favor escoge una de las dos opciones")
        time_1 = time.process_time()
        catalog = initCatalog(estructura)
        loadData(catalog)
        print("Cargando información de los archivos ....")
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
        time_2 = time.process_time()
        print('Segundos de carga :{}'.format(str(time_2-time_1)))

    elif int(inputs[0]) == 2:
        number = input("Buscando los TOP ?: ")
        ha_escogido_tamaño = False
        while not ha_escogido_tamaño:
            print("Recuerda que hay " + str(lt.size(catalog['videos'])) + "libro cargados")
            tamaño = int(input(""))
            if tamaño <= lt.size(catalog['videos']):
                ha_escogido_tamaño = True
        sublista = sub_lista(catalog['videos'],tamaño)
        
    
    elif int(inputs[0]) == 3:
        channelname = input("Nombre del canal a buscar: ")
        pass
    
    elif int(inputs[0]) == 4:
        label = input("Categoria a buscar: ")
        pass

    else:
        sys.exit(0)
sys.exit(0)
