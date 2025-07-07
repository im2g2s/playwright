import pytest
from utils.logger import log_message
from pages.login_page import LoginPage
from utils.TestRail import update_testrail
from Profiles.ENTProfile import ENTProfile

testcaseid = '3931395'

@pytest.mark.parametrize(
    "username,password",
    [
        (ENTProfile.USERNAME62, ENTProfile.PASSWORD),
        # Add more tuples here for additional test data sets
        # ("another_user", "another_password"),
    ]
)
def test_C3931395(page, request, username, password):
    """
    Test valid login using ENTProfile credentials and robust Playwright fixtures.
    Parameterized for multiple sets of credentials.
    """
    test_name = request.node.name
    log_message(f"Starting test: {test_name} with username: {username}")
    try:
        page.goto(ENTProfile.BASE_URL)
        log_message(f"Navigated to {ENTProfile.BASE_URL}")
        login_page = LoginPage(page)
        login_page.login(username, password)
        # Optionally, wait for a post-login element to confirm success
        # page.wait_for_selector('selector-for-dashboard', timeout=10000)
        log_message(f"{test_name} login successful.")
        update_testrail(testcaseid, 'PASS')
    except Exception as e:
        log_message(f"{test_name} failed: {e}")
        update_testrail(testcaseid, 'FAIL', comment=str(e))
        raise
