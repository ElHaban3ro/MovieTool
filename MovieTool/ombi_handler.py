import requests
from datetime import date


# ombi_login = requests.post('http://mikoin.sytes.net:5000/api/v1/Logging')


def ombi_requests(api_key: str, host: str, ssl: bool, port: int):
    """
    Usa este módulo como handler de tu servidor ombi y resivir las peliculas o series que se piden. Por ahora solo soporta las series, pero se está trabajando para hacerlo compatible con peliculas de igual forma.


    Params
    =======
    api_key: Clave de la api de OMBI. Importante para efectuar correctamente las consultas.

    host: Dirección url donde está corriendo tu OMBI. Puede ser
          ingresado con el protocolo https o sin él. De cualquier manera
          especificar en el siguiente parametro.

    ssl: Proporciona información de sí tu servidor OMBI corre en un ambiente "seguro".

    port: Puerto donde está corriendo tu servidor OMBI.
    """

    # Si la url contiene un '/' al final, se lo sacamos para poder añadir el puerto.

    if host[-1] == '/':
        host = host[:-1]

    host = f'{host}:{port}'

    # ¡Si la url no contiene ningún protocolo, se lo añadimos!
    if 'http://' in host or 'https://' in host:
        protocol: bool = True


    else:
        protocol: bool = False

        if not ssl:
            host = f'http://{host}'

        elif ssl:
            host = f'https://{host}'

    ombi_header = {'ApiKey': api_key}

    # Aquí hacemos la petición a la API.
    ombi_api_response = requests.get(f'{host}/api/v1/Request/tv', params=ombi_header)
    tv_requests = ombi_api_response.json()  # Esto nos devolvería ya las pelis que se han pedido.
    # Claramente en formato JSON.

    # PARA LAS PETICIONES DE SERIES.
    # No son lo mismo que las peliculas, ya que en ocaciones, algunos
    # capitulos de la serie no se han publicado.

    # Diccionario de la cola.
    cola = {}

    capitulos_publicados = []
    show_incomplete = []

    complete: bool = True

    # Añadimos la serie a la cola!
    for show in tv_requests:
        show_status = show['childRequests'][0]['requestStatus'].split('.')[1]
        show_title = show['title']
        show_seasons = show['totalSeasons']
        show_S_requests = show['childRequests'][0]['seasonRequests']
        show_request_ombi = show['childRequests'][0]['parentRequestId']

        complete = True

        for season in show['childRequests'][0]['seasonRequests']:
            charapters = []

            season_number = season['seasonNumber']

            if season_number >= 10:
                season_number = f"S{season['seasonNumber']}"

            else:
                season_number = f"S0{season['seasonNumber']}"

            for episode in season['episodes']:
                episode_number = episode['episodeNumber']

                if episode_number >= 10:
                    episode_number = f"E{episode['episodeNumber']}"

                else:
                    episode_number = f"E0{episode['episodeNumber']}"

                today = str(date.today())
                today_split = today.split('-')  # Spliteado en: Año/Mes/Día.

                pub = episode['airDate'].split('T')[0]
                pub_split = pub.split('-')  # Spliteado en: Año/Mes/Día.

                episode_se = f'{season_number}{episode_number}'

                if pub_split[0] <= today_split[0]:  # Si el año es menor o el mismo que el actual:

                    if pub_split[0] == today_split[0]:  # Si el año es el mismo,
                        # el mes de pub tiene que ser IGUAL o menor al actual.
                        if pub_split[1] <= today_split[1]:

                            if pub_split[1] == today_split[1]:
                                if pub_split[2] < today_split[2]:  # Si el día de publicación es menor que el actual:
                                    capitulos_publicados.append(True)
                                    complete = True

                                else:
                                    capitulos_publicados.append(False)
                                    complete = False


                            else:
                                capitulos_publicados.append(True)
                                complete = True


                        else:
                            capitulos_publicados.append(False)
                            complete = False

                    else:
                        capitulos_publicados.append(True)
                        complete = True

                    charapters.append(f'{show_title} {episode_se}')

            if complete:
                show_incomplete.insert(0, f'{show_title} {season_number}')

            else:
                for i in charapters:
                    show_incomplete.append(i)

        print(complete)

        show_seasons_list = []

        for S in show_S_requests:
            show_seasons_list.append(f"{S['seasonNumber']}")

        if show_status == 'ProcessingRequest':
            cola[show_title] = {'total seasons': show_seasons, 'season request': show_seasons_list,
                                'id': show_request_ombi}

    show_season = []

    # Para meter dentro de la lista "show_season", una lista con los strings del
    # nombre de la serie y su debido número de temporadas. Mire más abajo el ejemplo de lista que devuelve.
    for show in cola:
        show_list = []

        request_name = ''

        request_id = ''
        for season_info in cola[show]['season request']:
            if len(season_info) == 1:
                season_info = f'S0{season_info}'

            else:
                season_info = f'S{season_info}'

            show_list.append(f'{show} {season_info}')

            request_id = cola[show]['id']

            request_name = show

        show_list.append(request_id)
        show_incomplete.append(request_id)

        show_list.append(request_name)
        show_incomplete.append(request_name)

        if complete:
            show_season.append(show_list)

        else:
            show_season.append(show_incomplete)

    print(show_incomplete)

    return show_season  # IMPORTANTE: Esto devuelve una lista de listas.
    # Se vería así: [['The Boys S01', 'The Boys S02', 'The Boys S03', 'The Boys S04'],
    # ['Breaking Bad S01'], ['Stranger Things S03', 'Stranger Things S04'], ['Family Guy S16']]

    # Eso se tiene que hacer en bucle desde fuera.
    # Si se ejecuta este módulo una sola vez, solo obtiene la información de ese momento,
    # y, por tanto, no es conveniente dependiendo qué casos.

    # TODO: Crear función para extraer las peliculas también.


# Función para eliminar el requests de Ombi.
def ombi_delete(ombi_request_id: str, api_key: str, host: str, ssl: bool, port: int):
    """
    Elimina una petición dado su requestId. Si se utiliza la función anterior, esta se devuelve
    en el último índice de cada lista. Esto lo usamos para que, después de aceptar y
    poner a descargar la serie/pelicula, no se quede en el apartado de "espera".
    
    
    Params
    =======
    ombi_request_id: El requestId del cual se eliminará su petición dentro de OMBI, bien puede
    ser una pelicula o una serie.
    
    api_key: Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
    
    host: Dirección url donde está corriendo tu OMBI. Puede ser ingresado con el
    protocolo https o sin él. De cualquier manera especificar en el siguiente parametro.
    
    ssl: Proporciona información de sí tu servidor OMBI corre en un ambiente "seguro".
    
    port: Puerto donde está corriendo tu servidor OMBI.
    """

    # Si la url contiene un '/' al final, se lo sacamos para poder añadir el puerto.
    if host[-1] == '/':
        host = host[:-1]

    host = f'{host}:{port}'

    # ¡Sí la url no contiene ningún protocolo, se lo añadimos!
    if 'http://' in host or 'https://' in host:
        protocol: bool = True


    else:
        protocol: bool = False

        if not ssl:
            host = f'http://{host}'

        elif ssl:
            host = f'https://{host}'

    # ===========================================
    ombi_header = {'ApiKey': api_key}
    # Aquí hacemos la petición a la API.
    ombi_api_response = requests.delete(f'{host}/api/v1/Request/tv/{ombi_request_id}', params=ombi_header)
