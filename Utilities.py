from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def init_browser(browser_name):

        if browser_name.lower() == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name.lower() == 'firefox':
            driver = webdriver.Firefox(GeckoDriverManager().install())
        else:
            raise Exception('Invalid input, please choose a valid browser')
        return driver
