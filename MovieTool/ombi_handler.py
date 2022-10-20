import requests
from datetime import date

# ombi_login = requests.post('http://mikoin.sytes.net:5000/api/v1/Logging')


def ombi_requests(ombi_host: str, ombi_apikey: str):
    """
    Usa este módulo como handler de tu servidor ombi y resivir las peliculas o series que se piden. Por ahora solo soporta las series, pero se está trabajando para hacerlo compatible con peliculas de igual forma.


    Params
    =======
    ombi_host: str | Dirección url donde está corriendo tu OMBI.

    ombi_apikey: str | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.

    """
    

    ombi_header = {'ApiKey': ombi_apikey}  # Header que se envia al ombi y que es NECESARIO para que pueda ejecutar las consultas.

    # Aquí hacemos la petición a la API.

    if ombi_host[-1] == '/':
        ombi_tv = requests.get(f'{ombi_host}api/v1/Request/tv', params=ombi_header)  # Consulta que devuelve las series.
        ombi_movies = requests.get(f'{ombi_host}api/v1/Request/movie', params=ombi_header)  # Consulta que devuelve las peliculas sin aceptar.

    else:
        ombi_tv = requests.get(f'{ombi_host}/api/v1/Request/tv', params=ombi_header)  # Consulta que devuelve las series.
        ombi_movies = requests.get(f'{ombi_host}/api/v1/Request/movie', params=ombi_header)  # Consulta que devuelve las peliculas sin aceptar.

    
    
    if ombi_tv.status_code == 404:
        raise ValueError('(OmbiHostError, error 01) Es posible que la URL de donde está corriendo tu servidor de ombi sea incorrecta, asegurese de que esté en el puerto correcto!')

    elif ombi_tv.status_code == 401:
        raise ValueError('(OmbiApiKeyError, error 02) La API Key proporcionada es erronea. Asegurese de proporcionar la correcta. Si no está seguro de como obtenerla, vaya a su Ombi > Settings > Configuration > General > Api Key')


    #try:
    tv_requests = ombi_tv.json()  # Esto nos devolvería ya las series que se han pedido.
    #except json.decoder.JSONDecodeError:
    #    print('cero')

    # Claramente en formato JSON.
    movie_requests = ombi_movies.json()
    # print(movie_requests)

    # PARA LAS PETICIONES DE SERIES.
    # No son lo mismo que las peliculas, ya que en ocaciones, algunos
    # capitulos de la serie no se han publicado.

    # Lista de contenido en cola.
    cola = []

    capitulos_publicados = []
    show_incomplete = []

    complete: bool = True
    

    # Añadimos la serie a la cola!
    for show in tv_requests:
        show_status = show['childRequests'][0]['requestStatus'].split('.')[1]
        show_title = show['title'] # TODO: Converti nombre.
        show_id = show['id']
        


        show_seasons = show['totalSeasons']
        show_S_requests = show['childRequests'][0]['seasonRequests']
        show_request_ombi = show['childRequests'][0]['parentRequestId']

        show_tvId = show['externalProviderId']
        # print(show)
        
        get_serie_info = requests.get(f'https://api.themoviedb.org/3/tv/{show_tvId}?api_key=5eb7e21201ae0b13d5e4f992ee9d5471&language=es-ES')  # Se hace la petición con mi propia API Key, espero no conlleve un problema XDDDD.

        serie_info = get_serie_info.json()  # Esto nos devuelve un diccionario.
        show_title = serie_info['name']  # El titulo de la serie ya en español (en el caso de que esté).
        
        show_release = serie_info['first_air_date'].split('-')[0]

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

        charapters.append({'contentType': 'tv', 'showId': show_id, 'dbId': show_tvId, 'title': show_title, 'release': show_release})
        
        # Acá vamos a hacer una excepción con Dahmer – Monster: The Jeffrey Dahmer Story, ya que es conocida simplemente como Dahmer. Esto supongo que lo iré haciendo con diferentes series según convenga.
        charapters_except = []
        for c in charapters[:-1]:
            if isinstance(c, str) and 'Monstruo: La historia de Jeffrey Dahmer' in c:
                c = c.replace('Monstruo: La historia de Jeffrey Dahmer', 'Dahmer')
                charapters_except.append(c)

        


        if len(charapters_except) == 0:
            cola.append(charapters)
            
        else:
            charapters_except.append(charapters[-1])
            cola.append(charapters_except)


    movies = []


    for movie in movie_requests:
        consult_movie = requests.get(f'https://api.themoviedb.org/3/movie/{movie["theMovieDbId"]}?api_key=5eb7e21201ae0b13d5e4f992ee9d5471&language=es-ES').json()
        
        movie_title_es = consult_movie['title']
        movie_id = movie['id']
        movie_release = movie['releaseDate'].split('-')[0]
        

        # movie_append = [movie_title_es, movie['theMovieDbId'], ['movie', movie_id]]
        movies.append([movie_title_es, {'contentType': 'movie', 'showId': movie_id, 'dbId': movie['theMovieDbId'], 'title': movie_title_es, 'release': movie_release}])

        # Sacamos el titulo y el ID de TMDB. Esto mismo debo hacer con las series, no es complicado.
        # movies.append(movie_append)



    for movie in movies:
        cola.append(movie)

 
    return cola  # Esto devuelve una lista de listas con la serie! Un ejemplo sería el siguiente: [['La casa del Dragón S01E05', 234252, ['tv', 109]]]!! Para cada lista, los dos últimos indices pertenecen al ID del TheMovieDb y el ID del request del Ombi. Esto es útil para poder eliminar la requests desde API de OMBI.

    # Eso se tiene que hacer en bucle desde fuera.
    # Si se ejecuta este módulo una sola vez, solo obtiene la información de ese momento,
    # y, por tanto, no es conveniente dependiendo qué casos.

    # TODO: Crear función para extraer las peliculas también.

    


