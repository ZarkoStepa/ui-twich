import pytest
import os
from selenium import webdriver

@pytest.fixture
def driver():
    mobile_emulation = {
        "deviceName": "iPhone 12 Pro"
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    # create screenshots folder
    os.makedirs("screenshots", exist_ok=True)

    yield driver
    driver.quit()