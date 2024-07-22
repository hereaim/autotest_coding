from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calcMath(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет  поле
    get_value = browser.find_element(By.ID, 'input_value').text
    x = calcMath(get_value)
    browser.find_element(By.ID, 'answer').send_keys(x)

    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
    robot_check.click()
    robot_rule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()
    send_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    send_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()