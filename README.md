# Chain Reaction Music — instaladores y actualizaciones

Repositorio público de distribución. No contiene el código privado del proyecto ni credenciales.

## Android TV

[Descargar versión r19](tv/ChainReactionMusic-TV-0.1.0-demo1-r19-v35.apk)

Instalar sobre la versión anterior, sin desinstalar, para conservar favoritos y ajustes. Android puede pedir autorizar instalaciones desde esta aplicación. En r16: Ajustes → Actualizaciones permite comprobar nuevas versiones; la comprobación al abrir se limita a una vez por día y se puede desactivar. La descarga requiere elegir Actualizar ahora y la instalación requiere confirmación de Android.

El archivo `tv/latest.json` anuncia la versión disponible con tamaño, SHA256 y enlace HTTPS. La aplicación verifica también identidad, versión y firma del APK. No contiene publicidad ni claves de acceso al repositorio privado.

TV versionCode35, Android8 o posterior. Versión de prueba; validar funcionamiento en cada televisor. Las futuras versiones deben conservar el nombre de paquete y la misma clave de firma. Publicar primero el APK y actualizar el manifiesto al final.

## Cambios de r19

Letras sincronizadas con desplazamiento automático y salida al finalizar la cola. Mando: corazón y opciones accesibles, foco conservado por fila. Inicio con brillo suave, Historial y sugerencias según escuchas y Me gusta. Cranberries corregido. Explorar, discos y playlists continúan con los temas siguientes de la lista cargada. Letras argentinas de CMTV como respaldo sin tiempos.

134 pruebas por variante, lint sin errores y recorrido nativo de letras, cola y mando. Televisor físico pendiente. Recomendador sencillo local, con catálogo público; no es el algoritmo de Google. CMTV se consulta con límites de tiempo y páginas; no garantiza cobertura completa.

## Cambios de r18

Portadas sin marcos permanentes en Inicio, listas, radios y reproductor. Se conserva el resaltado al seleccionar con el mando. Historial local de las últimas 100 reproducciones, disponible en Biblioteca, separado de favoritos y playlists.

Probado en emulador: foco, reproducción de radio, registro real en Historial y nueva reproducción desde ese historial.

## Cambios de r17

Ecualizador con barras, bloques, puntos, onda, espejo, radial y osciloscopio; orden natural de frecuencias restaurado. Video a pantalla completa con controles pequeños en una esquina que se ocultan al reproducir; OK pausa y reproduce. Señal HD propia de La 100, según disponibilidad de la emisora.

Inicio con favoritos y sugerencias del catálogo, géneros, radios y seis podcasts de sus editores. Los episodios se consultan en feeds RSS públicos al abrir cada programa. Navegación espacial con el mando, foco visible, vuelta al principio de las filas, carga flotante y guía de tono alineada. Crintsoft es el último respaldo de letras automáticas y usa su servicio HTTP legado.

Probado en emulador Android TV API34; la respuesta y la decodificación pueden variar en cada televisor. Desde r16: Ajustes → Actualizaciones → Buscar actualización ahora.

## Android celular

[Descargar versión r12](phone/ChainReactionMusic-Phone-0.1.0-demo1-r12-v15.apk)

Primera versión con actualizador móvil. Versiones anteriores necesitan este primer APK manual. Instalar sobre la anterior sin desinstalar, para conservar biblioteca, skins y preferencias. Después: Ajustes → Actualizaciones → Buscar actualización ahora. Android exige confirmar cada instalación.

Modo día, tono con imagen personalizada y perfiles de preferencias probados físicamente en ZTE Blade A54. 140 pruebas y lint sin errores. Navegación TV y cambio real de calidad de video no forman parte de esa prueba física. Canal independiente phone/latest.json, paquete com.chainreactionmusic.android y misma firma anterior. La versión TV publicada no cambia.

### Celular r12

Campo de búsqueda y lupa visibles en Inicio; Skins en el menú inferior. Probado en ZTE: búsqueda real, regreso a Inicio, selector de skins y conservación de datos. La versión TV publicada no cambia.
