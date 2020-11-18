# #!/usr/bin/env python
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
        add_to_cart_buttons = driver.find_elements_by_class_name('btn_inventory')
        for add_to_cart_button in add_to_cart_buttons:
            add_to_cart_button.click()
        print('fill_cart PASSED')
    except:
        traceback.print_exc()
        raise
