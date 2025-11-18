import time
from selenium import webdriver
driver = webdriver.Chrome()

def test_search_example():
    """ Search some phrase in google and make a screenshot of the page. """
    # Open google search page:
    driver.get('https://google.com')
    # Find the field for search text input:
    search_input = driver.find_element('name','q')
    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')
    time.sleep(1)  # for demonstration
    # Click search:
    search_button = driver.find_element('name','btnK')
    # search_button.submit()
    search_button.click()
    time.sleep(2)  # for demonstration
    # Make the screenshot of browser window:
    driver.save_screenshot('result.png')
