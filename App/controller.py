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
 """

import config as cf
import model
import csv
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos
def initCatalog(estructura):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(estructura)
    return catalog

# Funciones para la carga de datos
def loadData(catalog, size_videos: int):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog, size_videos)
    loadCategorias(catalog)
    #sortVideos(catalog, shell, vistas)


def loadVideos(catalog, size_videos: int):
    """
    Carga los videos del archivo.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    contador_datos = 0
    for video_leido in input_file:
        video_agregar = {}
        info_deseada = ['title','video_id', 'trending_date', 'category_id', 'views', 'channel_title', 'trending_date',\
             'country', 'likes', 'dislikes']
        for info in info_deseada:
            video_agregar[info] = video_leido[info]
        model.addVideo(catalog, video_agregar)
        contador_datos += 1
        if contador_datos >= size_videos:
            break

def loadCategorias(catalog):
    """
    Carga las categorias del archivo.
    """
    catsfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(catsfile, encoding='utf-8'), delimiter = '\t')
    for cate_leida in input_file:
        model.addCategoria(catalog, cate_leida)



# Funciones de ordenamiento
def sortVideos(tad_lista, metodo, orden):
    """
    Ordena los videos por views
    metodo se refiere al algoritmo de sorting
    orden se refiere al criterio por el que se ordena: revisar las opciones en model.sortVideos
    """
    model.sortList(tad_lista, metodo, orden)

# Funciones de consulta sobre el catálogo

def subListVideos(catalog, pos, number):
    return model.subListVideos(catalog, pos, number)


def getMostViewed(catalog, number, metodo="shell"):
    """
    Primero organiza todos los videos por vistas 
    Retorna una sublista de los videos mas vistos
    """
    sublista = subListVideos(catalog, 1, number)
    sortVideos(sublista, metodo, "vistas")

    return sublista

def primer_video(catalog):
    return model.primer_video(catalog)