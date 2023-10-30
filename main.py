#import random
#import time
import pyautogui
import pyscreeze
import random
import time


ABSOLUATE_PATH="D:\\automation\\wechat\\"
BACK_IMAGE="pics\\Back.png"
CHATS_IMAGE="pics\\Chats-white-english.png"
DISCOVER_IMAGE="pics\\Discover-white-english.png"
MOMENTS_IMAGE="pics\\Moments_icon.png"
CAMERA_IMAGE="pics\\Camera.png"


#location = pyautogui.center(res)
#pyautogui.moveTo(location) # Move the mouse to the location

#def generate_random_coordinates():

def main_page():
    image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + BACK_IMAGE, confidence=0.8)
    i = 0
    while image_location is not None and i < 5:
        left, top, width, height = image_location

        # Calculate a random point within the located image
        random_x = random.randint(left, left + width)
        random_y = random.randint(top, top + height)

        # Move the mouse to the random location
        pyautogui.moveTo(random_x, random_y, duration=2)
        pyautogui.click()
        image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + BACK_IMAGE, confidence=0.8)
        i = i + 1

    image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + CHATS_IMAGE, confidence=0.8)
    move_and_click(image_location=image_location)
    print("We're at main page.")


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



if __name__ == "__main__":
    # Go to main page.
    main_page()

    # send friend
    send_moments()
 

