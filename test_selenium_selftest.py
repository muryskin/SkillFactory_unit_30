import pytest
# from selenium import webdriver
# from conftest import web_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_my_pets_are_present(driver):
    """Проверка, что присутствуют все питомцы.
            Т.е. количество питомцев в таблице совпадает с числом питомцев в строке 'Питомцев: N' """
    # driver.save_screenshot("my_pets.png")

    driver.implicitly_wait(10)
    # waiting for visibility numbers of my pets
    myDynamicElement = driver.find_element(By.CSS_SELECTOR, "div.\.col-sm-4.left:nth-of-type(1)")

    # searching text "user \n Питомцев: n \n Друзей: m \n Сообщений: l":
    pets_text = driver.find_element(By.CSS_SELECTOR, "div.\.col-sm-4.left:nth-of-type(1)").text
    # split text for text "Питомцев: n" and then for "n":
    pets_split_1 = pets_text.split("\n")
    pets_split_2 = pets_split_1[1].split(" ")

    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")
    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    assert int(pets_split_2[1]) == len(list_of_pets)  # Присутствуют все питомцы.

def test_half_of_my_pets_with_photo(driver):
    """Проверка, что у хотябы половины  питомцев есть фото.
        Т.е. количество питомцев с фото совпадает с округленной половиной количества питомцев"""
    driver.implicitly_wait(10)
    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # waiting photo of my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "th > img[src^='data:image']")
    # count number of photos
    list_photo = driver.find_elements(By.CSS_SELECTOR, "th > img[src^='data:image']")

    assert len(list_photo) >= len(list_of_pets) / 2  # Хотя бы у половины питомцев есть фото.

def test_my_pets_with_name(driver):
    """Проверка, что у все питомцев есть имя.
        Т.е. количество питомцев с именем совпадает с общим количеством"""
    driver.implicitly_wait(10)
    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of names
    list_names = []
    for i in range(len(list_of_pets)):
        # waiting names of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(2)")
        list_names.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i+1}) > td:nth-child(2)").text)
    nonempty_list_names = 0
    for item in list_names:
        if item:
            nonempty_list_names += 1

    assert nonempty_list_names == len(list_of_pets)  # У всех питомцев есть имя.

def test_my_pets_with_type(driver):
    """Проверка, что у все питомцев есть порода.
        Т.е. количество питомцев с породой совпадает с общим количеством"""
    driver.implicitly_wait(10)
    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of types
    list_types = []
    for i in range(len(list_of_pets)):
        # waiting types of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(3)")
        list_types.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(3)").text)
    nonempty_list_types = 0
    for item in list_types:
        if item:
            nonempty_list_types += 1
    assert nonempty_list_types == len(list_of_pets)  # У всех питомцев есть порода.

def test_my_pets_with_age(driver):
    """Проверка, что у все питомцев есть возраст.
        Т.е. количество питомцев с возрастом совпадает с общим количеством"""
    driver.implicitly_wait(10)
    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of ages
    list_ages = []
    for i in range(len(list_of_pets)):
        # waiting ages of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(4)")
        list_ages.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(4)").text)
    nonempty_list_ages = 0
    for item in list_ages:
        if item:
            nonempty_list_ages += 1

    assert nonempty_list_ages == len(list_of_pets)  # У всех питомцев есть возраст.

def test_my_pets_with_different_name(driver):
    """Проверка, что у все питомцев разные имена.
        Т.е. количество в массиве питомцев совпадает с количеством во множестве питомцев"""
    driver.implicitly_wait(10)
    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    list_names = []
    for i in range(len(list_of_pets)):
        # waiting names of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(2)")
        list_names.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i+1}) > td:nth-child(2)").text)

    assert len(list_names) == len(set(list_names)) # У всех питомцев разные имена

def test_my_pets_different(driver):
    """Проверка, что нет повторяющихся питомцев, у которых одинаковое имя, порода и возраст.
        Т.е. количество в массиве питомцев совпадает с количеством во множестве питомцев"""
    driver.implicitly_wait(10)
    # waiting table with my pets
    myDynamicElement = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    # count number of pets in table:
    list_of_pets = driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")

    list_names = []
    for i in range(len(list_of_pets)):
        # waiting names of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(2)")
        list_names.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i+1}) > td:nth-child(2)").text)

    list_types = []
    for i in range(len(list_of_pets)):
        # waiting types of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(3)")
        list_types.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(3)").text)

    list_ages = []
    for i in range(len(list_of_pets)):
        # waiting ages of my pets
        myDynamicElement = driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(4)")
        list_ages.append(driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) > td:nth-child(4)").text)

    # zip names, type and ages in one list
    list_zipped_pets = zip(list_names, list_types, list_ages)
    q = list(list_zipped_pets)
    assert len(q) == len(set(q)) # Нет повторяющихся питомцев
