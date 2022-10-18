# MOVIEPY

# DeeptransTool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_MovieTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/MovieTool/) [![GitGub Repositorie](https://img.shields.io/badge/GitHub_Repositorie-MovieTool-gray.svg?style=flat-square&logo=github)](https://github.com/ElHaban3ro/MovieTool/)

* ⚠ Este proyecto es uno personal, sin animo de lucro y tampoco animo a nadie a usarlo. La persona que utilice esta herramienta será bajo su propio riesgo y considero que no me hago cargo del uso que se haga de la misma. ⚠ 

*Este es mi proyecto más grande hasta el momento, por tanto, si ven errores o cualquier cosa que creen se puede mejorar, me pueden comentar por mis redes.*



## Detalles del proyecto

---
Descarga tus ***peliculas*** o ***series*** favoritas, **automatizando** la descarga de peliculas y series ***en español*** y 100% gratis (OJO, YO NO ALMACENO NADA, EL USAR TECNOLOGÍAS TORRENT ES BAJO SU RESPONSABILIDAD). Usamos **OMBI**, **Plex**, **QBitTorrent** y *otros* servicios más para *cumplir la meta*. Una alternativa *facil de implementar* (ya trabajaré en la implementación casi 100% automatica) y barata por donde lo veas. ¡Te recomendamos que tengas a tu disposición ***MUY BUEN ALMACENAMIENTO***, pues, todo lo que se pida, **se descargará**, por tanto, puedes ir mirando y eliminando, o *dejarlo de por vida* para que otras personas las ***utilicen!***

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
Lo siguiente en hacer es muy importante, necesitas instalar los requerimientos (el **requeriments.txt** incluye las librerias importantes que necesitamos para que el proyecto funcione). Ésto lo hacemos con el comando:
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

Hacer uso de nuestros modulos es realmente **facil**. Para utilizar un módulo, se haría de la siguiente forma:

```python
from MovieTool.ombi_handler import ombi_requests

ombi_requests('MiOmbiApiKey', 'https://mihostombi', True, 7777)
```


## Módulos (DOCS)

----
- ### ***download_torrents***:
    - > download_torrents.download(search: str, jacket_host: str, jacket_apiKey: str, qbtorrent_host: str, qbtorrent_user: str, qbtorrent_pass: str, max_size: int, low_discard: bool)
    
    - **Descripción:**
        - Usa este modulo para descargar el contenido multimedia es español. Como los parametros pueden indicar, hace falta tener corriendo en tu computadora el server de Jackett (muy facil de instalar) y un server de qBitTorrent (aún más facil de hacer).

    - **params**:
        - search: **(str)** | Nombre de la serie o película a buscar!
        
        - jackett_host: (str) | El host dond está corriendo tu servidor de Jackett.
            
        - jackett_apiKey: **(str)** | La API KEY de tu Jackett! La puedes encontrar
            arriba derecha de tú Jackett.

        - qbtorrent_host: **(str)** | El host donde esta corriento tu qBitTorrent WEB.

        - qbtorrent_user: **(str)** | Usuario admin en tu qBitTorrrent!

        - qbtorrent_pass: **(str)** | Contraseña de tu usuario en tu qBitTorrent!

        - max_size: **(int)** | Peso máximo **(en MB) que podrán tener los archivos.

        - low_discard: **(bool)** | Si desea que se descarte el contenido en 720p, active esto!
    
    - **Return**:
        - Nombre del torrent descargado (puede que en el futuro cambiemos lo que devuele)



