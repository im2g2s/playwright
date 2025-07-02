# from utils.helpers import checkbox_disabled

from playwright.sync_api import Page
from locators.LoginLocators import LoginLocators

from utils.EncryptDecrypt import EncryptDecrypt


class LoginPage:
    def __init__(self, page:Page):
        self.page = page

    def login(self, username, password):
        password = EncryptDecrypt.decrypted_text(password)
        self.page.locator(LoginLocators.USERNAME).fill(username)
        self.page.locator(LoginLocators.PASSWORD).fill(password)
        self.page.locator(LoginLocators.LOGIN_BUTTON).click()

        # self.username_input.fill(username)
        # self.password_input.fill(password)
        # self.login_button.click()
