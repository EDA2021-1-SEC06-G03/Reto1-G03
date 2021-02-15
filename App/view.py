﻿"""
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
def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req 2")
    print("3- Req 3")
    print("4- Req 4")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        #time_1 = time.time()
        catalog = initCatalog()
        loadData(catalog)
        print("Cargando información de los archivos ....")
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        #time_2 = time.time()
        #print('Segundos de carga :{}'.format(str(time_2-time_1)))

    elif int(inputs[0]) == 2:
        pass
    
    elif int(inputs[0]) == 3:
        pass
    
    elif int(inputs[0]) == 4:
        pass

    else:
        sys.exit(0)
sys.exit(0)