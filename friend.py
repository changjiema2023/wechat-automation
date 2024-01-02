import util
import const
import sys
import pyautogui
import database
import time
import pyperclip

DAILY_MAX_REQUEST=3
START_LOCATION=(66, 306, 135, 112)

def add_friend():
    # Go to group. Temporary
    '''
    # 群成员页面.
    try:
        util.move_and_click(const.THREE_DOTS)
        print("Reach group member page.")
    except ValueError as e:
        print(f"Error reaching group member page: {e}")
        sys.exit("Stopping the process because couldn't reach group member page.")

    err = util.move_and_click_image(const.THREE_DOTS)
    if err is not None:
        sys.exit("Stopping the process because couldn't locate three-dots image.")
    '''

    #iterate = 1
    #while iterate < DAILY_MAX_REQUEST:

    # Move to the first group member.
    '''
    x, y = util.random_location(START_LOCATION)
    pyautogui.moveTo(x, y, duration=2)
    pyautogui.click()
    time.sleep(2)
    '''

    # 检查是否已经是好友
    is_friend = False
    '''
    if util.locate(const.SEND_MESSAGE):
        is_friend = True
    '''
    '''
    # 查看‘设置备注和标签’
    err = util.move_and_click_image(const.EDIT_CONTACT)
    if err is not None:
        sys.exit("Stopping the process because couldn't locate edit-contact image.")
    '''


    # 查看‘备注’
    image_location = util.locate(const.REMARK)
    x, y = util.random_location(image_location)
    remark_x = x + const.REMAKR_X_EXTENTION
    remark_y = y + const.REMAKR_Y_EXTENTION
    util.long_press(remark_x, remark_y)
    util.move_and_click_image(const.SELECT_ALL, duration=1)
    util.move_and_click_image(const.COPY, duration=1)
    remark_content = pyperclip.paste()
    if util.is_valid_time_format(remark_content):
        # check if he is already a friend. If not,
        if is_friend:
            
    else:
        # Generate a new remark 
        # Add the new member to database

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