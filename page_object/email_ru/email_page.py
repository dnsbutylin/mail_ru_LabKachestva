from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class EmailPage(BasePage):

    def send_email_btn(self):
        """Возвращает элемент кнопки написать письмо"""
        return self.element(By.CSS_SELECTOR, '.compose-button__wrapper')

    def settings_btn(self):
        """Возвращает элемент кнопки настройки"""
        return self.element(By.CSS_SELECTOR, '.settings .button2__txt')

    def page_is_loaded(self):
        """Проверяет видимость кнопки подтверждения"""
        assert self.send_email_btn().is_displayed, "is not displayed"
        assert self.settings_btn().is_displayed, "is not displayed"

