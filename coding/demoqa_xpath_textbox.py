import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""Мини-конфиг"""
full_name = "Alex"
email = "alex@email.com"
current_address = "City Moscow, street Lenina, house 2"
perm_address = "City st.Petersburg, street Lomonosova, 45/1"
sleeping_time = 3

"""Инициализация драйвера и запуск сайта"""
driver_Chrome = webdriver.Chrome()
driver_Chrome.get("https://demoqa.com/text-box")
time.sleep(sleeping_time)

"""Получение xpath Локаторов"""
def get_xpath_locator():
    get_full_name = driver_Chrome.find_element('xpath', "//*[@id='userName']")
    get_email = driver_Chrome.find_element('xpath', "//*[@id='userEmail']")
    get_current_address = driver_Chrome.find_element('xpath', "//*[@id='currentAddress']")
    get_perm_address = driver_Chrome.find_element('xpath', "//*[@id='permanentAddress']")
    return get_full_name, get_email, get_current_address, get_perm_address

"""Проверка что локаторы пустые"""
def check_empty_locator(locators):
    for locator in locators:
        assert locator.get_attribute('value') == ""
        print(f"Поле {locator.get_attribute('id')} пустое")



"""Проверка значения локаторов"""
def check_value_locator(locators):
    for locator in locators:
        if locator.get_attribute('value') == '':
            print(f"Значение в поле {locator.get_attribute('id')} пустое")
        else:
            print(f"Значение в поле {locator.get_attribute('id')} равно: \n {locator.get_attribute('value')}")

"""Очистка всех локаторов"""
def clear_all_locator(locators):
    for locator in locators:
        if locator.get_attribute('value') == '':
            print(f"Поле {locator.get_attribute('id')} и так пустое")
        else:
            locator.clear()
            print(f"Поле {locator.get_attribute('id')} очищено")

"""Ввод значения в поля"""
def input_locators():
    get_full_name, get_email, get_current_address, get_perm_address = get_xpath_locator()
    get_full_name.send_keys(full_name)
    get_email.send_keys(email)
    get_current_address.send_keys(current_address)
    get_perm_address.send_keys(perm_address)

locators = get_xpath_locator()  #Получение списка всех локаторов
check_empty_locator(locators) # Проверка что локаторы пустые
time.sleep(sleeping_time) # 3 секунды остановки

input_locators()  # Заполнение полей
time.sleep(sleeping_time) # 3 секунды остановки

check_value_locator(locators)  # Проверка значения в полях
time.sleep(sleeping_time) # 3 секунды остановки

clear_all_locator(locators) #Очистка значений из полей
time.sleep(sleeping_time) # 3 секунды остановки

check_empty_locator(locators) # Проверка что локаторы пустые
time.sleep(sleeping_time) # 3 секунды остановки

