import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Registering the new user


def create_new_user():
    driver.find_element(By.XPATH, '//a[@title="USER"]//*[@id="menuUser"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').click()
    # driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//h3[contains(.,"ACCOUNT DETAILS")]').is_displayed()
    # Enter fake data into Username open field
    driver.find_element(By.NAME, "usernameRegisterPage").send_keys(locators.new_username)
    sleep(0.25)
    # Enter fake data into Email open field
    driver.find_element(By.NAME, "emailRegisterPage").send_keys(locators.email)
    sleep(0.25)
    # Enter fake data into Password open field
    driver.find_element(By.NAME, "passwordRegisterPage").send_keys(locators.new_password)
    sleep(0.25)
    # Enter fake data into Confirm password open field
    driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(locators.new_password)
    sleep(0.25)
    # Enter fake data into First Name open field
    driver.find_element(By.NAME, "first_nameRegisterPage").send_keys(locators.first_name)
    sleep(0.25)
    # Enter fake data into Last Name open field
    driver.find_element(By.NAME, "last_nameRegisterPage").send_keys(locators.last_name)
    sleep(0.25)
    # Enter fake data into Phone Number open field
    driver.find_element(By.NAME, "phone_numberRegisterPage").send_keys(locators.phone_number)
    sleep(0.25)
    # Enter fake data into Country open field
    driver.find_element(By.NAME, "countryListboxRegisterPage").send_keys(locators.country)
    sleep(0.25)
    # Enter fake data into City open field
    driver.find_element(By.NAME, "cityRegisterPage").send_keys(locators.city)
    sleep(0.25)
    # Enter fake data into Address open field
    driver.find_element(By.NAME, "addressRegisterPage").send_keys(locators.address)
    sleep(0.25)
    # Enter fake data into Province_abbreviation open field
    driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage").send_keys(locators.province)
    sleep(0.25)
    # Enter fake data into PostalCode open field
    driver.find_element(By.NAME, "postal_codeRegisterPage").send_keys(locators.postal_code)
    sleep(0.25)
    # Uncheck "Receive exclusive offers and promotions from Advantage"
    driver.find_element(By.NAME, "allowOffersPromotion").click()
    sleep(0.25)
    # Check that Register button inactive
    if not driver.find_element(By.ID, "register_btnundefined").is_enabled():
        # Click on "I agree....."
        driver.find_element(By.NAME, "i_agree").click()
        sleep(0.25)
        # Click Register button
        driver.find_element(By.ID, "register_btnundefined").click()
        sleep(1)
        # Check Username is displayed.
        assert driver.find_element(By.XPATH, '//*[contains(@class, "containMiniTitle")]').is_displayed()
        print(f'--- User with the name {locators.new_username} is displayed. Test Passed ---')
        print(f"You\'ve registered successfully at: {datetime.datetime.now()}")
    else:
        print(f"Something went wrong, Try again!")


def user_navigator():
    # Click by your username account
    driver.find_element(By.XPATH, '//*[contains(@class, "containMiniTitle")]').click()
    sleep(0.25)
    # Select My Account
    driver.find_element(By.XPATH, '//label[@role="link"][contains(., "My account")]').click()
    sleep(0.25)
    # Check Full name is displayed.
    if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
        print(f'--- User with the full name {locators.full_name} is displayed. Test Passed ---')
    # Click by your username account
    driver.find_element(By.XPATH, '//*[contains(@class, "containMiniTitle")]').click()
    sleep(0.25)
    # Select My Orders
    driver.find_element(By.XPATH, '//label[@role="link"][contains(., "My orders")]').click()
    sleep(0.25)
    # Check that is - No orders -
    order = driver.find_element(By.XPATH, '//label[contains(., "- No orders -")]').text
    print(f"You don\'t have any order! This shown message is: {order}")
    # Click by your username account
    driver.find_element(By.XPATH, '//*[contains(@class, "containMiniTitle")]').click()
    sleep(0.25)
    # Select Sign out
    driver.find_element(By.XPATH, '//label[@role="link"][contains(., "Sign out")]').click()
    sleep(1)
    print(f"You\'ve successfully signed out")

# Log In method with dynamic username and password


def log_in(username, password):
    if driver.current_url == locators.advantage_shopping_url:
        # Click on USER icon
        driver.find_element(By.XPATH, '//a[@title="USER"]//*[@id="menuUser"]').click()
        sleep(2)
        # Enter the Username open field
        driver.find_element(By.NAME, "username").send_keys(username)
        sleep(1)
        # Enter the Password open field
        driver.find_element(By.NAME, "password").send_keys(password)
        sleep(1)
        # Click on SIGN IN button
        driver.find_element(By.XPATH, '//sec-sender/button[contains(., "SIGN IN")]').click()
        sleep(1)
        if driver.find_element(By.XPATH, '//*[contains(@class, "containMiniTitle")]').is_displayed():
            print(f'You\'ve successfully logged in--- with username {locators.new_username}is displayed. Test Passed ---')
        else:
            message = driver.find_element(By.XPATH, '//label[@id="signInResultMessage"][contains(., " ")]').text
            print(f"You\'ve entered non-existing credentials.The shown message is: {message}")


def delete_user():
    # Click by your username account
    driver.find_element(By.XPATH, '//*[contains(@class, "containMiniTitle")]').click()
    sleep(0.25)
    # Select My Account
    driver.find_element(By.XPATH, '//label[@role="link"][contains(., "My account")]').click()
    sleep(0.25)
    # Scroll down the page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    # Click on Delete Account button
    driver.find_element(By.CLASS_NAME, "deleteBtnText").click()
    sleep(2)
    # Click on Yes button
    driver.find_element(By.XPATH, '//div[contains(@class, "deleteRed")]').click()
    sleep(1)
    print(f"Your Account deleted successfully at {datetime.datetime.now()}")
    # Condition to check we are in the right url
    if not driver.current_url == locators.advantage_shopping_url:
        driver.get(locators.advantage_shopping_url)
        sleep(7)





