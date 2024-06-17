from time import time
import pandas as pd

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.ke.sportpesa.com/en/sports-betting/football-1/")

# maximize the window
driver.maximize_window()

# wait for page to load
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".event-row-details.event-markets-count-4")))

except Exception as e:
    print(e)
    driver.close()
    exit()

teams = []
x12 = []
btts = []
dc = []


matches = driver.find_elements(
    By.CSS_SELECTOR, '.event-row-details.event-markets-count-4')

for match in matches:
    # teams
    event_details = match.find_element(By.CLASS_NAME, 'event-names')
    teams.append(event_details.text)

    # odds
    odds = match.find_elements(By.CLASS_NAME, 'event-market')

    # 1x2
    x12.append(odds[0].text)

    # btts
    # bt = odds[3].find_element(By.CLASS_NAME, 'ng-binding')
    # print(bt.text)
    # print('------------------')
    btts.append(odds[3].text)

    # dc
    dc.append(odds[1].text)


driver.quit()

'''CLEANING DATA'''
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


dict_gambling = {'Teams': teams, '3-Way': x12, 'BTTS': btts, 'DC': dc}
df = pd.DataFrame(dict_gambling)

# replace space with v for teams col
df['Teams'] = df['Teams'].str.replace('\n', ' v ').str.lower()

# change 3-way to array of floats
df['3-Way'] = df['3-Way'].str.split('\n')
df['3-Way'] = df['3-Way'].apply(lambda x: [float(i)
                                if isinstance(i, str) and len(x) > 1 else i for i in x])

# change dc to array of floats
df['DC'] = df['DC'].str.split('\n')
df['DC'] = df['DC'].apply(
    lambda x: [float(i) if isinstance(i, str) and len(x) > 1 else i for i in x])


'''SAVE DATA'''
df.to_csv('sportpesa.csv', index=False)
# print(df)
print(len(btts))
