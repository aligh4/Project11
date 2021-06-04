import Homepage
import Utilities
import pytest
import TestData


class TestSuite():

    browser_name = "chrome"
    driver = Utilities.init_browser(browser_name)

    def test01(self):
        testdata = TestData
        self.driver.get("www.code.burnalong.com")
        print("Expected condition is: ", testdata.expected_url)
        current_url = Homepage.Homepage.get_current_url()
        print("Actual condition is: ", current_url)
        assert current_url == testdata.expected_url
        self.driver.close()
        self.driver.quit()
