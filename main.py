import os
from dotenv import load_dotenv
from plyer import notification
from database import getAllNotifications
from constantes import FECHA_ACTUAL
from notificaciones import notificaciones

load_dotenv()

def notifyUser(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Reminder",
        app_icon=os.getenv('ICON_PATH'),
        timeout=10
    )

def sendNotifies():
    notifies = getAllNotifications()

    if(notifies):
        for notis in notifies:
            notifyUser(notis[0], notis[1])
    elif(notificaciones):
        for notificacion in notificaciones:
            if notificacion["fecha"] == FECHA_ACTUAL:
                notifyUser(notificacion["titulo"], notificacion["mensaje"])
    else:
        notification.notify("Error", "se produjo un error en la conexion")

def main():
    sendNotifies()

if __name__ == "__main__":
    main()
