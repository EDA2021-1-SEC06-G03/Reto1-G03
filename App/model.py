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
               'categorias': None,
               'paises': None}
    catalog['videos'] = lt.newList(estructura)
    catalog['categorias'] = lt.newList(datastructure = 'ARRAY_LIST')
    catalog['paises'] = lt.newList(datastructure = 'ARRAY_LIST')
    catalog['videos_distintos'] = lt.newList(datastructure = 'ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)

def addCategoria(catalog, cate):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(catalog['categorias'], cate)

def addPais(catalog, pais):
    # Se adiciona el pais a la lista de paises
    lt.addLast(catalog['paises'], pais)




# Funciones para creacion de datos
def loadPaises(catalog):
    for video in lt.iterator(catalog['videos']):
        pais = str(video['country']).lower()
        if not (pais_presente(catalog, pais)):
            addPais(catalog, pais)

# Funciones de consulta
def subListVideos(catalog, pos, number):
    """
    Retorna sublista de videos
    """
    videos = catalog["videos"]
    
    return lt.subList(videos, pos, number)

def primer_video(catalog):
    return lt.firstElement(catalog['videos'])

def pais_presente(catalog, pais:str):
    return lt.isPresent(catalog['paises'], pais)

def categoria_id_presente(catalog, categoria_id:str):
    id_presente = False
    for categoria in lt.iterator(catalog['categorias']):
        if categoria['id'] == categoria_id:
            id_presente = True
    return id_presente

def subListVideos_porCategoria(tad_lista, categoria_id:str):
    sublist = lt.newList(datastructure = tad_lista['type'])
    for video in lt.iterator(tad_lista):
        
        if str(video['category_id']) == categoria_id:
            lt.addLast(sublist, video)
    return sublist

def subListVideos_porPais(tad_lista, pais:str):
    sublist = lt.newList(datastructure = tad_lista['type'])
    for video in lt.iterator(tad_lista):
        if video['country'] == pais:
            lt.addLast(sublist, video)
    return sublist

def ObtenerVideosDistintos(tad_lista):
    videos_distintos = lt.newList(datastructure = 'ARRAY_LIST', cmpfunction = cmpVideosByVideoID)
    primero = lt.firstElement(tad_lista)
    primero['repeticiones'] = 1
    lt.addLast(videos_distintos, primero)
    for video in lt.iterator(tad_lista):
        video_agregar = {}
        info_deseada = ['title','video_id', 'category_id', 'views', 'channel_title', \
'country', 'likes', 'dislikes', 'publish_time']
        
        for info in info_deseada:
            video_agregar[info] = video[info]
        if   lt.lastElement(videos_distintos)['video_id'] == video_agregar['video_id']:
                lt.lastElement(videos_distintos)['repeticiones'] = lt.lastElement(videos_distintos)['repeticiones'] + 1
        else :
            video_agregar['repeticiones'] = 1
            lt.addLast(videos_distintos, video_agregar)
    return videos_distintos

'''def getRepeticiones(sublista, distintos_en_sublista):
    for video_unico in lt.iterator(distintos_en_sublista):
        encontrado = False
        repeticiones = 0
        for video in lt.iterator(sublista):
            if video['video_id'] == video_unico['video_id']:
                encontrado = True
                repeticiones += 1
            else:
                if encontrado == True:
                    break
        video_unico['repeticiones'] = repeticiones'''



def getMaxReps(sublista):
    if not lt.isEmpty(sublista):
        maximo_valor = 0
        maximo_apuntador = lt.firstElement(sublista)
        for video in lt.iterator(sublista):
            if video['repeticiones'] >= maximo_valor:
                maximo_valor = video['repeticiones']
                maximo_apuntador = video
        return maximo_apuntador
    else:
        return None



            



# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (int(video1['views']) > int(video2['views']))

def cmpVideosByVideoID(video1, video2):
    return (str(video1['video_id']) > str(video2['video_id']))

#def cmpVideosBy_criterio(video1, video2):
#    return (float(video1['criterio']) > float(video2['criterio']))

# Funciones de ordenamiento

def sortList(tad_lista, metodo, orden):
    if orden == "vistas":
        funcion_comp = cmpVideosByViews
    if orden == "video_id":
        funcion_comp = cmpVideosByVideoID
    '''
    if orden == "criterio"
        funcion_comp = cmpVideosBy_criterio
    '''
    #se puede hacer mas elegante haciendo un diccionario de funciones como valores y los nombres como llaves
    #tanto lo del criterio como lo de los metodos
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



'''lista = lt.newList()
lt.addLast(lista, {'.':'fecha7', 'video_id': 'id2'})
lt.addLast(lista, {'.':'fecha6', 'video_id': 'id3'})
lt.addLast(lista, {'.':'fecha2', 'video_id': 'id1'})
lt.addLast(lista, {'.':'fecha1', 'video_id': 'id1'})
lt.addLast(lista, {'.':'fecha4', 'video_id': 'id1'})
lt.addLast(lista, {'.':'fecha5', 'video_id': 'id1'})
lt.addLast(lista, {'.':'fecha3', 'video_id': 'id2'})

sortList(lista, 'merge', 'video_id')
distintos = ObtenerVideosDistintos(lista)
for i in lt.iterator(lista):
    print(i['video_id'])

print(getMaxReps(distintos))
print('')
for i in lt.iterator(distintos):
    print(i['video_id'])'''
