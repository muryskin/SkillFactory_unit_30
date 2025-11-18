import time

import pytest
# from selenium import webdriver
from conftest import web_browser
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

def test_show_all_pets(driver):
    # Add email
    driver.find_element('id', "email").send_keys("muryskin3@gmail.com")
    # Add password
    driver.find_element('id', "pass").send_keys("12345678")
    # Click submit button
    # btn_submit = driver.find_element('xpath',"//button[@type='submit']")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    # time.sleep(1)
    assert driver.find_element(By.TAG_NAME,"h1").text == 'PetFriends'

def test_petfriends_2(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")
    # time.sleep(5)
    # Click on the new user button:
    btn_newuser = web_browser.find_element('xpath',"//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()
    # time.sleep(5)
    # Click existing user button
    btn_exist_acc = web_browser.find_element('link text',u"У меня уже есть аккаунт")
    btn_exist_acc.click()
    # Add email
    field_email = web_browser.find_element('id',"email")
    field_email.clear()
    field_email.send_keys("muryskin3@gmail.com")
    # Add password
    field_password = web_browser.find_element('id',"pass")
    field_password.clear()
    field_password.send_keys("12345678")
    # Click submit button
    btn_submit = web_browser.find_element('xpath',"//button[@type='submit']")
    btn_submit.click()
    # time.sleep(5)
    # if web_browser.current_url == "https://petfriends.skillfactory.ru/all_pets":
        # Make the screenshot of browser window
        # web_browser.save_screenshot('result_petfriends.png')
    # else:
    #     raise Exception('login error')
    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"