- ### ***ombi_handler***:
    - > ombi_handler.ombi_requests(api_key: str, host: str, ssl: bool, port: int)
        - **Descripción:**
          - Usa este módulo como handler de tu servidor ombi y resivir las peliculas o series que se piden. Por ahora solo soporta las series, pero se está trabajando para hacerlo compatible con peliculas de igual forma. Recomiendo ejecutar esto en un nuevo hilo Python, además de estar en un bucle infinito con un ```time.sleep(15)```

        - **params**:
          - api_key: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
    
          - host: **(str)** | Dirección url donde está corriendo tu OMBI. Puede ser ingresado con el protocolo https o sin él. De cualquier manera especificar en el siguiente parametro.
    
          - ssl: **(bool)** |  Proporciona información de sí tu servidor OMBI corre en un ambiente "seguro".

          - port: **(int)** | Puerto donde está corriendo tu servidor OMBI.

        - **Return**:
          - Una lista de listas, con las series que se han pedido.
            - **example**:
              - ```console
                > [['Stranger Things S01', 'Stranger Things S02'], ['House Of The Dragon S01E01', ''House Of The Dragon S01E02'']]
                ```

    - > ombi_handler.ombi_delete(ombi_request_id:str, api_key: str, host: str, ssl: bool, port: int)
        - **Descripción:**
          - Elimina una petición dado su requestId. Si se utiliza la función anterior, esta se devuelve en el último índice de cada lista. Esto lo usamos para que, después de aceptar y poner a descargar la serie/pelicula, no se quede en el apartado de "espera".

        - **params**:
          - ombi_request_id: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
        
          - api_key: **(str)** | Clave de la api de OMBI. Importante para efectuar correctamente las consultas.
    
          - host: **(str)** | Dirección url donde está corriendo tu OMBI. Puede ser ingresado con el protocolo https o sin él. De cualquier manera especificar en el siguiente parametro.
    
          - ssl: **(bool)** |  Proporciona información de sí tu servidor OMBI corre en un ambiente "seguro".

          - port: **(int)** | Puerto donde está corriendo tu servidor OMBI.

        - **Return**:
          - None.


- ### ***torrent_handler***:

    - > ombi_handler.t_handler(torrent_name_to_handler: str, search: str, movies_db_route: str, serie_name: str, qb_user: str,
              qb_pass: str, qb_ip: str, handler_time: int)
        - **Descripción:**
          - ¡Usa ese módulo para estar pendiente de sí tus torrents ya descargaron! Recomendamos ejectuar esto en un nuevo hilo. De igual forma, si utilizas este módulo te recomendamos utilizar el limitador de seeding propio del qBitTorrent.

        - **params**:
          - torrent_name_to_handler: Torrent name to handler!
    
          - search: La búsqueda que utilizaste para el torrent! Esto lo empleamos para renombrar las peliculas. Si no quieres añadir un nombre, proporciona aquí el mismo que en el parametro anterior (torrent_name_to_handler)
    
          - movies_db_route: Ruta definitiva (donde moveremos las pelis para generar nuestro catálogo) donde se estructurarán las series/peliculas por nombre oficial, después de terminar de descargar y mover los archivos, se espera que no se muevan de nuevo, una ruta definitiva!
    
          - serie_name: Nombre de la serie! ¡Utilizada para crear una carpeta con el nombre! Si se emplea OMBI con nuestro módulo, puedes optar por acceder al nombre de la serie con su Return.
    
          - qb_user: Usuario admin de tú QBitTorrent.
    
          - qb_pass: Contraseña del usuario admin de tu QBitTorrent.
    
          - qb_ip: Ruta donde está corriendo tu Web UI del QBitTorrent.

          - handler_time: Tiempo de espera (en segundos) con el cual se hace las peticiones a la API de qBitTorrent y ver si se ha descargado dicha serie.

          - **Return**:
            - La lista de los archivos que se consideraron multimedia y que se pasaron a la nueva carpeta de esa serie/pelicula.
              - **Example**:
                - ```console
                  > ['S01E01', 'S01E04'. 'S05E666']
                  ```



[//]: # (A)
# Autor Contact
---

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro) [![Contact Discord](https://img.shields.io/badge/Discord-!%20Die()%231274-lightgray?style=for-the-badge&logo=discord)](https://discord.com) [![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)