import time
from pages.login_page import LoginPage
from utils.TestRail import update_testrail
from utils.config import BASE_URL, USERNAME, PASSWORD
from utils.helpers import take_screenshot, log_message
from Profiles.ENTProfile import ENTProfile

testcaseid = '3931395'


def test_3931395(page, request):
    test_name = request.node.name  # Gets 'test_valid_login'
    try:

        page.goto(ENTProfile.BASE_URL)
        LoginPage.login(self.driver,ENTProfile.USERNAME116,ENTProfile.PASSWORD)
        login_page = LoginPage(page)
        login_page.login(USERNAME, PASSWORD)
        time.sleep(5)
        assert page.locator("div.flash.success").is_visible()
        # take_screenshot(page, f"screenshots/{test_name}_success.png")
        log_message(f"{test_name} passed successfully.")
    except Exception as e:
        take_screenshot(page, f"screenshots/FAIL_{test_name}.png")
        log_message(f"{test_name} failed: {e}")
        update_testrail(testcaseid, 'FAIL', comment=str(e))
        assert False
    else:
        take_screenshot(page, f"screenshots/PASS_{test_name}.png")
        update_testrail(testcaseid, 'PASS')
