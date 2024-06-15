from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import time

AUTH = 'brd-customer-hl_27940302-zone-scraping_arbibot:f79gn2gi0rzf'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'


def main():
    start = time.time()
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get('https://22bet.co.ke/')
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated!')
        print(f'Execution time: {time.time() - start:.2f} seconds')


main()
