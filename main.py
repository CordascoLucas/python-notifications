import os
from dotenv import load_dotenv
from plyer import notification
import mysql.connector
from datetime import datetime

load_dotenv()


def notifyUser(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Reminder",
        app_icon=os.getenv('ICON_PATH'),
        timeout=10
    )


def conectDb():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

    if connection.is_connected():
        cursor = connection.cursor()
        return connection, cursor
    else:
        return None, None


def getAllNotifications():
    connection, cursor = conectDb()

    if(connection and cursor):

        fecha_actual = datetime.today().strftime('%Y-%m-%d')

        query = "SELECT title, message FROM notifies WHERE time_to_notify LIKE '" + \
            fecha_actual + "%';"

        cursor.execute(query)

        records = cursor.fetchall()

        connection.close()
        cursor.close()

        return records

    else:
        return None


def sendNotifies():
    notifies = getAllNotifications()

    if(notifies):
        for notis in notifies:
            notifyUser(notis[0], notis[1])
    else:
        notify("Error", "se produjo un error en la conexion")


def main():
    sendNotifies()


if __name__ == "__main__":
    main()
