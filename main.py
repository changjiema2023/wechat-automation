#import random
#import time
import pyautogui
import pyscreeze
import random
import time
import mysql.connector
import location
from datetime import datetime
import pygetwindow as gw
import product
import database
import util

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

# Move the window to the desired location.
window_title = "2201117TY"
def move_window_to_top_left(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.moveTo(0, 0)
        print(f"Moved window '{window_title}' to the top-left corner.")
    except IndexError:
        print(f"Window '{window_title}' not found.")

if __name__ == "__main__":
    #insert_db()
    #location.main_page()
    
    #move_window_to_top_left(window_title)
    #database.connect_mysql()
    product.read_product()
    #database.close_mysql()
    #util.scroll_down()

    '''
    res = pyautogui.locateOnScreen(ABSOLUATE_PATH + "pics\\Chats-green.png", confidence=0.9)
    print(res)
    test

    # Go to main page.
    main_page()

    # send friend
    send_moments()
    '''
