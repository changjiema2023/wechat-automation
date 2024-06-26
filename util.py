import random
import pyautogui
import pyscreeze
import time
from datetime import datetime
import const
import re
import adbutils

def scroll_down():
    # Create an ADB device object
    adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
    device = adb.device()

    start_x, start_y = const.FIRST_POST_LOCATION[0], const.FIRST_POST_LOCATION[1]
    end_x, end_y = start_x, start_y + const.PRODUCT_SCROLL_DOWN_DISTANCE

    # Scroll down the screen for the distance of one post
    device.shell(f"input swipe {start_x} {start_y} {end_x} {end_y}")

def generate_random_coordinates(x, y):
    """Generate random coordinates within the screen resolution."""
    random_x = random.randint(x - const.RANGE_ON_X_AXIS, x + const.RANGE_ON_X_AXIS)
    random_y = random.randint(y - const.RANGE_ON_Y_AXIS, y + const.RANGE_ON_Y_AXIS)
    return random_x, random_y

def move_and_click(x, y, range, duration=const.MOVING_SPEED):
    random_x, random_y = x, y

    """Move the mouse to the specified location within a specific range and click."""
    if range:
        random_x, random_y = generate_random_coordinates(x, y)

    pyautogui.moveTo(random_x, random_y, duration)
    pyautogui.click()
    time.sleep(1)


def long_press(x, y, duration=const.MOVING_SPEED, press_duration=2):
    random_x, random_y = generate_random_coordinates(x, y) 
    pyautogui.moveTo(x, y, duration)

    # Simulate a mouse press
    pyautogui.mouseDown()

    # Wait for the specified duration (long press)
    time.sleep(press_duration)

    # Release the mouse button
    pyautogui.mouseUp()
    time.sleep(0.5)


def get_brand_and_product(clipboard_content, product_item):
    brands_pattern = '|'.join(re.escape(brand) for brand in const.BRANDS)
    brands_regex = re.compile(brands_pattern)

    products_pattern = '|'.join(re.escape(product) for product in const.PRODUCTS)
    products_regex = re.compile(products_pattern)

    brand, product, capacity, valid = "", "", "", ""
    effects = ""
    price = 0

    filename = const.ABSOLUATE_PATH + "product.txt"
    for line in clipboard_content:
        if "专柜" in line:
            continue

        # search for brand
        match = brands_regex.search(line)
        if match:
            brand = match.group()
            
            # with open(filename, 'w', encoding='utf-8') as file:
            #     file.write(matched_brand)

        # search for product
        match = products_regex.search(line)
        if match:
            product = match.group()


        # search for capacity
        if capacity == "":      
            capacity = get_capacity(line)

        if effects == "":
            effects = get_effect(line)            

        # search for price
        price_match = re.search(r'💰(\d+)', line)
        if price_match:
            buy_price = float(price_match.group(1))

        # search for valid
        valid_match = re.search(r'效期(\d+)', line)
        if valid_match:
            valid_thru = valid_match.group(1)

    #output = f"Brand: {brand}, Product: {product}, Capacity: {capacity}, Price: {price}, valid: {valid}"
    #with open(filename,  'w', encoding='utf-8') as file:
     #   file.write(output)
    
    product_item.类别 = product
    product_item.品牌 = brand
    product_item.功效 = effects
    product_item.容量 = capacity
    product_item.成本 = buy_price
    product_item.有效期 = valid_thru


def get_capacity(line):
    # Find the capacity in the string
    capacity_match = re.search(r'(\d+ml\*\d+)', line)
    weight_match = re.search(r'(\d+\.?\d*g)', line)
    capacity = ""

    # Extract the capacity
    if capacity_match:
        capacity = capacity_match.group(1)
    elif weight_match:
        capacity = weight_match.group(1)

    return capacity

def get_effect(line):
    effects = ""

    for effect in const.EFFECTS:
        if effect in line:
            effects += effect + " "

    """remove the last space"""
    effects = effects[:-1]

    return effects

def get_capacity_and_price(third_line):
    # Find the capacity and price in the string
    capacity_match = re.search(r'(\d+ml\*\d+)', third_line)
    price_match = re.search(r'💰(\d+)', third_line)

    # Extract the capacity and price
    capacity = capacity_match.group(1) if capacity_match else None
    price = int(price_match.group(1)) if price_match else None

    print(f"Capacity: {capacity}, Price: {price}")
 
    return capacity, price






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