import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            link = "https://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            # Ваш код, который заполняет обязательные поля
            textbox_name_list = browser.find_elements(By.CSS_SELECTOR, "input[required]")
            for textbox in textbox_name_list:
                textbox.send_keys("Тест")
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = WebDriverWait(browser,5).until(
                EC.presence_of_element_located(By.TAG_NAME, "h1"))
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()