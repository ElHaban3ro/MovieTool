MovieTool (v3.5)
---


Módulos

---
- ### ***download_torrents***:
    - > download_torrents.download(search: str, jacket_host: str, jacket_apiKey: str, qbtorrent_host: str, qbtorrent_user: str, qbtorrent_pass: str, download_path: str, max_size: int, delete_torrents_die: bool)
    
    - **Descripción:**
        - Usa este modulo para descargar el contenido multimedia en español. Como los parametros pueden indicar, hace falta tener corriendo en tu computadora el server de Jackett (muy facil de instalar) y un server de qBittorrent (aún más facil de hacer).

    - **params**:
        - search: **(str)** | Nombre de la serie o película a buscar!
        
        - jackett_host: **(str)** | El host dond está corriendo tu servidor de Jackett.
            
        - jackett_apiKey: **(str)** | La API KEY de tu Jackett! La puedes encontrar
            arriba derecha de tú Jackett.

        - qbtorrent_host: **(str)** | El host donde esta corriento tu qBittorrent WEB.

        - qbtorrent_user: **(str)** | Usuario admin en tu qBitTorrrent!

        - qbtorrent_pass: **(str)** | Contraseña de tu usuario en tu qBittorrent!

        - download_path: **(str)** | Ruta donde se descargarán los archivos virgenes, sin haberlos procesado y renombrado, por tanto, no des la ruta defenitiva.  ***RUTA ABSOLUTA!!!!***

        - max_size: **(int)** | Peso máximo **(en MB) que podrán tener los archivos.

        - delete_torrents_die: **(bool)** | Elimina la descarga de torrents muertos (con 0 seeders. Si esto se establece como False, el torrent quedará dentro del qBittorrent, esperando...)


    - **Return**:
        - Nombre del torrent descargado o 0 si no encontró contenido valido.



- ### ***ombi_handler***:
    - > ombi_handler.ombi_requests(ombi_host: str, ombi_apikey)
        - **Descripción:**
          - Usa este módulo como handler de tu servidor ombi y recibir las peliculas o series que se piden. Por ahora solo soporta las series, pero se está trabajando para hacerlo compatible con peliculas de igual forma. Recomiendo ejecutar esto en un nuevo hilo Python, además de estar en un bucle infinito con un ```time.sleep(15)```

        - **params**:
          - ombi_host: **(str)** | Dirección url donde está corriendo tu OMBI. Puede ser ingresado con el protocolo https o sin él. De cualquier manera especificar en el siguiente parametro.

          - ombi_apikey: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
    

        - **Return**:
          - Esto devuelve una lista de listas con la serie! Un ejemplo sería el siguiente:

            - **example**:
              - ```console
                > [['La casa del Dragón S01E05', {'contentType': 'movie', 'showId': 234252, 'dbId': 777, 'title': 'Sos mi peli favorita', 'release': '1987'}]
                ```

             Para cada lista, los dos últimos indices pertenecen al ID del TheMovieDb y el ID del request del Ombi. Esto es útil para poder eliminar la requests desde API de OMBI.

    - > ombi_handler.ombi_delete(ombi_request_id:str, ombi_host: str, ombi_apikey: str, content_type: str)
        - **Descripción:**
          - Elimina una petición dado su requestId. Si se utiliza la función anterior, esta se devuelve en el último índice de cada lista. Esto lo usamos para que, después de aceptar y poner a descargar la serie/pelicula, no se quede en el apartado de "espera".

        - **params**:
          - ombi_request_id: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
        
          - ombi_host: **(str)** | Dirección url donde está corriendo tu OMBI. Puede ser ingresado con el protocolo https o sin él. De cualquier manera especificar en el siguiente parametro.

          - ombi_apikey: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.

          - content_type: **(str)** | Tipo de contenido a eliminar. Este parametro solo puede recibir 2 valores: "**movie**" o "**tv**", siendo tv correspondiente a las series.
    
        - **Return**:
          - Info string.


- ### ***torrent_handler***:

    - > torrent_handler.torrent_handler(torrent_name: str, original_name: str, route_moviesdb: str, torrent_type: str, qbtorrent_host: str, qbtorrent_user: str, qbtorrent_pass: str, handler_time: float)
        - **Descripción:**
          - ¡Usa ese módulo para estar pendiente de sí tus torrents ya se descargaron! Recomendamos ejectuar esto en un nuevo hilo. De igual forma, si utilizas este módulo te recomendamos utilizar el limitador de seeding propio del qBittorrent.

        - **params**:
            - torrent_name: **(str)** | Nombre del torrent a visualizar.

            - original_name: **(str)** | El nombre oficial de la serie/pelicula. Esto lo usamos para renombrar archivos, crear carpetas etc.

            - route_moviesdb: **(str)** | Ruta definitiva para el contenido. Esta ruta es la que tomará plex para ver el contenido. Lo ideal sería que una vez  establecida no fuera cambiada, por tanto, ten en cuenta esto. 

            - torrent_type: **(str)** | El tipo de contenido que está intentando rastrear. Ese parametro soporta SOLO dos valores: 'tv' o 'movie'

            - qbtorrent_host: **(str)** | El host donde esta corriento tu qBittorrent WEB.

            - qbtorrent_user: **(str)** | Usuario admin en tu qBitTorrrent!

            - qbtorrent_pass: **(str)** | Contraseña del usuario admin de tu QBitTorrent.

            - handler_time: **(float)** | Tiempo de espera sobre el cual se harán las peticiones al estado de la descarga, en segundos. Recomiendo no dejar un numero tan alto (como 60), ni tan bajo (como 3).

            - season: **(str)** | Si el parametro de "torrent_type" es "tv", es necesario especificar la temporada con el formato SXX, donde "X" es el número de temporada. Ej: S01.

            - episode: **(str)** | Si el parametro de "torrent_type" es "tv", es necesario especificar el episodio con el formato EXX, donde "X" es el número de episodio. Ej: E02.


          - **Return**:
            - None



                  