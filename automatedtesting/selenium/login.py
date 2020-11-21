# #!/usr/bin/env python
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback

# Start the browser and login with standard_user
def login (argv, user, password):
    try:
        options = ChromeOptions()
        for arg in argv:
            options.add_argument(arg)
        if '--headless' in argv:
            print ('Running the tests in headless mode...')
            # settings are very linux-centric
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-setuid-sandbox")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--remote-debugging-port=9222")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.binary_location = "/usr/lib/chromium-browser"
        else:
            print ('Starting the browser...')
        driver = webdriver.Chrome(options=options)
        print ('Browser started successfully. Navigating to the demo page to login.')
        driver.get('https://www.saucedemo.com/')
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, 'login-button'))
        )
        driver.find_element_by_id('user-name').send_keys(user)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('login-button').click()
        print(str(datetime.datetime.now()) + ' login PASSED')
        return driver
    except:
        traceback.print_exc()
        raise
