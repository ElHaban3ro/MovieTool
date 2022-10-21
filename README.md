# MOVIEPY

# DeeptransTool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_MovieTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/MovieTool/) [![GitGub Repositorie](https://img.shields.io/badge/GitHub_Repositorie-MovieTool-gray.svg?style=flat-square&logo=github)](https://github.com/ElHaban3ro/MovieTool/)

* ⚠ Este proyecto es uno personal, sin animo de lucro y tampoco animo a nadie a usarlo. La persona que utilice esta herramienta será bajo su propio riesgo. Aclarar antes de que continues leyendo que acá no se proporciona NINGÚN contenido, todo es descargado usando redes torrents, por tanto, es cuestión del usuario en sí (usted) de si accede a ese contenido.

*Proyecto actualmente en desarrollo, puede que cuando esté leyendo el proyecto no esté completamente hecho o incluso tenga bugs IMPORTANTES.*


- Developed in Python 3.10.

## Detalles del proyecto

---
Proyecto **personal** para automatizar la descarga de contenido multimedia (películas y series) por medio de redes **TORRENTS**. Para lograr el objetivo hacemos uso de **Plex**, **Ombi** y otros cuantos servicios más (luego enumerados). La idea principal del proyecto es que se pueda crear una biblioteca con tus películas y series favoritas, esto, como proyecto personal para mi portafolio. Podrá crear un proyecto **100%** montando y casi listo para correr haciendo uso de nuestro script de construcción (disponible en el futuro). Esta herramienta en conjunto con plex y otras más, crearía algo MUY parecido a **Netflix**, pero asegurate de que si lo haces, sea con fines didácticos. Recomiendo que al montar el servidor se disponga de MUY BUEN **ALMACENAMIENTO**, pues, aunque existe la posibilidad de ver y eliminar, la idea es que descargues las películas/series y puedas reproducirlas en un **futuro**.

Podrás usar los diferentes **modulos** de maneras independientes (más adelante la ***documentación***) o si lo prefieres, ***montar*** tu propio servidor *casi listo para utilizar* usando nuestros **scripts** (aún no ***disponibles***, no puedes montar tu servidor aún).

El **enfoque** inicial del proyecto cambió. Ahora nuestro *principal objetivo* es descargar el contenido en ***español***, olvidandonos de los mayores **problemas** causados por los subtitlos de las **peliculas**/**series** en ***inglés***.




## Instalación (del paquete)

---
La mejor idea para obtener acceso a este paquete, es haciendo uso de ***pip***:
```bash
pip install MovieTool
```
Ya con el comando ejecutado, podrás comenzar a usar nuestro paquete.

---

Si por alguna razón tienes algún problema con esto, puedes **instalar** el proyecto ***clonando el repositorio*** dentro de la carpeta de un proyecto ya creado:
```bash
git clone https://github.com/ElHaban3ro/MovieTool.git
```

Esto te copiará el proyecto dentro de una **nueva** carpeta.
Lo siguiente en hacer es muy importante, necesitas instalar los requisitos previos (el **requeriments.txt** incluye las librerías importantes que necesitamos para que el proyecto funcione). Ésto lo hacemos con el comando:
```bash
pip install -r requirements.txt 
```

Esto, **idealmente** tendría que instalarte todas las librerias necesarias.


Una vez con esto hecho, tu proyecto personalizado se vería así:
```
tu_proyecto |
               .venv
               MovieTool (librería)  |
                                      download_torrents.py
                                     
               main.py (tu script principal)
```




## Uso

---

*Ten en cuenta que, todos estos módulos fueron construidos con la idea de ser utilizados juntos, ayudándose entre ellos y haciendo que el trabajo sea perfecto, por tanto, no recomendamos tocar scripts y simplemente montar tu proyecto desde [aquí (aún no disponible)](https://isaitech.site)*

Hacer uso de nuestros modulos es realmente **facil**. Para utilizar un módulo, se haría de la siguiente forma:

```python
from MovieTool.download_torrents import download

d = download('Dahmer S01E05', 'http://jacketthost:9197', 'jackettAPIKey', 'http://qbtorrenthost:8080', 'admin', 'adminadmin', 'C:/users/yo/raw_movies/', 2000, False)
```


## Módulos (DOCS)

----
- ### ***download_torrents***:
    - > download_torrents.download(search: str, jacket_host: str, jacket_apiKey: str, qbtorrent_host: str, qbtorrent_user: str, qbtorrent_pass: str, download_path: str, max_size: int, low_discard: bool)
    
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

        - low_discard: **(bool)** | Si desea que se descarte el contenido en 720p, active esto!

    
    - **Return**:
        - Nombre del torrent descargado (puede que en el futuro cambiemos lo que devuele)



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
                > [['La casa del Dragón S01E05', {'contentType': 'movie', 'showId': 234252, 'dbId': 777, 'title': 'La Casa Del Dragón'}]
                ```

             Para cada lista, los dos últimos indices pertenecen al ID del TheMovieDb y el ID del request del Ombi. Esto es útil para poder eliminar la requests desde API de OMBI.

    - > ombi_handler.ombi_delete(ombi_request_id:str, ombi_host: str, ombi_apikey: str, content_type: str)
        - **Descripción:**
          - Elimina una petición dado su requestId. Si se utiliza la función anterior, esta se devuelve en el último índice de cada lista. Esto lo usamos para que, después de aceptar y poner a descargar la serie/pelicula, no se quede en el apartado de "espera".

        - **params**:
          - ombi_request_id: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
        
          - ombi_host: **(str)** | Dirección url donde está corriendo tu OMBI. Puede ser ingresado con el protocolo https o sin él. De cualquier manera especificar en el siguiente parametro.

          - ombi_apikey: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.

          - content_type: **(str)** | Tipo de contenido a eliminar. Este parametro solo puede recibir 2 valores: "**movies**" o "**tv**", siendo tv correspondiente a las series.
    
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
            - La lista de los archivos que se consideraron multimedia y que se pasaron a la nueva carpeta de esa serie/pelicula.
              - **Example**:
                - ```console
                  > ['S01E01', 'S01E04'. 'S05E666']
                  ```



                  

## Aplicaciones Independientes necesarias para usar el proyecto en su totalidad

----

- Python - Lenguaje base del proyecto.
- qBittorrent - Cliente de BitTorrents.
- Jackett - API Para trackers.
- Ombi - Para hacer peticiones de peliculas.
- Plex - Servicio para la visualización del contenido.


# Autor Contact
---

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro) [![Contact Discord](https://img.shields.io/badge/Discord-!%20Die()%231274-lightgray?style=for-the-badge&logo=discord)](https://discord.com) [![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)