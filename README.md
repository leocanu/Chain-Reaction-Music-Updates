# Chain Reaction Music — instaladores y actualizaciones

Repositorio público de distribución. No contiene el código privado del proyecto ni credenciales.

## Windows

[Descargar candidata Windows 0.1.27](https://github.com/leocanu/Chain-Reaction-Music-Updates/releases/download/windows-v0.1.27-rc1/ChainReactionMusic-Setup-0.1.27.exe) | [Notas de la version](https://github.com/leocanu/Chain-Reaction-Music-Updates/releases/tag/windows-v0.1.27-rc1)

Instalador para Windows 10/11 de 64 bits. Cerrar la app y actualizar sobre la misma carpeta para conservar los datos. Se recomienda exportar primero el respaldo personal.

Incluye Acerca del proyecto con relatos rotativos, etiquetas discretas para identificar las ondas al pasar el mouse y la corrección de empaquetado de proxy_tools. Windows ya no muestra skins de imágenes del repositorio; las skins siguen disponibles en Android celular. Inno Setup compila el instalador e incluye el bootstrapper oficial firmado de WebView2.

Es una **candidata de prueba**, no una version declarada estable. 395 pruebas Python aprobadas (1 omitida), sintaxis JavaScript y compilacion del instalador verificadas. Instalada y abierta desde el acceso directo en otra PC; backend 0.1.27 responde correctamente. El archivo windows/candidate.json contiene version, tamano, SHA256 y enlace al instalador.

## Android: celular r21 / TV r22

JioSaavn para audio cuando coinciden artista principal, título y duración, con YouTube como respaldo. Reproducción a 128 kbps y fuente de descarga a 320 kbps cuando está disponible. El video conserva su fuente anterior.

Iconos de géneros: Bicolor, Siluetas, Tarjetas y Emblemas (vista previa), con opción aleatoria. Selector en Ajustes > Apariencia. El resto del diseño y las letras se mantienen.

177 pruebas Java aprobadas por variante (2 pruebas de red opcionales omitidas en la suite local), lint sin errores y reproducción real de JioSaavn verificada en emuladores de celular API35 y TV API34. En TV también se comprobó letras, cola y navegación con mando. Firma igual a las versiones anteriores. Pendiente prueba en dispositivos físicos.

## Android TV

[Descargar versión r22](tv/ChainReactionMusic-TV-0.1.0-demo1-r22-v38.apk)

Instalar sobre la versión anterior, sin desinstalar, para conservar favoritos y ajustes. Android puede pedir autorizar instalaciones desde esta aplicación. El archivo tv/latest.json anuncia la versión, tamaño, SHA256 y enlace HTTPS; la aplicación verifica identidad, versión y firma del APK.

TV versionCode 38, Android 8 o posterior. La apariencia de TV conserva sus temas y colores; la galería de skins del repositorio queda solo en Android celular. Las futuras versiones deben conservar el nombre de paquete y la misma clave de firma.

## Cambios de r21

Acerca del proyecto muestra el logo y diez relatos originales que cambian al abrir la página, con el año 2026. Se retiró de TV la galería de skins de imágenes del repositorio; sigue disponible en Android celular. Validado con 157 pruebas Java por variante (celular y TV) y compilación de ambos APK. Prueba en televisor físico pendiente.

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

[Descargar versión r22](phone/ChainReactionMusic-Phone-0.1.0-demo1-r22-v25.apk)

Primera versión con actualizador móvil. Versiones anteriores necesitan este primer APK manual. Instalar sobre la anterior sin desinstalar, para conservar biblioteca, skins y preferencias. Después: Ajustes → Actualizaciones → Buscar actualización ahora. Android exige confirmar cada instalación.

Modo día, tono con imagen personalizada y perfiles de preferencias probados físicamente en ZTE Blade A54. 140 pruebas y lint sin errores. Navegación TV y cambio real de calidad de video no forman parte de esa prueba física. Canal independiente phone/latest.json, paquete com.chainreactionmusic.android y misma firma anterior. La versión TV publicada no cambia.

### Celular r22: Explorar

Icono y nombre alineados, botones con fondo sutil y bordes redondeados, respuesta al toque y 26 categorias con iconos representativos. Se conservan las cuatro colecciones, el selector de Ajustes y la opcion aleatoria. Dance y Electro tienen dibujos distintos; el contraste se adapta a claro y oscuro.

177 pruebas Java aprobadas por variante, lint sin errores y prueba nativa de 208 celdas en ambas apariencias, repetida con pantalla de 360 dp y fuente al 130%. APK compatible con la firma anterior; telefono fisico pendiente.

### Celular r20

Acerca del proyecto con logo, diez relatos originales rotativos y año 2026. Se conserva el selector de skins en el celular. Probado con 157 pruebas Java y APK firmado con el certificado de las versiones publicadas.

### Celular r12

Campo de búsqueda y lupa visibles en Inicio; Skins en el menú inferior. Probado en ZTE: búsqueda real, regreso a Inicio, selector de skins y conservación de datos. La versión TV publicada no cambia.
