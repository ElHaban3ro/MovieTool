from MovieTool.download_torrents import download
from MovieTool.torrent_handler import torrent_handler



# Script De Testeo!!!!! Es necesario tener instalado MovieTool.
search = input('Has tu busqueda ------------>   ')

# Parametros
# Jackett
jackett_host = 'http://mikoin.sytes.net:9117/'
jackett_apikey = 'z96avavpt0rmbakcr7h2c85ir8ukw3dq'

# qBittorrent
qbtorrent_host = 'http://mikoin.sytes.net:8080/'
qb_user = 'admin'
qb_pass = 'adminadmin'
qbtorrent_download_route = '/home/ferdev/raw_movies/'
max_size = 2000



d_torrent = download(search, jackett_host, jackett_apikey, qbtorrent_host, qb_user, qb_pass, qbtorrent_download_route, max_size, low_discard = False)


# Bucle infinito:
while True:
    torrent_handler(d_torrent, 'La Casa Del Dragon', '/home/ferdev/db_movies/', 'http://mikoin.sytes.net:8080/', qb_user, qb_pass)