from time import time

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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "event-row-container")))

except Exception as e:
    print(e)
    driver.close()
    exit()

# get all elements with class name "event-row-container ng-scope"

matches = driver.find_elements(
    By.CSS_SELECTOR, "div.event-row-container.ng-scope")


sure_bet_odds = []
double_chance_odds = []
over_under_odds = []

for match in matches[:5]:
    # teams
    teams_container = match.find_element(
        By.CSS_SELECTOR, "div.event-details")

    # odds
    odds_containers = match.find_elements(
        By.CSS_SELECTOR, "div.event-market.market-3-way.event-market-availables-count-0.market-selections-3")

    # 3-way
    sure_bets = odds_containers[0].find_elements(
        By.CSS_SELECTOR, "div.event-selection.ng-scope"
    )

    team_odds = {
        "bookmaker": "Sportpesa",
        "match": teams_container.text.replace("\n", " v ").lower(),
        "odds": []
    }

    for sure_bet in sure_bets:
        team_odds["odds"].append(sure_bet.text)

    sure_bet_odds.append(team_odds)

    # double chance
    if len(odds_containers) < 2:
        continue

    # double_chance = odds_containers[1].find_elements(
    #     By.CSS_SELECTOR, "div.event-selection.ng-scope"
    # )

    # team_odds_double = {
    #     "bookmaker": "Sportpesa",
    #     "match": teams_container.text.replace("\n", " v ").lower(),
    #     "odds": []
    # }

    # for double_chance_bet in double_chance:
    #     team_odds_double["odds"].append(double_chance_bet.text)

    # double_chance_odds.append(team_odds_double)

    # # over/under
    # over_under = odds_containers[2].find_elements(
    #     By.CSS_SELECTOR, "div.event-selection.ng-scope"
    # )

    # team_odds_over_under = {
    #     "bookmaker": "Sportpesa",
    #     "match": teams_container.text.replace("\n", " v ").lower(),
    #     "odds": []
    # }

    # for over_under_bet in over_under:
    #     team_odds_over_under["odds"].append(over_under_bet.text)

    # over_under_odds.append(team_odds_over_under)


print(f"double chance odds🎯🎯 {sure_bet_odds}")
print("==========================")
print(f"over/under odds🎯🎯 {double_chance_odds[:3]}")


print(len(matches))


# time.sleep(3)

driver.close()

[
    {'bookmaker': 'Sportpesa', 'match': '15/06/24 - 23:00 | id: 2754 v hfx wanderers fc v forge fc',
        'odds': ['1.57', '1.25', '1.24']},
    {'bookmaker': 'Sportpesa', 'match': '15/06/24 - 23:00 | id: 3076 v ponte preta v novorizontino sp', 'odds': [
        '1.33', '1.36', '1.31']},
    {'bookmaker': 'Sportpesa', 'match': '15/06/24 - 23:00 | id: 3099 v csa al v botafogo pb',
        'odds': ['1.51', '1.21', '1.31']}
]
