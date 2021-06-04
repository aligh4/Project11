import Test_Suite
import Utilities
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class Homepage():

    def __init__(self):
        self.driver = Test_Suite.TestSuite.driver

    def get_current_url(self):
        driver = self.driver
        return driver.current_url()

