from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calcMath(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Ваш код, который заполняет  поле
    get_value = browser.find_element(By.ID, 'input_value').text
    x = calcMath(get_value)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print(browser.switch_to.alert.text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()