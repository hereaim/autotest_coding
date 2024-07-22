from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 5
def selector():
    check_field = By.CSS_SELECTOR, '.check[type="checkbox"]'
    result_button = By.CSS_SELECTOR, 'input[value="Отправить"]'
    result_field = By.ID, 'result'
    return check_field, result_button, result_field

def send_click():
    try:
        check_field, result_button, result_field = selector()
        print("\nstart browser for test..")
        driver = webdriver.Chrome()
        link = 'https://parsinger.ru/selenium/4/4.html'
        driver.get(link)
        get_all_check = WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(check_field))
        for element in get_all_check:
            element.click()
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(result_button)).click()
        result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(result_field))
        print(result.text)
    finally:
        print("\nquit browser..")
        driver.quit()


send_click()

