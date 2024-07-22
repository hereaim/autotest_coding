from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 5
def selector():
    text_field = By.XPATH, "//div[@class='text']//p[2]"
    result_field = By.ID, 'result'
    return text_field, result_field
def send_click():
    try:
        text_field, result_field = selector()
        result = 0
        print("\nstart browser for test..")
        driver = webdriver.Chrome()
        link = 'https://parsinger.ru/selenium/3/3.html'
        driver.get(link)
        get_all_p = WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(text_field))
        for element in get_all_p:
            result += int(element.text)
        print(result)
    finally:
        print("\nquit browser..")
        driver.quit()


send_click()

