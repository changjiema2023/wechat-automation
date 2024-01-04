import util
import const
import sys
import pyautogui
import database
import time
import pyperclip
import mysql_util
from datetime import datetime

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
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    time.sleep(2)
    '''

    is_friend = False
    gender = "Female"
    name = ""
 
    # 检查是否已经是好友
    is_friend = False
    gender = "Female"
    name = ""
 
    if util.locate(const.SEND_MESSAGE):
        is_friend = True
        # 查找微信号
        image_location = util.locate(const.WECHAT_NAME)
        x, y = util.random_location(image_location)
        util.long_press(x, y)
        util.move_and_click_image(const.WECHAT_NAME_COPY)
        name = pyperclip.paste()

        # 查找性别
        if util.locate(const.MALE):
            gender = "Male"

    # 查看‘设置备注和标签’
    err = util.move_and_click_image(const.EDIT_CONTACT)
    if err is not None:
        sys.exit("Stopping the process because couldn't locate edit-contact image.")

    # 查看‘备注’
    image_location = util.locate(const.REMARK)
    x, y = util.random_location(image_location)
    remark_x = x + const.REMAKR_X_EXTENTION
    remark_y = y + const.REMAKR_Y_EXTENTION
    pyautogui.moveTo(remark_x, remark_y, duration=0.5)
    pyautogui.click()
    util.long_press(remark_x, remark_y)
    util.move_and_click_image(const.SELECT_ALL, duration=1)
    util.move_and_click_image(const.COPY, duration=1)
    remark_content = pyperclip.paste()
    if util.is_valid_time_format(remark_content):
        # 如果已经是好友，且数据库中没有，则加入数据库
        if is_friend:
            mysql_util.add_new_customer(name, gender, remark_content)
    else:
        # 生成并修改用户备注
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # 有问题
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        util.move_and_click_image(const.CLEAR_REMARK, duration=1)
        pyautogui.hotkey('ctrl', 'v')



            






if __name__ == "__main__":
    add_friend()