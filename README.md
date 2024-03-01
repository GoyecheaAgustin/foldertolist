


### Spotify Playlist Maker
Este proyecto es una aplicación de línea de comandos que permite crear una lista de reproducción en Spotify a partir de archivos de música almacenados localmente en tu computadora.

### Requisitos
Python 3.6 o superior
Instalar las dependencias usando pip install

### Configuración
Antes de usar la aplicación, necesitas configurar las credenciales de la API de Spotify. Sigue estos pasos:

Crea una aplicación en el Tablero de Desarrolladores de Spotify.
Obtiene el ID de cliente y el secreto de cliente de la aplicación.
Configura la redirección URI en la configuración de la aplicación.
Proporciona tu ID de cliente, secreto de cliente y URI de redirección.

### Uso
Coloca tus archivos de música en una carpeta en tu sistema.
Ejecuta el script spotifyList.py
Sigue las instrucciones para autenticarte con Spotify y seleccionar la carpeta de música.
La aplicación buscará las canciones en Spotify y creará una lista de reproducción con ellas.
### Dependencias
Este proyecto utiliza la biblioteca Spotipy para interactuar con la API de Spotify. La biblioteca Spotipy facilita la autenticación, búsqueda y manipulación de listas de reproducción en Spotify. Puedes encontrar más información sobre Spotipy en su página de documentación.

Para instalar Spotipy, puedes ejecutar:

pip install spotipy

### Consideraciones
Asegúrate de tener una conexión a Internet estable durante la ejecución del programa.
Si encuentras problemas de autenticación, verifica la configuración de la aplicación en el Tablero de Desarrolladores de Spotify.
La aplicación agrega canciones a la lista de reproducción según la fecha de modificación de los archivos de música. Sin embargo, el orden de las canciones en la lista de reproducción es una preferencia personal y puede ajustarse según tus preferencias.
