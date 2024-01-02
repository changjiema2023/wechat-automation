import mysql.connector
from datetime import datetime

CUSTOMER_INSERT_QUERY = "INSERT INTO customer (姓名, 性别, 好友, 创建日期) VALUES (%(姓名)s, %(性别)s, %(好友)s, %(创建日期)s)"

def add_new_customer():
    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    entry_data = {
        "姓名": "Doe",
        "性别": "Male",
        "好友": "否",
        "创建日期": time_string,
    }
    cursor.execute(CUSTOMER_INSERT_QUERY, entry_data)

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close() 