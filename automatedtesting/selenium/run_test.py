# #!/usr/bin/env python

import sys
import datetime
from login import login
from fill_cart import fill_cart
from go_to_cart import go_to_cart
from empty_cart import empty_cart

try:
    driver = login(sys.argv, 'standard_user', 'secret_sauce')
    fill_cart(driver)
    go_to_cart(driver)
    empty_cart(driver)
    print(str(datetime.datetime.now()) + ' UI tests PASSED')
except:
    print(str(datetime.datetime.now()) + ' UI tests FAILED')
    exit(1)
