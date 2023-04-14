import os
import mysql.connector
from constantes import FECHA_ACTUAL

def conectDb():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor
    except:
        print("No se pudo realizar la conexión a la base de datos")
        return None, None

def getAllNotifications():
    connection, cursor = conectDb()

    if(connection and cursor):

        query = "SELECT title, message FROM notifies WHERE time_to_notify LIKE '" + \
            FECHA_ACTUAL + "%';"

        cursor.execute(query)

        records = cursor.fetchall()

        connection.close()
        cursor.close()

        return records
    else:
        return None