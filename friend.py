import util
import const
import sys
import pyautogui
import database
import time

DAILY_MAX_REQUEST=3
START_LOCATION=(66, 306, 135, 112)

def add_friend():
    # Go to group. Temporary
    '''
    # Go to group member page.
    try:
        util.move_and_click(const.THREE_DOTS)
        print("Reach group member page.")
    except ValueError as e:
        print(f"Error reaching group member page: {e}")
        sys.exit("Stopping the process because couldn't reach group member page.")
    '''

    #iterate = 1
    #while iterate < DAILY_MAX_REQUEST:

    # Move to the first group member.
    x, y = util.random_location(START_LOCATION)
    pyautogui.moveTo(x, y, duration=2)
    pyautogui.click()
    time.sleep(2)
    
    # 查看‘设置备注和标签’
    image_location = util.locate(const.EDIT_CONTACT)
    if image_location is None:
        sys.exit("Stopping the process because couldn't locate edit-contact image.")

    util.move_and_click_image(image_location)

    image_location = util.locate(const.REMARK)
    print(image_location)

    '''
    image_location = util.locate(const.ADD_TO_CONTACTS)
    if image_location:
        # add it to the database
        database.add_new_friend()
        print
        iterate = iterate + 1
    else:
        # Check friend state.
    '''
            






if __name__ == "__main__":
    add_friend()