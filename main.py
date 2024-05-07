#import random
#import time
import pyautogui
import pyscreeze
import random
import time
import mysql.connector
import location
from datetime import datetime


#location = pyautogui.center(res)
#pyautogui.moveTo(location) # Move the mouse to the location

#def generate_random_coordinates():


'''
def send_moments():
    # Go to Discover.
    image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + DISCOVER_IMAGE, confidence=0.8)
    move_and_click(image_location=image_location)

    # Go to Moments.
    image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + MOMENTS_IMAGE, confidence=0.8)
    move_and_click(image_location=image_location)

    time.sleep(2)

    # Go to Camera.
    image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + CAMERA_IMAGE, confidence=0.8)
    move_and_click(image_location=image_location)
'''

def insert_db():
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'database': 'cosmeticsdb',
    }

    # Create a connection to the MySQL database
    connection = mysql.connector.connect(**db_config)

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Example data to insert
    customer_data = [
        ('Doe', 'Male', '否', ''),
        # Add more rows as needed
    ]

    # SQL query to insert data into the customer table
    insert_query = "INSERT INTO customer (姓名, 性别, 好友, 创建日期) VALUES (%(姓名)s, %(性别)s, %(好友)s, %(创建日期)s)"

    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    entry_data = {
        "姓名": "Doe",
        "性别": "Male",
        "好友": "否",
        "创建日期": time_string,
    }
    cursor.execute(insert_query, entry_data)
    '''
    # Example data to insert
    customer_data = [
        ('Doe', 'Male', '否', ''),
        # Add more rows as needed
    ]

    # Execute the query for each row of data
    for customer in customer_data:
        cursor.execute(insert_query, customer)
    '''

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close() 


if __name__ == "__main__":
    insert_db()
    #location.main_page()

    '''
    res = pyautogui.locateOnScreen(ABSOLUATE_PATH + "pics\\Chats-green.png", confidence=0.9)
    print(res)
    test

    # Go to main page.
    main_page()

    # send friend
    send_moments()
    '''
 

