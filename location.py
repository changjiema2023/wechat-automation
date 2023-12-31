import pyautogui
import pyscreeze
import random

ABSOLUATE_PATH="D:\\new-automation\\wechat-automation\\"
BACK_IMAGE="pics\\Back.png"
CHATS_IMAGE="pics\\Chats-white-english.png"
DISCOVER_IMAGE="pics\\Discover-white-english.png"
MOMENTS_IMAGE="pics\\Moments_icon.png"
CAMERA_IMAGE="pics\\Camera.png"
MAIN_PAGE_GREEN_IMAGE="pics\\Chats-green.png"
MAIN_PAGE_WHITE_IMAGE="pics\\Chats-white.png"

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

def main_page():
    main_page_image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + MAIN_PAGE_GREEN_IMAGE, confidence=0.9)

    if main_page_image_location is None:
        # Click Chats-white to go to main page.
        image_location = pyautogui.locateOnScreen(ABSOLUATE_PATH + MAIN_PAGE_WHITE_IMAGE, confidence=0.9)
        left, top, width, height = image_location

        # Calculate a random point within the located image
        random_x = random.randint(left, left + width)
        random_y = random.randint(top, top + height)

        # Move the mouse to the random location
        pyautogui.moveTo(random_x, random_y, duration=2)
        pyautogui.click()

    print("We're at main page.")