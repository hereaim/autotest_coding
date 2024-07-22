from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def calcMath(x,y):
    sum_xy = int(x+y)
    return sum_xy
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет  поле
    x = browser.find_element(By.ID, 'num1')
    print(x.text)
    y = browser.find_element(By.ID, 'num2')
    print(y.text)
    summa = calcMath(int(x.text), int(y.text))
    print(summa)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(f'{summa}')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()