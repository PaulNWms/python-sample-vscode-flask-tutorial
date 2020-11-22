# #!/usr/bin/env python
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback

# Shopping spree
def fill_cart(driver: webdriver):
    try:
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'footer'))
        )
        products = {}
        inventory_item_names = driver.find_elements_by_class_name('inventory_item_name')
        for inventory_item_name in inventory_item_names:
            add_to_cart_button = inventory_item_name.find_element_by_xpath('../../../div[@class="pricebar"]/button')
            products[inventory_item_name.text] = add_to_cart_button
        for product, button in products.items():
            button.click()
            print(str(datetime.datetime.now()) + ' "' + product + '" added to cart.')

        print(str(datetime.datetime.now()) + ' fill_cart PASSED')
    except:
        traceback.print_exc()
        raise
