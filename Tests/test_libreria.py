from MoviePy.download_torrents import get_torrent
from MoviePy.torrent_handler import T_HANDLER

from MoviePy.ombi_request import ob_requests, delete_ombi


import time
import threading










# ==================== PARAMETERS ZONE ====================

# Zona de parametros importantes que utilizaremos constantemente, por tanto, se me hace más como instanciarlos antes! Los nombres son bastante representativos, por tanto no voy a explicar todos.


# TORRENT DOWNLOAD. CUIDADO CON ESTO!!!!! 
movie_db = '/home/ferdev/MOVIES_DB'



# QBITTORENT!!!!
qb_user = 'admin'
qb_password = 'adminadmin'
qb_host = 'http://mikoin.sytes.net:8080/'


qb_cat_list = [] # Lista de categorías sobre las que se busca en el rargb.
qb_save_route = '/home/ferdev/Proyecto-Fantasma/Res'
qb_download_quality = 1080
qb_download_max_size = 100 # En GB's







# OMBI!!!!
ombi_key = '5e7a7c736ea84fd3bfd69fb12890d62a'
ombi_host = 'http://mikoin.sytes.net/'
ombi_port = 5000
ssl_ombi = False



# =========================================================

already_download = [] # Lista donde entrarán todas las series descargadas!













while True: # Bucle que mantendrá SIEMPRE ejecutando el programa.
    
    ap_torrents = ob_requests(api_key = ombi_key, host = ombi_host, ssl = ssl_ombi, port = ombi_port) # Esto  devuelve la lista de listas en las que están los nombres de las series con sus temporadas. Todo esto proviene de ombi!
    
    
    # Validamos si la lista devuelta de "ap_torrents" no está vacía.
    if len(ap_torrents) >= 1:
        
        
        # Finalmente recorremos por cada una de ellas para poner a descargar cada capítulo con ayuda del modulo "get_torrent", hecho anteriormente. Mirar la documentación para llenar los campos.
        for e, apm_name in enumerate(ap_torrents):
            for ap_name in apm_name[:-2]:
                
                
                torrent = get_torrent(search = ap_name, categories = qb_cat_list, route = qb_save_route, filter_quality = qb_download_quality, filter_size = qb_download_max_size, qbittorrent_user = qb_user, qbittorrent_password = qb_password, qbittorrent_server_ip = qb_host)

                try:
                    torrent_name = torrent[0]
                    movie_search = torrent[1]
                    print(ap_torrents)

                    
                    manage_download = threading.Thread(target = lambda: T_HANDLER(torrent_name, movie_search, movies_db_route = movie_db, serie_name = apm_name[-1], qb_ip = qb_host)).start()

                except:
                    pass
                
            
            delete_ombi(ombi_request_id = apm_name[-2], api_key = ombi_key, host = ombi_host, ssl = ssl_ombi, port = ombi_port)
            
            already_download.append(apm_name)


            


            
    
    
    time.sleep(15)