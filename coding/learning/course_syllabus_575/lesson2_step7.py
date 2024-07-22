from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calcMath(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет  поле
    get_atr_img = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    x = calcMath(get_atr_img)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()