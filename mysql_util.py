import mysql.connector
from datetime import datetime
import database


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