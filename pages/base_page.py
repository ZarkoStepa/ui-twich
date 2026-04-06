import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self, url):
        self.driver.get(url)
        
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return element

    def screenshot(self, name):
        path = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(path)

    def scroll_down(self, times=1):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 800)")
            #time.sleep(1)