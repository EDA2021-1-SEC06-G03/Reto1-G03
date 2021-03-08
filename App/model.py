"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as selection
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(estructura):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categorias': None,}
    catalog['videos'] = lt.newList(estructura, cmpfunction=NotImplemented)
    catalog['categorias'] = lt.newList('ARRAY_LIST', cmpfunction=NotImplemented)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)

def addCategoria(catalog, cate):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(catalog['categorias'], cate)

# Funciones para creacion de datos

# Funciones de consulta
def subListVideos(catalog, pos, number):
    """
    Retorna sublista de videos
    """
    videos = catalog["videos"]
    
    return lt.subList(videos, pos, number)

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

#def cmpVideosBy_criterio(video1, video2):
#    return (float(video1['criterio']) > float(video2['criterio']))

# Funciones de ordenamiento

def sortList(tad_lista, metodo, orden):
    if orden == "vistas":
        funcion_comp = cmpVideosByViews
    '''
    if orden == "criterio"
        funcion_comp = cmpVideosBy_criterio
    '''
    if metodo == "shell":
        shell.sort(tad_lista, funcion_comp)
    if metodo == "selection":
        selection.sort(tad_lista, funcion_comp)
    if metodo == "insertion":
        insertion.sort(tad_lista, funcion_comp)
    if metodo == "quick":
        quick.sort(tad_lista, funcion_comp)
    if metodo == "merge":
        merge.sort(tad_lista, funcion_comp)
