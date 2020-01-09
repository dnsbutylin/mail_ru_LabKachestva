from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class AuthorizationMailRuPage(BasePage):

    def submit_btn(self):
        """Возвращает элемент кнопки подтверждения"""
        return self.element(By.CSS_SELECTOR, 'input.o-control')

    def username_inp(self):
        """Возвращает элемент поля для ввода имени пользователя"""
        return self.element(By.CSS_SELECTOR, '[id="mailbox:login"]')

    def password_inp(self):
        """Возвращает элемент поля для ввода пароля"""
        return self.element(By.CSS_SELECTOR, '[id="mailbox:password"]')

    def login(self, username, password):
        """Авторизуется с указанными логином/паролем"""
        self.typing(self.username_inp(), username)  # Вводим логин
        self.submit_btn().click()  # Нажимаем подтвердить
        self.wait_visibility_of_element_by_css('[id="mailbox:password"]')
        self.typing(self.password_inp(), password)  # Вводим пароль
        self.submit_btn().click()  # Нажимаем подтвердить
        self.wait_visibility_of_element_by_css('.settings .button2__txt')

    def page_is_loaded(self):
        """Проверяет видимость кнопки подтверждения"""
        assert self.submit_btn().is_displayed, "is not displayed"
