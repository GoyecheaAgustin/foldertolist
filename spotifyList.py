import os
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

# Configura las credenciales de la API de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='xxxxxxxxx',
                                               client_secret='xxxxxxxxxx',
                                               redirect_uri='xxxxxxxxxx',
                                               scope='playlist-modify-private', requests_timeout=20))
# Ruta a la carpeta que contiene las canciones
folder_path = 'C:\\Users\\Agustin Goyechea\\Desktop\\Musica\\GOYE'

# Obtén los nombres de los archivos en la carpeta con sus fechas de modificación
files_with_dates = [(filename, os.path.getmtime(os.path.join(folder_path, filename))) for filename in os.listdir(folder_path) if filename.endswith('.mp3')]

# Ordena los archivos en función de la fecha de modificación
files_with_dates.sort(key=lambda x: x[1])

# Extrae los nombres de los archivos ordenados
song_names_ordered = [filename for filename, _ in files_with_dates]

# Crea una nueva lista de reproducción
playlist = sp.user_playlist_create('xxxxxxxxx', 'My Python Playlist', public=False)

# Lista para almacenar los nombres de las canciones agregadas
added_songs = []

# Agrega canciones a la lista de reproducción en orden
for song_name in song_names_ordered:

    time.sleep(3)
    # Extrae el nombre del archivo sin la extensión
    song_name_without_extension = os.path.splitext(song_name)[0]

    # Busca la canción en Spotify
    search_query = f"{song_name_without_extension} NOT remix NOT cover"
    track_results = sp.search(q=search_query, type='track', limit=1)

    if track_results['tracks']['items']:
        track_uri = track_results['tracks']['items'][0]['uri']
        sp.playlist_add_items(playlist['id'], [track_uri])
        added_songs.append(song_name_without_extension)  # Agrega el nombre de la canción a la lista
        print(f"Canción encontrada y agregada: {song_name_without_extension}")
    else:
        print(f"No se encontró una canción con el nombre '{song_name_without_extension}' en Spotify.")

# Guarda los nombres de las canciones agregadas en un archivo de texto
with open('canciones_agregadas.txt', 'w', encoding='utf-8') as file:
    for song in added_songs:
        file.write(song + '\n')

print("Canciones agregadas correctamente a la lista de reproducción.")
print("Se ha creado el archivo 'canciones_agregadas.txt' con los nombres de las canciones agregadas.")
