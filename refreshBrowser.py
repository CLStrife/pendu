from selenium.common.exceptions import *
from selenium import webdriver
import time

url = "https://mantis.lcv-group.net/view_all_bug_page.php"
driver = webdriver.Firefox()
driver.get(url)

while True:
    if driver.current_url == url:
        try:
            time.sleep(5)
            driver.refresh()
        except TimeoutException as ex:
            print(ex.message)

driver.quit
