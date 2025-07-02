class CaregiverCaregiverChat:
    A_CAREGIVER = "xpath=//[text()='Caregiver']"
    A_CAREGIVER_CHAT = 'xpath=//*[@id="ulMenu"]/li/ul/li/a[contains(text(),"Caregiver Chat")]'
    CAREGIVER_SEARCH_BOX = 'xpath=//input[@aria-labelledby="messageSearchBtn"]'
    MYCHAT_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"MyChats")]'
    EVV_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"EVV")]'
    GENERAL_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"General")]'
    MOBILE_APP_ISSUE_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"Mobile App Issue")]'
    PATIENT_ISSUE_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"Patient Issue")]'
    SCHEDULING_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"Scheduling")]'
    TIMESHEET_MENU = 'xpath=//*[@id="memberTabs"]/li/a/span[contains(text(),"Timesheet")]'

    MYCHAT_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"MyChats")]'
    EVV_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"EVV")]'
    GENERAL_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"General")]'
    MOBILE_APP_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"Mobile App Issue")]'
    PATIENT_ISSUE_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"Patient Issue")]'
    SCHEDULING_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"Scheduling")]'
    TIMESHEET_LABEL = 'xpath=//*[@id="private"]//h2[contains(text(),"Timesheet")]'

    I_ICON = 'xpath=//*[@id="viewToggle"]/medium/em'
    CAREGIVER_STATUS = 'xpath=//*[@id="ctl00_ContentPlaceHolder1_uxLblAideStatus"]'

    # MyChat Section
    MYCHAT_LABEL_INSIDE = 'xpath=//h2[contains(text(), "MyChats")]'
    UNREAD_CHAT_ICON = 'xpath=//*[@id="unreadToggle"]'
    ONLINE_CAREGIVER_ICON = 'xpath=//*[@id="onlineToggle"]'
    NEW_CHAT_BUTTON = 'xpath=//a[contains(text(),"New Chat")]'
    SELECT_LIST = 'xpath=//*[@class="selected-list"]'
    SEARCH_TYPE_TEXTBOX = 'xpath=//*[@aria-labelledby="searchIcon"]'
    SELECT_CAREGIVER_FROM_LIST = 'xpath=//*[contains(text(),"test test (MAN-2302)")]'
    TYPE_NEW_MESSAGE = 'xpath=//*[@placeholder="Type a new message"]'
    SEND_BUTTON = 'xpath=(//div[@class="input-group-button"])[2]'
    MESSAGE_SENT_AREA = 'xpath=//*[@id="messagelist"]//*[@class="chat"]'
    MESSAGE_TEXT_RETURN = 'xpath=//*[@id="msgTabs"]/li[2]/a/span[3]'

    # EVV Menu
    EVV_LABEL_INSIDE = 'xpath=//h2[contains(text(), "EVV")]'
    GENERAL_LABEL_INSIDE = 'xpath=//h2[contains(text(), "General")]'
    MOBILE_APP_ISSUE_LABEL = 'xpath=//h2[contains(text(), "Mobile App Issue")]'
