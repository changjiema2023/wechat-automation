import pyautogui
import util
import const
import pyperclip
import product_db
import datetime

def read_product():
    # Assume we are at the page Friend
    # Click on the first post
    util.move_and_click(const.FIRST_POST_LOCATION[0], const.FIRST_POST_LOCATION[1], True)

    util.long_press(const.PRODUCT_DESCRIPTION_LOCATION[0], const.PRODUCT_DESCRIPTION_LOCATION[1])

    # Copy in the product description
    util.move_and_click(const.PRODUCT_DESCRIPTION_LOCATION[0] + const.COPY_LOCATION_RELATIVE_TO_PRODUCT_DESCRIPTION_LOCATION[0], 
                        const.PRODUCT_DESCRIPTION_LOCATION[1] + const.COPY_LOCATION_RELATIVE_TO_PRODUCT_DESCRIPTION_LOCATION[1], False)
    

    #util.print_clipboard_content(pyperclip.paste())
    
    """
    filename = const.ABSOLUATE_PATH + "product.txt"
    clipboard_content = pyperclip.paste()
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(clipboard_content)
    """

    description = pyperclip.paste()
    """get current time"""

    clipboard_content = pyperclip.paste().split('\n')

    """Create a productItem object"""
    product_item = product_db.ProductItem()
    product_item.产品描述 = description
    product_item.更新日期 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    util.get_brand_and_product(clipboard_content, product_item)

    in_database = product_item.is_in_database()

    if in_database:
        print("Product already in database")
    else:
        print("Product not in database")
        product_item.insert_to_database()
        print("Product is inserted in database")

    # effect = util.get_effect(clipboard_content[1])

    # capacity, price = util.get_capacity_and_price(clipboard_content[2])