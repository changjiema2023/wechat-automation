import mysql.connector

class ProductItem:
    def __init__(self, product, brand, capacity, buy_price, valid_thru):
        self.类别 = product
        self.品牌 = brand
        self.容量 = capacity
        self.成本 = buy_price
        self.有效期 = valid_thru

    def save_to_database(conn, self):
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
        sql = "INSERT INTO products (类别, 品牌, 容量, 成本, 有效期) VALUES (%s, %s, %f, %f, %s)"
        values = (self.类别, self.品牌, self.容量, self.成本, self.有效期)

        # Execute the SQL query
        cursor.execute(sql, values) 

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()



    @staticmethod
    def retrieve_from_database(conn, product):
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
        sql = "SELECT * FROM products WHERE 类别 = %s AND 品牌 = %s AND 容量 = %s AND 成本 = %s AND 有效期 = %s"
        values = (product.类别, product.品牌, product.容量, product.成本, product.有效期)

        # Execute the SQL query
        cursor.execute(sql, values)

        # Fetch the first row from the result set
        row = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # If a row is found, return True and the product instance
        if row:
            return True, ProductItem(row[0], row[1], row[2], row[3], row[4])
        
        # If no row is found, return False and None
        return False, None