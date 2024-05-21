import mysql.connector

class ProductItem:
    def __init__(self):
        self.类别 = ""
        self.品牌 = ""
        self.功效 = ""
        self.容量 = ""
        self.成本 = ""
        self.有效期 = 0
        self.更新日期 = ""
        self.产品描述 = ""

    def insert_to_database(self):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cosmeticsdb"
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Prepare the SQL query to insert the product item into the database
        sql = "INSERT INTO product (类别, 品牌, 功效, 容量, 成本, 有效期, 更新日期, 产品描述) VALUES (%(类别)s, %(品牌)s, %(功效)s, %(容量)s, %(成本)s, %(有效期)s, %(更新日期)s, %(产品描述)s)"
        values = {'类别': self.类别, '品牌': self.品牌, '功效': self.功效, '容量': self.容量, '成本': self.成本, '有效期': self.有效期, '更新日期': self.更新日期, '产品描述': self.产品描述}

        # Execute the SQL query
        cursor.execute(sql, values) 

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()


    def is_in_database(self):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cosmeticsdb"
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Prepare the SQL query to retrieve the product item from the database
        sql = "SELECT * FROM product WHERE 类别 = %s AND 品牌 = %s AND 功效 = %s AND 容量 = %s AND 成本 = %s AND 有效期 = %s"
        values = (self.类别, self.品牌, self.功效, self.容量, self.成本, self.有效期)

        # Execute the SQL query
        cursor.execute(sql, values)

        # Fetch the first row from the result set
        row = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # If a row is found, return True and the product instance
        if row:
            return True
        
        # If no row is found, return False and None
        return False