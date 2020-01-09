from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class PopUp(BasePage):

    def status_after_send_email(self):
        """Возвращает элемент сообщения содержащий статус его отправки"""
        return self.element(By.CSS_SELECTOR, '.layer__header span')
