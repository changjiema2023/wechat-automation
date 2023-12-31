#import random
#import time
import pyautogui
import pyscreeze
import random
import time
#import mysql.connector
import location




#location = pyautogui.center(res)
#pyautogui.moveTo(location) # Move the mouse to the location

#def generate_random_coordinates():


'''
def move_and_click(image_location):
    # Check if the image was found
    if image_location is not None:
        # Extract the coordinates of the located image
        left, top, width, height = image_location

        # Calculate a random point within the located image
        random_x = random.randint(left, left + width)
        random_y = random.randint(top, top + height)

        # Move the mouse to the random location
        pyautogui.moveTo(random_x, random_y, duration=2)
        pyautogui.click()
    else:
        print("Discover image not found on the screen.")


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
        (2, 'John Doe', 'Male'),
        (3, 'Jane Smith', 'Female'),
        # Add more rows as needed
    ]

    # SQL query to insert data into the customer table
    insert_query = "INSERT INTO customer (id, name, gender) VALUES (%s, %s, %s)"

    # Execute the query for each row of data
    for customer in customer_data:
        cursor.execute(insert_query, customer)

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()  
'''

if __name__ == "__main__":

    location.main_page()

    '''
    res = pyautogui.locateOnScreen(ABSOLUATE_PATH + "pics\\Chats-green.png", confidence=0.9)
    print(res)

    # Go to main page.
    main_page()

    # send friend
    send_moments()
    '''
 

