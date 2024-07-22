from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 5
def selector():
    input_field = By.CSS_SELECTOR, 'input[type="text"]'
    sumbit_button = By.CSS_SELECTOR, 'input[value="Отправить"]'
    result_field = By.ID, 'result'
    return input_field, sumbit_button, result_field
def send_click():
    try:
        input_field,  sumbit_button, result_field = selector()
        # input_field = By.CSS_SELECTOR, 'input[type="text"]'
        # sumbit_button = By.CSS_SELECTOR, 'input[value="Отправить"]'
        # result_field = By.ID, 'result'
        print("\nstart browser for test..")
        driver = webdriver.Chrome()
        link = 'https://parsinger.ru/selenium/1/1.html'
        driver.get(link)
        everyone_input = WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(input_field))
        for element in everyone_input:
            element.send_keys('Текст')
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(sumbit_button)).click()
        result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(result_field)).text
        print(result)
    finally:
        print("\nquit browser..")
        driver.quit()
send_click()

