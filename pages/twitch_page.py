from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class TwitchPage(BasePage):

    BROWSE_BUTTON = (By.XPATH, "//a[@href='/directory']")
    CATEGORIES = (By.XPATH, "//img[@class='tw-image']")
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    STREAMERS = (By.XPATH, "(//div[@class='Layout-sc-1xcs6mc-0 eynyeD'])[9]")
    OVERLAY = (By.CSS_SELECTOR, "[data-a-target='player-overlay-click-handler']")
    VIDEO_PLAYER = (By.XPATH, "//div[@data-a-target='ax-overlay']")
    
    def open_twitch(self):
        self.open("https://m.twitch.tv")
        assert "Twitch" in self.driver.title, "Title is not expected"
        self.wait.until(lambda d: "twitch" in d.title.lower())
        time.sleep(1)
        self.screenshot("01_home")

    def click_browse(self):
        self.click(self.BROWSE_BUTTON)
        self.wait.until(
            EC.presence_of_element_located(self.CATEGORIES)
        )
        self.screenshot("02_browse")

    def search(self, text):
        self.type(self.SEARCH_INPUT, text)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        self.wait.until(EC.visibility_of_element_located(self.STREAMERS))
        self.screenshot("03_search")
        
    def scroll(self):
        self.scroll_down(2)
        self.screenshot("04_scroll")

    def click_first_streamer(self):
        self.click(self.STREAMERS)
        assert "twitch.tv" in self.driver.current_url
        self.wait.until(EC.visibility_of_element_located(self.VIDEO_PLAYER))
        self.wait.until(EC.presence_of_element_located(self.VIDEO_PLAYER))
        self.wait.until(EC.visibility_of_element_located(self.OVERLAY))
        time.sleep(2)
        self.screenshot("05_stream_open")
  
    def verify_stream_loaded(self):
        assert self.driver.find_element(*self.VIDEO_PLAYER).is_displayed()        
        self.wait.until(EC.presence_of_element_located(self.VIDEO_PLAYER))
        self.wait.until(EC.visibility_of_element_located(self.VIDEO_PLAYER))
        assert "twitch.tv" in self.driver.current_url
        