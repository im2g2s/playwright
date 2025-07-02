from conftest import page


class LoginLocators:
    USERNAME = 'xpath=//*[@id="Username"]'
    PASSWORD = 'xpath=//*[@id="Password"]'
    LOGIN_BUTTON = 'xpath=//*[@id="login"]/input[3]'
    LOGIN_BUTTON2 = 'xpath=//*[@id="login"]/button'
    SELECT_CLOUD = 'xpath=//*[@id="SelectedPortal"]'
    LOGIN_BUTTON_1 = 'xpath=//*[@id="loginbtn"]'
    TXT_ACCT_LOCKED = 'xpath=//form[@id="login"]//div[1]'
    TXT_LOGIN_ERROR = '#login-error'  # CSS selector
