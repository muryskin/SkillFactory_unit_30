# import traceback

import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/path/to/chrome'
    # chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--kiosk')
    chrome_options.set_headless(True)
    return chrome_options

@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL']

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get('https://petfriends.skillfactory.ru/login')
    # waiting for login-form:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form[action='/login']")))

    driver.find_element('id', "email").send_keys("muryskin3@gmail.com")
    driver.find_element('id', "pass").send_keys("12345678")

    # Click submit button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # driver.get('https://petfriends.skillfactory.ru/my_pets')
    # waiting for my pets button
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/my_pets']")))

    driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    # waiting for my pets table
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "all_my_pets")))
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_'+rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request):
    browser = webdriver.Chrome()
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):
    if request.node.rep_call.failed:
        # Make the screeshot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screeshot for local debug:
            browser.save_screenshot('screeshots/'+ str(uuid.uuid4()) + '.png')

            # For happy debugging:
            print('URL:', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except:
            pass # just ignore any errors here

