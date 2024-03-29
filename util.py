import random
import pyautogui
import pyscreeze
import time
from datetime import datetime
import const

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

def move_and_click_image(image_path, duration=1):
    image_location = locate(image_path)

    # Check if the image was found
    if image_location is not None:
        x, y = random_location(image_location)

        # Move the mouse to the random location
        pyautogui.moveTo(x, y, duration)
        pyautogui.click()
        time.sleep(1)
    else:
        #print("image " + image_path + " is not found on the screen")

        error_message = f"Image {image_path} is not found on the screen"
        # Raise a ValueError with the error message
        raise ValueError(error_message)
    
def move_and_click_location(x, y, duration=1):
    random_x = random.randint(x, x + const.RANGE)
    random_y = random.randint(y, y + const.RANGE)    
    pyautogui.moveTo(random_x, random_y, duration)
    pyautogui.click()
    
def long_press(x, y, duration=1):
    # Move the mouse to the desired location
    pyautogui.moveTo(x, y, duration)

    # Simulate a mouse press
    pyautogui.mouseDown()

    # Wait for the specified duration (long press)
    time.sleep(duration)

    # Release the mouse button
    pyautogui.mouseUp()
    time.sleep(1)

def locate(image_path, confidence=0.9, region=None, grayscale=False):
    '''
    Parameters:
    - image_path (str): Path to the image file.
    - confidence (float): The confidence level for the match (default is 0.9).
    - region (tuple): Specify a region of the screen to search in (default is None).
    - grayscale (bool): Set to True to convert the image and screen to grayscale (default is False).

    Returns:
    - tuple or None: If the image is found, returns the location (x, y, width, height). If not found, returns None.
    '''
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence, region=region, grayscale=grayscale)
        return location
    except pyautogui.ImageNotFoundException:
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def random_location(coordinates):
    # Extract the coordinates of the located image
    left, top, width, height = coordinates

    # Calculate a random point within the located image
    random_x = random.randint(left, left + width)
    random_y = random.randint(top, top + height)

    return random_x, random_y

def is_valid_time_format(time_string, format="%Y-%m-%d %H:%M:%S"):
    try:
        # Attempt to parse the string according to the specified format
        datetime.strptime(time_string, format)
        return True
    except ValueError:
        # ValueError is raised if the string does not match the specified format
        return False