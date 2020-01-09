from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_visibility_of_element_by_css(self, locator):
        """Ожидание для проверки того, что элемент присутствует в DOM страницы и виден"""
        return self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def element(self, how, locator, listed=False):
        """Возврает элемент по заданным параметрам (listed=True указывать, если нужно получить список)"""
        e = self.wait.until(lambda e: self.driver.find_elements(how, locator))
        if listed:
            return e
        else:
            return e[0]

    @staticmethod
    def typing(elem, text):
        """Чистим текстовое поле до переедачи в него текста, посимвольно вводим текст, и проверяем что ввели"""
        elem.click()
        elem.send_keys(Keys.CONTROL + "a" + Keys.BACK_SPACE)
        for symbol in text:
            elem.send_keys(symbol)
