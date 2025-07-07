# from utils.helpers import checkbox_disabled

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from locators.LoginLocators import LoginLocators
from utils.EncryptDecrypt import EncryptDecrypt
from utils.logger import log_message


class LoginPage:
    """
    Page object for the Login page. Encapsulates all login actions and elements.
    """
    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str, timeout: int = 10000) -> None:
        """
        Perform login with the given username and password.
        Raises an exception if login fails.
        """
        try:
            decrypted_password = EncryptDecrypt.decrypted_text(password)
            log_message(f"Attempting login for user: {username}")
            self.page.locator(LoginLocators.USERNAME).fill(username, timeout=timeout)
            self.page.locator(LoginLocators.PASSWORD).fill(decrypted_password, timeout=timeout)
            self.page.locator(LoginLocators.LOGIN_BUTTON).click(timeout=timeout)
            # Optionally, wait for a post-login element to appear
            # self.page.wait_for_selector('selector-for-dashboard', timeout=timeout)
            log_message(f"Login successful for user: {username}")
        except PlaywrightTimeoutError as e:
            log_message(f"Login failed for user {username}: Timeout - {e}")
            raise
        except Exception as e:
            log_message(f"Login failed for user {username}: {e}")
            raise

        # self.username_input.fill(username)
        # self.password_input.fill(password)
        # self.login_button.click()
