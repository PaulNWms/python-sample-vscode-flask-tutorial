# #!/usr/bin/env python
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback

# Sticker shock!
def empty_cart(driver: webdriver):
    try:
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'footer'))
        )
        remove_buttons = driver.find_elements_by_class_name('cart_button')
        for remove_button in remove_buttons:
            inventory_item_name = remove_button.find_element_by_xpath('../../a/div').text
            remove_button.click()
            print(str(datetime.datetime.now()) + ' Item "' + inventory_item_name + '" removed from cart.')
        print(str(datetime.datetime.now()) + ' empty_cart PASSED')
    except:
        traceback.print_exc()
        raise
