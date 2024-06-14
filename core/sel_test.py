from time import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

clickable = driver.find_element(By.TAG_NAME, "textarea")
ActionChains(driver)\
    .move_to_element(clickable)\
    .pause(1)\
    .click()\
    .pause(1)\
    .send_keys("Lionel Messi" + Keys.ENTER)\
    .pause(1)\
    .perform()


time.sleep(10)

driver.close()
