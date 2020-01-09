from selenium import webdriver
import unittest
from page_object.mail_ru.authorization_page import AuthorizationMailRuPage
from page_object.email_ru.email_page import EmailPage
from page_object.email_ru.writing_page import WritingPage
from page_object.email_ru.pop_ups import PopUp
from selenium.webdriver import ActionChains


class SendEmailPositive(unittest.TestCase):

    USERNAME = 'testaccount.2000'
    PASSWORD = 'qwe321!qwe'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://mail.ru/')  # Перехаодим на нужный урл
        auth = AuthorizationMailRuPage(cls.driver)
        auth.page_is_loaded()  # Проверка загрузки страницы
        auth.login(cls.USERNAME, cls.PASSWORD)  # Авторизуемся

    def test_01_send_email_positive(self):
        """Отправляет письмо другому пользователю"""
        email = EmailPage(self.driver)
        email.page_is_loaded()  # Проверка загрузки страницы
        email.send_email_btn().click()  # Нажимаем кнопку написать письмо
        writing = WritingPage(self.driver)
        writing.page_is_loaded()  # Проверка загрузки страницы
        writing.typing(writing.whom_inp(), 'dnsbutylin@gmail.com')  # Указываем кому отправляем
        writing.typing(writing.topic_inp(), 'Test')  # Пишем тему письма
        # Вводим данные в тело письма
        ActionChains(self.driver).click(writing.first_string_of_text()).send_keys(
            '11111111111111111111111111111111111111111').perform()
        writing.send_btn().click()  # Нажимаем отправить
        pop_up = PopUp(self.driver)
        # Проверяем, что появилось сообщение об отправке
        assert pop_up.status_after_send_email().is_displayed, "is not displayed"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
