from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pickle
import pandas as pd


driver = webdriver.Chrome()

driver.get("https://www.betika.com/en-ke/s/soccer")

# wait for page to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "prebet-match")))

except Exception as e:
    print(e)
    driver.close()
    exit()

# scroll down to fetch as many data as possible
# for second in range(1):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)


teams = []
x12 = []
btts = []
dc = []
odds_events = []


def scroll_page():
    htmlElem = driver.find_element(By.TAG_NAME, 'html')
    htmlElem.send_keys(Keys.END)
    # for i in range(1, 15, 1):
    #     time.sleep(2)
    #     continue


def dropdown_menu(option='1x2'):
    options = {
        '1x2': 0,
        'dc': 1,
        '1st Half 1x2': 2,
        'btts': 3
    }

    dropdowns = driver.find_elements(
        By.CLASS_NAME, 'match-filter__button')
    dropdown_button = dropdowns[3]
    dropdown_button.click()
    btts_button = driver.find_elements(
        By.CLASS_NAME,
        'match-filter__group__action')
    time.sleep(3)
    btts_button[options[option]].click()


def x_12(x12):
    sport_title = driver.find_elements(By.CLASS_NAME, 'prebet-match')
    for game in sport_title:
        team = game.find_element(By.CLASS_NAME, 'prebet-match__teams')
        teams.append(team.text)

        odd = game.find_element(By.CLASS_NAME, 'prebet-match__odds')
        x12.append(odd.text)


def both_teams_to_score(btts):
    dropdown_menu(option='btts')
    time.sleep(3)
    # scroll_page()
    sport_title = driver.find_elements(By.CLASS_NAME, 'prebet-match')
    for game in sport_title:
        odd = game.find_element(By.CLASS_NAME, 'prebet-match__odds__container')
        btts.append(odd.text)


def double_chance(dc):
    dropdown_menu(option='dc')
    time.sleep(3)
    # scroll_page()
    sport_title = driver.find_elements(By.CLASS_NAME, 'prebet-match')
    for game in sport_title:
        odd = game.find_element(By.CLASS_NAME, 'prebet-match__odds__container')
        dc.append(odd.text)

# Clean and convert the 'DC' column


def clean_dc(dc_list):
    x2 = dc_list[-1]
    x_12 = dc_list[-2]

    dc_list[-1] = x_12
    dc_list[-2] = x2

    return [float(i) if isinstance(i, str) and i.isdigit() else i for i in dc_list]


# scroll_page()
x_12(x12)
both_teams_to_score(btts)
double_chance(dc)

driver.quit()

'''CLEANING DATA'''
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


dict_gambling = {'Teams': teams, '3-Way': x12, 'BTTS': btts, 'DC': dc}
df_betika = pd.DataFrame.from_dict(dict_gambling)
df_betika = df_betika.map(lambda x: x.strip() if isinstance(x, str) else x)

# replace space with v for teams col
df_betika['Teams'] = df_betika['Teams'].str.replace('\n', ' v ').str.lower()

# change 3-way to array of floats
df_betika['3-Way'] = df_betika['3-Way'].str.split('\n')
df_betika['3-Way'] = df_betika['3-Way'].apply(lambda x: [float(i) for i in x])

# change btts to array of floats
df_betika['BTTS'] = df_betika['BTTS'].str.split('\n')
df_betika['BTTS'] = df_betika['BTTS'].apply(lambda x: [float(i) for i in x])

# change dc to array of floats
df_betika['DC'] = df_betika['DC'].str.split('\n')
df_betika['DC'] = df_betika['DC'].apply(clean_dc)

df_betika.set_index('Teams', inplace=True)

'''SAVE DATA'''
df_betika.to_csv('betika.csv', index=False)
print(df_betika)
print(len(btts))
