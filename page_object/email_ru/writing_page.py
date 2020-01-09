from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class WritingPage(BasePage):

    def whom_inp(self):
        """Возвращает элемент поля: "Кому" """
        return self.element(By.CSS_SELECTOR, '.container--zU301 .container--H9L5q.size_s--3_M-_')

    def topic_inp(self):
        """Возвращает элемент поля: "Тема" """
        return self.element(By.CSS_SELECTOR, '.container--3QXHv .container--H9L5q.size_s--3_M-_')

    def first_string_of_text(self):
        """Возвращает элемент первой строки текста письма"""
        return self.element(By.CSS_SELECTOR, '.cke_editable > div > div:nth-child(1)')

    def send_btn(self):
        """Возвращает элемент кнопки "Отправить" """
        return self.element(By.CSS_SELECTOR, '.compose-app__buttons .button2_primary')

    def page_is_loaded(self):
        """Проверяет видимость кнопки подтверждения"""
        assert self.whom_inp().is_displayed, "is not displayed"
        assert self.topic_inp().is_displayed, "is not displayed"
        assert self.send_btn().is_displayed, "is not displayed"
