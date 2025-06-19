# from utils.helpers import checkbox_disabled
from utils.EncryptDecrypt import EncryptDecrypt


class LoginPage:
    def __init__(self, page):
        # self.page = page
        # self.username_input = page.locator("#username")
        # self.password_input = page.locator("#password")
        # self.login_button = page.locator("button[type='submit']")

        self.page = page
        self.username_input = page.locator('xpath=//*[@id="Username"]')
        self.password_input = page.locator('xpath=//*[@id="Password"]')
        self.login_button = page.locator('xpath=//*[@id="login"]/input[3]')
        self.login_button2 = page.locator('xpath=//*[@id="login"]/button')
        self.select_cloud = page.locator('xpath=//*[@id="SelectedPortal"]')
        self.login_button_1 = page.locator('xpath=//*[@id="loginbtn"]')
        self.txt_acct_locked = page.locator('xpath=//form[@id="login"]//div[1]')
        self.txt_login_error = page.locator('#login-error')

        # self.btnclick = checkbox_disabled

    def login(self, username, password):
        password = EncryptDecrypt.decrypted_text(password)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
