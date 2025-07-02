from function.Function_caregiver_chat import Page_Cargiver_Chat
from locators.Function_caregiver_chat import CaregiverCaregiverChat
from utils.logger import log_message
from pages.login_page import LoginPage
from utils.TestRail import update_testrail
from utils.helpers import take_screenshot, log_message
from Profiles.ENTProfile import ENTProfile

testcaseid = '3931424'


def test_C3931424(page, request):
    test_name = request.node.name  # Gets 'test_valid_login'
    # profile = load_profile()
    try:
        page.goto(ENTProfile.BASE_URL)
        Obj_Login_Page = LoginPage(page)
        Obj_Login_Page.login(ENTProfile.USERNAME11,ENTProfile.PASSWORD)
        Page_Cargiver_Chat(page)
        page.click(CaregiverCaregiverChat.MYCHAT_MENU)
        page.wait_for_selector(CaregiverCaregiverChat.MYCHAT_LABEL)
        page.click(CaregiverCaregiverChat.EVV_MENU)
        page.wait_for_selector(CaregiverCaregiverChat.EVV_LABEL)
        page.click(CaregiverCaregiverChat.GENERAL_MENU)
        page.wait_for_selector(CaregiverCaregiverChat.GENERAL_LABEL)
        page.click(CaregiverCaregiverChat.MOBILE_APP_ISSUE_MENU)
        page.click(CaregiverCaregiverChat.MOBILE_APP_LABEL)
        page.click(CaregiverCaregiverChat.PATIENT_ISSUE_MENU)
        page.wait_for_selector(CaregiverCaregiverChat.PATIENT_ISSUE_LABEL)

        page.click(CaregiverCaregiverChat.SCHEDULING_MENU)
        page.wait_for_selector(CaregiverCaregiverChat.SCHEDULING_LABEL)

        page.click(CaregiverCaregiverChat.TIMESHEET_MENU)
        page.wait_for_selector(CaregiverCaregiverChat.TIMESHEET_LABEL)


    except Exception as e:
        take_screenshot(page, f"screenshots/FAIL_{test_name}.png")
        log_message(f"{test_name} failed: {e}")
        update_testrail(testcaseid, 'FAIL', comment=str(e))
    else:
        take_screenshot(page, f"screenshots/PASS_{test_name}.png")
        update_testrail(testcaseid, 'PASS')
