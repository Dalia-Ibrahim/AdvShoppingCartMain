import datetime
from selenium import webdriver
import adshopcart_locators as locators
from selenium.webdriver.chrome.service import Service
s = Service(executable_path=r"C:\Users\amr_a\PycharmProjects\python_cctb\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Fixture method - to open web browser


def setUp():
    print(f'Test started at: {datetime.datetime.now()}')
    # Maximize Window
    driver.maximize_window()
    # Let's wait for the browser response in general
    driver.implicitly_wait(30)
    # open Advantage Shopping Browser
    driver.get(locators.advantage_shopping_url)
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_shopping_url and driver.title == " Advantage Shopping":
        print(f"You\'ve successfully entered homepage{driver.current_url}")
        print(f"You\'re seeing title message:{driver.title}")
    else:
        print(f'We\'re not at the advantage Shopping Cart homepage. Check your code!')
        driver.close()
        driver.quit()


# Fixture method - to close web browser
def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
tearDown()

