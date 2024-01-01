import util
import const
import sys
import pyautogui

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
   
    # Move to the first group member.
    x, y = util.random_location(START_LOCATION)
    pyautogui.moveTo(x, y, duration=2)
    pyautogui.click()

    iterate = 1
    while iterate < DAILY_MAX_REQUEST:
        image_location = util.locate(const.ADD_TO_CONTACTS)
        if image_location:
            # add it to the database
            print
            iterate = iterate + 1
        else:
            # Check friend state.
            






if __name__ == "__main__":
    add_friend()