# Simple python notifier

La aplicación verifica en la base de datos definida si existe notificacion para la fecha actual y emite una notificación en el escritorio. En caso de haber un problema con la conexión se toman los datos desde un archivo con notificaciones en un diccionario de python llamado "notificaciones.py"

## Prerequisitos

- Crear la base de datos a utilizar
- Cargar las notificaciones de manera manual

## pasos a seguir

- Crear un cron job para que corra el script a un tiempo determinado por día para verificar notificaciones
