#import random
#import time
import pyautogui
import pyscreeze

ABSOLUATE_PATH="D:\\automation\\wechat\\"


#location = pyautogui.center(res)
#pyautogui.moveTo(location) # Move the mouse to the location

#def generate_random_coordinates():


if __name__ == "__main__":
    
    res = pyautogui.locateOnScreen(ABSOLUATE_PATH + "pics\\Chats-green-chinese.png", confidence=0.9)
    print(res)
    print("test4")