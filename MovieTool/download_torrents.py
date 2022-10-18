# Libraries
import feedparser
import requests



def download(search: str, jacket_host: str, jacket_apiKey: str, max_size = 2000):
    """
    Descarga los torrents de las peliculas con ayuda de este módulo.

    Params
    ====
    search: str | Nombre de la serie o película a buscar!

    jackett_host: str | El host dond está corriendo tu servidor de Jackett.

    jackett_apiKey: str | La API KEY de tu Jackett! La puedes encontrar arriba derecha de tú Jackett.

    max_size: int | Peso máximo (en MB) que podrán tener los archivos.
    """

    # Configuración inicial del string debúsqueda.
    busqueda = search.replace(' ', '+')
    
    # Configuraciones básicas. Es importante que, para empezar, se tiene que tener los trackers ya puestos en jackett.


    # A continuación extraigo la información de la serie (temporada y episodio) guiandome del formato SXXEXX que ya conociamos.
    serie_number_info = search.split(' ')[-1].upper()  # -1 porque,la temporada y episodio de la serie queda a lo último.


    parameters: str

    if 'S' in serie_number_info[0] and 'E' in serie_number_info[1:]:  # Desde acá, descartamos directamente el indice 0, ya que ya se validó y no lo necesitamos.

        # Extraemos el numero de temporada y episodio.
        season_number = serie_number_info[1:serie_number_info.find('E')]
        episode_number = serie_number_info[serie_number_info.find('E') + 1:]


        parameters = f'api/v2.0/indexers/all/results/torznab/api?apikey={jacket_apiKey}&cat=5000,5030,5040,5070,2000,2030,2040,2045,2070&t=search&q={busqueda[:busqueda.find(serie_number_info)]}&season={season_number}&ep={episode_number}'

        

    else:
        parameters = f'api/v2.0/indexers/all/results/torznab/api?apikey={jacket_apiKey}&t=search&q={busqueda}'
        






    # Validación de sí la url pasada contiene la típica "/" al fínal. Sí es así, se la eliminamos.
    if jacket_host[-1] == '/':
        url_consult = f'{jacket_host[:-1]}/{parameters}'  # ¡Url lista para consulta!

    else:
        url_consult = f'{jacket_host}/{parameters}'  # ¡Url lista para consulta!


    print(f'Haciendo la busqueda de {search} con la siguiente url: {url_consult}')



    # Accediendo!
    feed = feedparser.parse(url_consult)  # Se lee el RSS. ¡Devuelve una lista de diccionarios con los resultados!



    torrents = {}  # Diccionario para guardar los torrents


    for torrent in feed['entries']:
        torrents[torrent['title']] = [torrent['size'], torrent['link']]


    torrents_values = list(torrents.values())  # Los valores que contiene cada torrent. El peso y el magnet link
    torrents_name = list(torrents.keys())

    for size_count, size in enumerate(torrents_values):
        print(f'{size[0]} - {torrents_name[size_count]}')


download('Fall', 'http://mikoin.sytes.net:9117/', 'z96avavpt0rmbakcr7h2c85ir8ukw3dq')
