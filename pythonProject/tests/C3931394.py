from selenium.webdriver.common.by import By

from function.Function_caregiver_chat import Page_Cargiver_Chat
from locators.HomePage import HomePage
from utils.logger import log_message
from pages.login_page import LoginPage
from utils.TestRail import update_testrail
from utils.helpers import take_screenshot, log_message
from Profiles.ENTProfile import ENTProfile

testcaseid = '3931424'


def get_int_count(text):
    number = '0123456789'
    for i in text:
        if i not in number:
            text = text.replace(i, "")
    return int(text)


def test_C3931424(page, request):
    test_name = request.node.name  # Gets 'test_valid_login'
    # profile = load_profile()
    try:
        page.goto(ENTProfile.BASE_URL)
        Obj_Login_Page = LoginPage(page)
        Obj_Login_Page.login(ENTProfile.USERNAME11, ENTProfile.PASSWORD)

        # page.click(HomePage.A_PATIENT)
        page.click(HomePage.A_SEARCH_PATIENT)
        page.click(HomePage.BUTTON_SEARCH)

        page.wait_for_timeout(5000)
        search_result = "xpath =//h2[contains(text(),'Search Result')]"

        count = get_int_count(page.text_content(search_result))
        assert count > 0

    except Exception as e:
        take_screenshot(page, f"screenshots/FAIL_{test_name}.png")
        log_message(f"{test_name} failed: {e}")
        update_testrail(testcaseid, 'FAIL', comment=str(e))
    else:
        take_screenshot(page, f"screenshots/PASS_{test_name}.png")
        update_testrail(testcaseid, 'PASS')
