import time

from selenium import webdriver
from selenium.webdriver.common.by import By

sleeping_time = 2
"""Инициализация драйвера и запуск сайта"""
driver_Chrome = webdriver.Chrome()
driver_Chrome.get("https://the-internet.herokuapp.com/status_codes")
time.sleep(sleeping_time)

"""Получение всех ссылок из таблицы ul"""
def get_element_xpath_href():
    xpath = driver_Chrome.find_elements("xpath", "//*[@id='content']/div/ul/li/a")
    list_href = []
    for i in xpath:
        get_href = i.get_attribute('href')
        list_href.append(get_href)
    return list_href

"""Функция переходов по ссылкам, полученным в get_element_xpath_href"""
def forward_list():
    list_href = get_element_xpath_href()
    for i in list_href:
        print(f"Осуществляется переход по ссылке {i}")
        driver_Chrome.get(i)
        time.sleep(sleeping_time)
        assert driver_Chrome.current_url == i
        print(f"Вы находитесь на странице {driver_Chrome.current_url}")
        time.sleep(sleeping_time)
        print(f"Осуществляется переход назад")
        driver_Chrome.back()
        time.sleep(sleeping_time)
        assert driver_Chrome.current_url == 'https://the-internet.herokuapp.com/status_codes'
        print("Ссылка является главной\n")
        time.sleep(sleeping_time)
    print("Конец переходов по ссылкам")

forward_list()#Вызов функции forward_list
