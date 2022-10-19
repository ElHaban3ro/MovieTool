from qbittorrent import Client
import time
import os
import shutil


def torrent_handler(torrent_name: str, original_name: str, route_moviesdb: str, qbtorrent_host: str, qbtorrent_user='admin', qbtorrent_pass='adminadmin', handler_time = 10):
    """
    ¡Usa ese módulo para estar pendiente de sí tus torrents ya descargaron! Recomendamos ejectuar esto en un nuevo hilo.
    
    
    Params
    =======
    torrent_name: str | Nombre del torrent a visualizar.

    original_name: str | El nombre oficial de la serie/pelicula. Esto lo usamos para renombrar archivos, crear carpetas etc.

    route_moviesdb: str | Ruta definitiva para el contenido. Esta ruta es la que tomará plex para ver el contenido. Lo ideal sería que una vez  establecida no fuera cambiada, por tanto, ten en cuenta esto.

    qbtorrent_host: str | El host donde esta corriento tu qBittorrent WEB.

    qbtorrent_user: str | Usuario admin en tu qBitTorrrent!

    qbtorrent_pass: str | Contraseña del usuario admin de tu QBitTorrent.

    handler_time: float | Tiempo de espera sobre el cual se harán las peticiones al estado de la descarga, en segundos. Recomiendo no dejar un numero tan alto (como 60), ni tan bajo (como 3).
    """

    # Torrent Name!
    name = torrent_name

    # Login qBitTorrent
    qb = Client(qbtorrent_host)  # Nos conectamos al qBittorrent.
    qb.login(qbtorrent_user, qbtorrent_pass)  # Login.

    # Con el handler en sí, cada 10 s haremos una petición a qBitTorrent server para ver y manejar la descarga. De aquí solo sacaremos el hash de la descarga (por si la necesitamos), el estado actual y el path, que es donde se está descargando.

    # Esta sub función la usamos para obtener el estado del torrent. Esto lo sacamos en una función aparte, ya que, es lo que por separado, toca ejectutar constantemente para obtener SIEMRPE el estado del torrent.
    def get_state():
        my_hash = 'idk'
        state = 'idk'
        path = 'idk'
        name_torrent = 'idk'


        torrents_list = qb.torrents()

        # Vemos si el nombre proporcionado coincide con alguno de la lista actual del qBitTorrent.
        if len(torrents_list) == 0:
            print('No hay ningún torrent con ese nombre')
            exit()

        for download in torrents_list:

            # ¡Viendo un poco los torrents de diferentes descargas, algunas traen dobles espacios, ni puta idea de por qué, pero para solucionar eso básicmante eliminamos uno de esos espacios para que puedan coincidir perfectamente!
            if download['name'].replace('  ', ' ') != name:
                my_hash = download['hash']  # Extraemos el hash.
                state = download['state']  # Extraemos el estado actual.
                path = download['save_path']  # Extraemos la ruta de descarga.
                name_torrent = download['name']  # Extraemos el nombre del torrent.
                continue



            elif download['name'] != name:
                my_hash = download['hash']
                state = download['state']
                path = download['save_path']
                name_torrent = download['name']


            else:
                my_hash = download['hash']
                state = download['state']
                path = download['save_path']
                name_torrent = download['name']

            break

        return [state, path, my_hash, name_torrent]

    while True:
        handler_state = get_state()
        print(f'====================================\n Siguiendo: {handler_state[2]}\n{handler_state[0]}\n====================================\n\n\n')


        # Acá es donde empezamos a manejar los archivos. ¡Con esto, ya verificamos que descargó y simplemente tenemos que idear una buena forma de detectar si es una serie o es una pelicula! (probablemente OMBI ayude)
        if handler_state[0] == 'stalledUP' or handler_state[0] is None or handler_state[0] == 'uploading':  # Esto quiere decir que está seedeando, terminó de descargar o está "subiendo".

            # download_route = handler_state[1]  # ¡Ruta donde se descargó el torrent!
            folder_download = os.listdir(handler_state[1])  # Lista de archivos de donde se descargó el torrent.

            for filec, filef in enumerate(
                    folder_download):  # Saco todos los archivos".html", solo saco esto porque estoy seguro de que aquí no hay nada más. No va a haber ningún otro archivo. Estos dos, serán acompañados por la carpeta donde estarán los archivos de video, en el caso de que se haya encontrado algo para descargar.
                if '.html' in filef or '.txt' in filef or '.url' in filef:
                    folder_download.pop(filec)  # Sacamos eso de la lista. ¿Por qué? Luego lo usamos para mover los archivos, y no queremos que se muevan archivos basura.

            break

        # ¡Para estar pendiente de los torrents, pero que no esté ejecutandoce siempre, lo ponemos a esperar un tiempo, para que luego vuelva a ver el estado!
        time.sleep(handler_time)


    # Después de la descarga!
    print()



while True:
    torrent_handler('La Casa del Dragon - Temporada 1 [HDTV 720p][Cap.102][AC3 5.1 Castellano][www.atomoHD.wf]', 'La Casa Del Dragon', '/home/ferdev/db_movies/', 'http://mikoin.sytes.net:8080/', 'admin', 'adminadmin')