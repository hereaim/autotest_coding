from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 5
def selector():
    example_field = By.XPATH, "//a[contains(text(), '1624316244162')]"
    result_field = By.ID, 'result'
    return example_field, result_field
def send_click():
    try:
        example_field, result_field = selector()
        print("\nstart browser for test..")
        driver = webdriver.Chrome()
        link = 'https://parsinger.ru/selenium/2/2.html'
        driver.get(link)
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(example_field)).click()
        result = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(result_field)).text
        print(result)
    finally:
        print("\nquit browser..")
        driver.quit()
send_click()

