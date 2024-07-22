from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calcMath(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет  поле
    get_value = browser.find_element(By.ID, 'input_value').text
    x = calcMath(get_value)
    browser.find_element(By.ID, 'answer').send_keys(x)

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()