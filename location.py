import pyautogui
import pyscreeze
import random
import const
import util

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

def main_page():
    main_page_image_location = pyautogui.locateOnScreen(const.MAIN_PAGE_GREEN_IMAGE, confidence=0.9)

    if main_page_image_location is None:
        # Click Chats-white to go to main page.
        image_location = pyautogui.locateOnScreen(const.MAIN_PAGE_WHITE_IMAGE, confidence=0.9)
        x, y = util.random_location(image_location)

        # Move the mouse to the random location
        pyautogui.moveTo(x, y, duration=2)
        pyautogui.click()

    print("We're at main page.")