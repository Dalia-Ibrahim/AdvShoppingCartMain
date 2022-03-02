import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
    sleep(1)
    # Scroll down the page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    # Click on Delete Account button
    driver.find_element(By.CLASS_NAME, "deleteBtnText").click()
    sleep(1)
    # Click on Yes button
    driver.find_element(By.XPATH, '//div[contains(@class, "deleteRed")]').click()
    sleep(1)
    print(f"Your Account deleted successfully at {datetime.datetime.now()}")
    # Condition to check we are in the right url
    if not driver.current_url == locators.advantage_shopping_url:
        driver.get(locators.advantage_shopping_url)
        sleep(7)


def check_homepage():
    # Check that SPEAKERS texts is displayed.
    speakers_element = driver.find_element(By.ID, "speakersTxt").text
    sleep(0.25)
    print(f"You\'re seeing {speakers_element} in homepage")
    # Click on Speaker link
    driver.find_element(By.ID, "speakersTxt").click()
    sleep(0.25)
    # Check SPEAKERS is displayed
    assert driver.find_element(By.XPATH, '//h3[contains(., "SPEAKERS")]').is_displayed()
    sleep(0.75)
    print(f"You\'re in the following page: {driver.current_url}")
    driver.get(locators.advantage_shopping_url)
    # Check that TABLETS texts is displayed.
    tablets_element = driver.find_element(By.ID, "tabletsTxt").text
    sleep(0.25)
    print(f"You\'re seeing {tablets_element} in homepage")
    # Click on TABLETS link
    driver.find_element(By.ID, "tabletsTxt").click()
    sleep(0.25)
    # Check TABLETS is displayed
    assert driver.find_element(By.XPATH, '//h3[contains(., "TABLETS")]').is_displayed()
    sleep(0.75)
    print(f"You\'re in the following page: {driver.current_url}")
    driver.get(locators.advantage_shopping_url)
    # Check that HEADPHONES texts is displayed.
    headphones_element = driver.find_element(By.ID, "headphonesTxt").text
    sleep(0.25)
    print(f"You\'re seeing { headphones_element} in homepage")
    # Click on HEADPHONES link
    driver.find_element(By.ID, "headphonesTxt").click()
    sleep(0.25)
    # Check HEADPHONES is displayed
    assert driver.find_element(By.XPATH, '//h3[contains(., "HEADPHONES")]').is_displayed()
    sleep(0.75)
    print(f"You\'re in the following page: {driver.current_url}")
    driver.get(locators.advantage_shopping_url)
    # Check that LAPTOPS texts is displayed.
    laptops_element = driver.find_element(By.ID, "laptopsTxt").text
    sleep(0.25)
    print(f"You\'re seeing {laptops_element} in homepage")
    # Click on LAPTOPS link
    driver.find_element(By.ID, "laptopsTxt").click()
    sleep(0.25)
    # Check LAPTOPS is displayed
    assert driver.find_element(By.XPATH, '//h3[contains(., "LAPTOPS")]').is_displayed()
    sleep(0.75)
    print(f"You\'re in the following page: {driver.current_url}")
    driver.get(locators.advantage_shopping_url)
    # Check that MICE texts is displayed.
    mice_element = driver.find_element(By.ID, "miceTxt").text
    sleep(0.25)
    print(f"You\'re seeing {mice_element} in homepage")
    # Click on MICE link
    driver.find_element(By.ID, "miceTxt").click()
    sleep(0.25)
    # Check MICE is displayed
    assert driver.find_element(By.XPATH, '//h3[contains(., "MICE")]').is_displayed()
    sleep(0.75)
    print(f"You\'re in the following page: {driver.current_url}")
    driver.get(locators.advantage_shopping_url)
    # Click by OUR PRODUCTS
    driver.find_element(By.LINK_TEXT, "OUR PRODUCTS").click()
    sleep(0.5)
    # Check that OUR PRODUCTS is displayed.
    assert driver.find_element(By.XPATH, "//a[contains(., 'OUR PRODUCTS')]").is_displayed()
    # Click by SPECIAL OFFER
    driver.find_element(By.LINK_TEXT, "SPECIAL OFFER").click()
    sleep(0.5)
    # Check that SPECIAL OFFER is displayed
    assert driver.find_element(By.XPATH, "//h3[contains(., 'SPECIAL OFFER')]").is_displayed()
    # Click by POPULAR ITEMS
    driver.find_element(By.LINK_TEXT, "POPULAR ITEMS").click()
    sleep(0.5)
    # Check that POPULAR ITEMS is displayed
    assert driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').is_displayed()
    # Click by CONTACT US
    driver.find_element(By.LINK_TEXT, "CONTACT US").click()
    # Check that CONTACT US is displayed
    assert driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
    # Check main logo is displayed.
    assert driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').is_displayed()
    assert driver.find_element(By.XPATH, '//span[contains(., "DEMO")]').is_displayed()
    print("advantage Demo Logo is displayed")


def check_contact_us_form():
    # Click by CONTACT US
    driver.find_element(By.LINK_TEXT, "CONTACT US").click()
    sleep(0.25)
    # Check that CONTACT US is displayed
    assert driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
    # Select LapTop from dropdown-menu
    driver.find_element(By.XPATH, '//select[@name="categoryListboxContactUs"]/option[@value="object:59"]').click()
    sleep(0.25)
    print("You selected first element LapTop")
    # Select HP Chromebook 14 from dropdown-menu
    select = Select(driver.find_element(By.NAME, "productListboxContactUs"))
    select.select_by_visible_text("HP Chromebook 14 G1(ENERGY STAR)")
    print("You selected HP Chromebook 14 G1(ENERGY STAR) ")
    # Enter fake data into Email open field
    driver.find_element(By.NAME, "emailContactUs").send_keys(locators.email)
    sleep(0.25)
    # Enter fake data into Subject open field
    driver.find_element(By.NAME, "subjectTextareaContactUs").send_keys(locators.subject)
    sleep(0.25)
    # Click on Send button
    driver.find_element(By.ID, "send_btnundefined").click()
    sleep(5)
    # Check Thanks message is displayed
    assert driver.find_element(By.XPATH, '//*[contains(@class, "successMessage")]').is_displayed()
    sleep(1)
    thanks_message = driver.find_element(By.XPATH, '//*[contains(@class, "successMessage")]').text
    print(f"{thanks_message}")
    # Check CONTINUE SHOPPING button is displayed
    assert driver.find_element(By.LINK_TEXT, "CONTINUE SHOPPING").is_displayed()
    # Click on CONTINUE SHOPPING button
    driver.find_element(By.LINK_TEXT, "CONTINUE SHOPPING").click()
    sleep(0.25)





