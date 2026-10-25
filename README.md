# Chain Reaction Music — instaladores y actualizaciones

Repositorio público de distribución. No contiene el código privado del proyecto ni credenciales.

## Android TV

[Descargar versión r17](tv/ChainReactionMusic-TV-0.1.0-demo1-r17.apk)

Instalar sobre la versión anterior, sin desinstalar, para conservar favoritos y ajustes. Android puede pedir autorizar instalaciones desde esta aplicación. En r16: Ajustes → Actualizaciones permite comprobar nuevas versiones; la comprobación al abrir se limita a una vez por día y se puede desactivar. La descarga requiere elegir Actualizar ahora y la instalación requiere confirmación de Android.

El archivo `tv/latest.json` anuncia la versión disponible con tamaño, SHA256 y enlace HTTPS. La aplicación verifica también identidad, versión y firma del APK. No contiene publicidad ni claves de acceso al repositorio privado.

TV versionCode32, Android8 o posterior. Versión de prueba; validar funcionamiento en cada televisor. Las futuras versiones deben conservar el nombre de paquete y la misma clave de firma. Publicar primero el APK y actualizar el manifiesto al final.

## Cambios de r17

Ecualizador con barras, bloques, puntos, onda, espejo, radial y osciloscopio; orden natural de frecuencias restaurado. Video a pantalla completa con controles pequeños en una esquina que se ocultan al reproducir; OK pausa y reproduce. Señal HD propia de La 100, según disponibilidad de la emisora.

Inicio con favoritos y sugerencias del catálogo, géneros, radios y seis podcasts de sus editores. Los episodios se consultan en feeds RSS públicos al abrir cada programa. Navegación espacial con el mando, foco visible, vuelta al principio de las filas, carga flotante y guía de tono alineada. Crintsoft es el último respaldo de letras automáticas y usa su servicio HTTP legado.

Probado en emulador Android TV API34; la respuesta y la decodificación pueden variar en cada televisor. Desde r16: Ajustes → Actualizaciones → Buscar actualización ahora.
