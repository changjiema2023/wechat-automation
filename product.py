import pyautogui
import util
import const
import pyperclip



def read_product():
    # Assume we are at the page Friend
    # Click on the first post
    util.move_and_click(const.FIRST_POST_LOCATION[0], const.FIRST_POST_LOCATION[1], True)

    util.long_press(const.PRODUCT_DESCRIPTION_LOCATION[0], const.PRODUCT_DESCRIPTION_LOCATION[1])

    # Click copy button in the product description
    util.move_and_click(const.PRODUCT_DESCRIPTION_LOCATION[0] + const.COPY_LOCATION_RELATIVE_TO_PRODUCT_DESCRIPTION_LOCATION[0], 
                        const.PRODUCT_DESCRIPTION_LOCATION[1] + const.COPY_LOCATION_RELATIVE_TO_PRODUCT_DESCRIPTION_LOCATION[1], False)
    

    #util.print_clipboard_content(pyperclip.paste())
    """
    filename = const.ABSOLUATE_PATH + "product.txt"
    clipboard_content = pyperclip.paste()
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(clipboard_content)
    """

    clipboard_content = pyperclip.paste().split('\n')

    util.get_brand_and_product(clipboard_content)

    # effect = util.get_effect(clipboard_content[1])

    # capacity, price = util.get_capacity_and_price(clipboard_content[2])