# Función para eliminar el requests de Ombi.
def ombi_delete(ombi_request_id: str, ombi_host: str, ombi_apikey: str, content_type:str):
    """
    Elimina una petición dado su requestId. Si se utiliza la función anterior, esta se devuelve
    en el último índice de cada lista. Esto lo usamos para que, después de aceptar y
    poner a descargar la serie/pelicula, no se quede en el apartado de "espera".
    
    
    Params
    =======
    Usa este módulo como handler de tu servidor ombi y resivir las peliculas o series que se piden. Por ahora solo soporta las series, pero se está trabajando para hacerlo compatible con peliculas de igual forma.


    Params
    =======
    ombi_request_id: (str) | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.

    ombi_host: str | Dirección url donde está corriendo tu OMBI.

    ombi_apikey: str | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.

    content_type: str | El tipo de contenido del que se va a borrar. Recibe solo dos posibles parametros: "movie" o "tv".

    """
    
    # ===========================================
    headers = {'content-type': 'application/json'}
    ombi_header = {'ApiKey': ombi_apikey}
    
    


    if ombi_host[-1] == '/':
        ombi_host = ombi_host[:-1]
    else:
        pass
    

    # Aquí hacemos la petición a la API.
    if content_type == 'tv':
        consult = requests.delete(f'{ombi_host}/api/v1/Request/tv/{ombi_request_id}',params=ombi_header)

        if consult.status_code == 200:
            return 'Eliminación completa'

        else:
            return 'Algo ha sucedido, puede que no este pasando el request id correcto.'

    else:
        consult = requests.delete(f'{ombi_host}/api/v1/Request/movie/{ombi_request_id}',  params = ombi_header, headers = headers, data = ombi_header)  # TODO: ARREGLAR DE QUE SE ELIMINEN LA PELICULAS SOLICITADAS. Funciona con las series pero no con las peliculas por alguna razón.No tiene sentido. Puede ser por el desactualizado server, pero debemos esperar.


        print(consult.headers)
       
        if consult.status_code == 200:
            return 'Eliminación completa'

        else:
            return 'Algo ha sucedido, puede que no este pasando el request id correcto.'