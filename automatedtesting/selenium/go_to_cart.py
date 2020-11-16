# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback

def go_to_cart(driver: webdriver):
    try:
        WebDriverWait(driver, 3).until(
            # As invoked in this sequence, not wait here - but make no assumptions
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_link'))
        )
        driver.find_element_by_class_name('shopping_cart_link').click()
    except:
        traceback.print_exc()
        raise
