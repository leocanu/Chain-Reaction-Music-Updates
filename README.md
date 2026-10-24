# Chain Reaction Music — instaladores y actualizaciones

Repositorio público de distribución. No contiene el código privado del proyecto ni credenciales.

## Android TV

[Descargar versión r16](tv/ChainReactionMusic-TV-0.1.0-demo1-r16-v31.apk)

Instalar sobre la versión anterior, sin desinstalar, para conservar favoritos y ajustes. Android puede pedir autorizar instalaciones desde esta aplicación. En r16: Ajustes → Actualizaciones permite comprobar nuevas versiones; la comprobación al abrir se limita a una vez por día y se puede desactivar. La descarga requiere elegir Actualizar ahora y la instalación requiere confirmación de Android.

El archivo `tv/latest.json` anuncia la versión disponible con tamaño, SHA256 y enlace HTTPS. La aplicación verifica también identidad, versión y firma del APK. No contiene publicidad ni claves de acceso al repositorio privado.

TV versionCode31, Android8 o posterior. Versión de prueba; validar funcionamiento en cada televisor. Las futuras versiones deben conservar el nombre de paquete y la misma clave de firma. Publicar primero el APK y actualizar el manifiesto al final.
