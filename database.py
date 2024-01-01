import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'database': 'cosmeticsdb',
    }

    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")

    except Error as e:
        print(f"Error when connecting mysql database: {e}")
        # Raise an exception to indicate the connection failure
        raise Exception("Failed to connect to MySQL database")

    finally:
        # Close the connection in the finally block to ensure it is closed regardless of success or failure
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed")


def add_new_friend():
    try:
        connect_to_mysql()
        
        

    except Exception as e:
        print(f"Error in add_new_friend: {e}")
        # Handle the connection failure or other errors here


if __name__ == "__main__":
    add_new_friend()
