#import random
#import time
import pyautogui
import pyscreeze
import random


ABSOLUATE_PATH="D:\\automation\\wechat\\"
DISCOVER_IMAGE="pics\\Discover-white-english.png"


#location = pyautogui.center(res)
#pyautogui.moveTo(location) # Move the mouse to the location

#def generate_random_coordinates():

def send_moments():
    image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + DISCOVER_IMAGE, confidence=0.9)

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




if __name__ == "__main__":
    
    # send friend
    send_moments()
 

