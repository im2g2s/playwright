from locators.LoginLocators import LoginLocators
from locators.Function_caregiver_chat import CaregiverCaregiverChat
from playwright.sync_api import Page

def perform_login(page: Page, username: str, password: str):
    page.goto("https://example.com/login")
    page.fill(LoginLocators.USERNAME, username)
    page.fill(LoginLocators.PASSWORD, password)
    page.click(LoginLocators.LOGIN_BUTTON)

def Page_Cargiver_Chat(page:Page):
    page.click(CaregiverCaregiverChat.A_CAREGIVER)
    page.click(CaregiverCaregiverChat.A_CAREGIVER_CHAT)
    page.wait_for_selector(CaregiverCaregiverChat.CAREGIVER_SEARCH_BOX)
