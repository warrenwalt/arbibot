from time import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.bet365.com/#/HO/")
time.sleep(20)

clickable = driver.find_element(
    By.CLASS_NAME, "hm-MainHeaderRHSLoggedOutWide_Join")
ActionChains(driver)\
    .move_to_element(clickable)\
    .pause(1)\
    .click()\
    .perform()


time.sleep(60)

driver.close()
