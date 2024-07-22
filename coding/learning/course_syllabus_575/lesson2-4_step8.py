from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calcMath(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    browser.find_element(By.ID, 'book').click()
    # Ваш код, который заполняет  поле
    get_value = browser.find_element(By.ID, 'input_value').text
    x = calcMath(get_value)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.ID, 'solve').click()
    print(browser.switch_to.alert.text)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()