from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://wiki.lcv-group.net/index.php/Verification_du_matin")
link = driver.find_element_by_link_text("log in")
link.click()
login = driver.find_element_by_id("wpName1")
pwd = driver.find_element_by_id("wpPassword1")
login.send_keys("wli")
pwd = driver.find_element_by_id("wpPassword1")
pwd.send_keys("")
driver.find_element_by_id("wpLoginAttempt").click()
'''driver.find_element_by_id("Username").send_keys("wli")'''
'''driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + "t")'''

driver.execute_script("window.open('https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python')")


'''driver.close()'''