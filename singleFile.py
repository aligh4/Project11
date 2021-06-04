from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

"""This is a Low-Level test made in a single script without a supporting framework"""

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://code.burnalong.com")
url = driver.current_url
expected_url = "code.burnalong.com"
if url == expected_url:
    print("The URL's match!")
if url != expected_url:
    print("The URLs do NOT match!")
driver.close()
driver.quit()