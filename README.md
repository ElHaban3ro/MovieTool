# MOVIEPY

[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_MovieTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/MovieTool/) [![GitGub Repositorie](https://img.shields.io/badge/GitHub_Repositorie-MovieTool-gray.svg?style=flat-square&logo=github)](https://github.com/ElHaban3ro/MovieTool/)

* ⚠ Este proyecto es uno personal, sin animo de lucro y tampoco animo a nadie a usarlo. La persona que utilice esta herramienta será bajo su propio riesgo. Aclarar antes de que continues leyendo que acá no se proporciona NINGÚN contenido, todo es descargado usando redes torrents, por tanto, es cuestión del usuario en sí (usted) de si accede a ese contenido.

*Ten en cuenta que estás en github, y que por tanto, casi todo lo que se dice acá se dice teniendo en mente que sabes algo de python o parecido. Si no es desarrollador puede ir a la zona de descargas, descargar y leer la documentación para el usuario.*


## Detalles del proyecto

---
*Hola usuario de internet! Si quieres tener tu proyecto de MovieTool montado, ten en cuenta que no es necesario programar, puedes descargar el ejecutable de todo el [proyecto aquí](https://github.com/ElHaban3ro/MTRA)! Si eres programador, puedes ver la documentación [oficial aquí](https://movietool.readthedocs.io/es/latest/)*.

---

Hola! Me emociona contarles y mostrarles este gran proyecto personal. **MovieTool** es una app que hace uso de Python para automatizar la descarga de **contenido multimedia**, haciendo uso de Torrents, esto quiere decir que no existe contenido almacenado por nosotros. Hacemos uso de múltiples aplicaciones y APIs ya existentes para lograr este objetivo.Podrás crear tu propia biblioteca de contenido y disfrutarlo desde donde quieras usando Plex (lo ideal) o alguna otra solución. Podrás descargar contenido de todo tipo, limitado por la cantidad de seeders (cantidad de personas que ya tienen el contenido multimedia y lo comparten) que haya en ese instante, siendo que, si hay pocos seeders para esa serie/película, tu contenido tardará en descargar o directamente no descarga. La idea de este proyecto fue que **descargar** y **almacenar** contenido fuera realmente sencillo, fácil y seguro, y si tenemos en cuenta lo anterior dicho, crear una biblioteca de contenido multimedia puede llegar a ser **muy pesado**, pues, se necesitan muchas GBs para almacenar mucho contenido, así que asegurate de tener espacio libre :) Una solución que puedes aplicar es descargar contenido y posteriormente eliminarlo para **liberar espacio**. 

Cuando pongas a correr nuestro programa, recomendamos que lo haga desde una **compu secundaria** donde idealmente no se use para nada más (aunque descargar torrents no conlleva mucho estrés a la cpu, puede traer error aún no previstos. Nos faltan pruebas)








## Apps que NO son de nuestra autoría y que se usan

----
Hacemos uso de algunas apps para cumplir nuestro objetivo, y que se proporcionan independientemente de tu **sistema operativ**o en el **montable** del proyecto (más abajo)

- Python - Lenguaje base del proyecto.
- qBittorrent - Cliente de BitTorrents.
- Jackett - API Para trackers (la piedra angular aquí).
- Ombi - Para hacer peticiones de peliculas.
- Plex - Servicio para la visualización del contenido.

*Si no eres programador, es probable que lo siguiente parezca casi criptográfico, así que te recomiendo ir directamente a la zona de descarga!*

## Descargas
*Esta zona va dedicada a todos los usuarios que quieren montarse su propio servidor de contenido multimedia de manera sencilla.*

-  Para empezar es necesario que descargue **MovieTool Runner Apps**, la cual instala en su sistema operativo (Windows o Linux) las aplicaciones necesarias para poder crear el servidor. *(La configuración para la configuración de cada uno de los programas que se descargan está junto al ejecutable!)* [![Download MovieToolRunnerApps](https://img.shields.io/badge/Download-MovieTool_Runner_Apps-red.svg?style=flat-square)](https://github.com/ElHaban3ro/MTRA)


- Comming Soon.




## Instalación (para desarrolladores)

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




## Uso (si eres programador)

---

*Esta descripción de uso es poco detallada, si quiere más información vaya a la [documentación](https://movietool.readthedocs.io/es/latest/) ofical*

Hacer uso de nuestros modulos es realmente **facil**. Para utilizar un módulo, se haría de la siguiente forma:

```python
from MovieTool.download_torrents import download

d = download('Dahmer S01E05', 'http://jacketthost:9197', 'jackettAPIKey', 'http://qbtorrenthost:8080', 'admin', 'adminadmin', 'C:/users/yo/raw_movies/', 2000, False)
```




# Autor Contact
---

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro) [![Contact Discord](https://img.shields.io/badge/Discord-!%20Die()%231274-lightgray?style=for-the-badge&logo=discord)](https://discord.com) [![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)