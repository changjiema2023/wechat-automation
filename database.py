import mysql.connector
from mysql.connector import Error

"""
编号
类别： 口红，精华
品牌
分类： 小样，正装
功效
容量
属性
来源
成本
售价
有效期
库存
更新日期
产品描述
图片

"""

"""Write a function to establish a connection to the MySQL database."""
def connect_mysql():
    db_config = {
        'host': 'localhost',    # The host where the MySQL database is located
        'user': 'root',     # The username to connect to the database    
        'password': 'root',   # The password to connect to the database
        'database': 'cosmeticsdb',  # The name of the database to connect to
    }

    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")    # Print a message to indicate a successful connection
            
    except Error as e:
        print(f"Error when connecting mysql database: {e}")
        # Raise an exception to indicate the connection failure
        raise Exception("Failed to connect to MySQL database")
    
    return connection


"""Write a function to close the connection to the MySQL database."""
def close_mysql(connection):
    connection.close()
    print("Connection closed")





CUSTOMER_INSERT_QUERY = "INSERT INTO customer (姓名, 性别, 创建日期) VALUES (%(姓名)s, %(性别)s, %(创建日期)s)"
CUSTOMER_SEARCH_QUERY = "SELECT * FROM customer WHERE 姓名 = %(姓名)s AND 性别 = %(性别)s AND 创建日期 = %(创建日期)s"

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=5,
    user='root',
    password='root',
    host='localhost',
    database='cosmeticsdb'
)

def add_new_customer(name, gender, time_string):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    entry_data = {
        "姓名": name,
        "性别": gender,
        "创建日期": time_string,
    }

    cursor.execute(CUSTOMER_SEARCH_QUERY, entry_data)
    result = cursor.fetchone()

    if result:
        print(f"Already had customer {name} in the database")
    else:
        cursor.execute(CUSTOMER_INSERT_QUERY, entry_data)
        # Commit the changes to the database
        connection.commit()
        print(f"Added customer {name} to database")

    # Close the cursor and connection
    cursor.close()
    connection.close()