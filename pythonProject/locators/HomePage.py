from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class HomePage:
    A_DATA_INSIGHTS = (By.XPATH, '(//a[normalize-space() = "Data Insights"])[2]')
    Eligibility_Batch_Review = (By.LINK_TEXT, 'Eligibility Batch Review')
    IFRAME_MSG_BATCH = 'ctl00_ContentPlaceHolder1_divEligibilityBatchReview'
    Eligibility_Batch_Review_Search = (By.XPATH, '//input[@id="ctl00_ContentPlaceHolder1_btnSearch"]')
    Monitor_Process = 'HHAeXchange - Process Monitor'

    A_EVV_Aggregator = (By.XPATH, '(//a[normalize-space() = "EVV Aggregation Transaction Manager"])[2]')
    A_CUSTOM_EXPORT = (By.XPATH, '(//a[contains(text(), "Custom Export")])[2]')
    A_SYSTEM_NOTIFICATIONS = (By.XPATH, '//*[@id="sysNoti-label"]')
    A_SELECT_PRIORITY = (By.XPATH, "//select[@id='ddlPrioritySent']/option[2]")
    A_PRIORITY_DROPDOWN = (By.XPATH, '//select[@id="ddlPrioritySent"]')
    A_SYSTEM_NOTIFICATION_TEXT = (By.XPATH, '//h2[text()="Search System Notifications"]')
    A_NEW_PAYROLL = (By.LINK_TEXT, 'New Payroll')
    A_PAYROLL = (By.LINK_TEXT, 'Payroll')
    A_SEARCH_BY_BATCH = (By.LINK_TEXT, 'Search By Batch')
    DIV_SPINNER = (By.XPATH, '//div[@id="load-spinner-main"]')
    A_Compliance_Setup = (By.LINK_TEXT, 'Compliance Setup')
    A_Item_Manager = (By.XPATH, '(//a[normalize-space() = "Item Manager"])[2]')
    A_Search_Setup = (By.LINK_TEXT, 'Search Setups')
    HOME = (By.LINK_TEXT, 'Home')
    A_ADMIN = (By.LINK_TEXT, 'Admin')
    A_MANAGE_REPORT = (By.LINK_TEXT, 'Manage Report Subscription')
    A_FAMILY_PORTAL_GLOBAL_MGNT = (By.XPATH, "//*[@id='ulMenu']//a[contains(text(),'Family Portal Global Management')]")
    A_REGISTERED_FAMILY_MEMBER = (By.XPATH, "//*[@id='ulMenu']//a[contains(text(),'Registered Family Members')]")
    A_CONTRACT_SETUP = (By.LINK_TEXT, 'Contract Setup')
    A_NEW_CONTRACT = (By.LINK_TEXT, 'New Contract')
    A_SEARCH_CONTRACT = (By.LINK_TEXT, 'Search Contract')
    A_OFFICE_SETUP = (By.LINK_TEXT, 'Office Setup')
    A_NEW_OFFICE = (By.LINK_TEXT, 'New Office')
    A_SEARCH_OFFICE = (By.LINK_TEXT, 'Search Office')
    A_PATIENT = 'a:has-text("Patient")'
    A_PROVIDER_AND_CAREGIVER = (By.LINK_TEXT, 'Provider and Caregiver')
    A_HOME = (By.XPATH, '//*[@id="ulMenu"]//a[text()="Home"]')
    A_NEW_PATIENT = (By.LINK_TEXT, 'New Patient')
    A_SEARCH_PATIENT = 'a:has-text("Search Patient")'
    A_CAREGIVER = (By.LINK_TEXT, 'Caregiver')
    A_TRAINEE = (By.LINK_TEXT, 'Trainee')
    A_NEW_TRAINEE = (By.LINK_TEXT, 'New Trainee')
    A_SEARCH_TRAINEE = (By.LINK_TEXT, 'Search Trainee')
    A_NEW_CAREGIVER = (By.LINK_TEXT, 'New Caregiver')
    A_SEARCH_CAREGIVER = (By.LINK_TEXT, 'Search Caregiver')
    A_New_SEARCH_CAREGIVER = (By.LINK_TEXT, ' Search Caregiver ')
    A_New_SEARCH_CAREGIVER_Under_Search = (By.XPATH, "//a[text()=' Search Caregiver']//parent::li[@role='none']")
    A_ORG_STRUCTURE = (By.LINK_TEXT, 'Org. Structure')
    A_ORDER_TRACKING = (By.LINK_TEXT, 'Order Tracking')
    A_BILLING = (By.LINK_TEXT, 'Billing')
    A_BILLING_REVIEW = (By.LINK_TEXT, 'Billing Review')
    A_NEW_INVOICE_INTERNAL = (By.LINK_TEXT, 'New Invoice - (Internal)')
    A_NEW_INVOICE_BATCH = (By.LINK_TEXT, 'New Invoice Batch')
    A_PROCESS_MONITOR = (By.LINK_TEXT, 'Process Monitor')
    A_CASH_PAYMENT = (By.LINK_TEXT, 'Cash Payment')
    A_SUPPORT_MENU = (By.XPATH, '//*[@id="ulMenu"]/li[12]/a')
    A_SUPPORT_MENU_PAYER = (By.XPATH, '//*[@class="user"]')
    A_LOGOUT = (By.LINK_TEXT, 'Logout')
    A_PAYER_PROFILE_MENU = (By.XPATH, '//*[@id="app-container"]//hhax-navigation//div//button')
    A_INVOICE_SEARCH = (By.LINK_TEXT, 'Invoice Search')
    A_BY_BATCH = (By.LINK_TEXT, 'By Batch')
    A_BY_VISIT = (By.LINK_TEXT, 'By Visit')
    A_BY_INVOICE = (By.LINK_TEXT, 'By Invoice')
    A_ELECTRONIC_BILLING = (By.LINK_TEXT, 'Electronic Billing')
    A_E_SUBMISSION_BATCHES = (By.LINK_TEXT, 'E-Submission Batches')
    A_ACTION = (By.XPATH, '(//a[normalize-space() = "Action"])[2]')
    A_ACTION1 = (By.XPATH, '//*[@id="ulMenu"]/li[5]/a')
    A_OPERATION_WORKLIST = (By.LINK_TEXT, 'Operation Worklist')
    A_IN_SERVICE = (By.LINK_TEXT, 'In Service')
    A_NEW = (By.LINK_TEXT, 'New')
    A_SEARCH = (By.LINK_TEXT, 'Search')
    A_OVERTIME_DASHBOARD = (By.LINK_TEXT, 'Overtime Dashboard')
    A_SEARCH_CAREGIVER_NEW = (By.LINK_TEXT, 'Search Caregiver (New)')
    A_SEARCH_CAREGIVER_NEW_Under_SEARCH = "(//a[text()=' Search Caregiver'])[2]"
    A_GENERAL_CAREGIVER_AVAILABILITY = (By.LINK_TEXT, 'General Caregiver Availability')
    A_SEARCH_CAREGIVER_COMMUNICATION = (By.XPATH, "(//a[normalize-space()='Search Caregiver'])[4]")
    A_FILL_A_SHIFT = (By.LINK_TEXT, 'Fill a Shift')
    A_TRAVEL_TIME = (By.LINK_TEXT, 'Travel Time')
    A_REFERENCE_TABLE_MANAGEMENT = (By.LINK_TEXT, 'Reference Table Management')
    A_VISIT = (By.LINK_TEXT, 'Visit')
    A_QUICK_VISIT_ENTRY = (By.LINK_TEXT, 'Quick Visit Entry')
    A_APPOINTMENT = (By.LINK_TEXT, 'Appointments')
    A_PAYROLLL_SETUP = (By.LINK_TEXT, 'Payroll Setup')
    A_PREBILLING = (By.LINK_TEXT, 'Prebilling')
    A_VISIT_SEARCH = (By.LINK_TEXT, 'Visit Search')
    A_REFERRAL_PATIENT_MANAGEMENT = (By.LINK_TEXT, 'Referral Patient Management')
    A_SALES_STAFF = (By.LINK_TEXT, 'Sales Staff')
    A_ATTRIBUTE_SETUP = (By.LINK_TEXT, 'Attributes Setup')
    A_NEW_SALES_STAFF = (By.LINK_TEXT, 'New Sales Staff')
    A_SEARCH_SALES_STAFF = (By.LINK_TEXT, 'Search Sales Staff')
    A_SEARCH_REFERRAL_PATIENT = (By.XPATH, '//*[@id="ulMenu"]//a[contains(text()," Search Referral Patient")]')
    A_REFERRAL_PATIENT_SOURCE = (By.LINK_TEXT, 'Referral Patient Sources')
    A_NEW_REFERRAL_PATIENT_SOURCE = (By.LINK_TEXT, 'New Referral Patient Source')
    A_SEARCH_REFERRAL_PATIENT_SOURCE = (By.LINK_TEXT, 'Search Referral Patient Source')
    A_REFERRAL_PATIENT_ELIGIBILITY_CHECK = (By.LINK_TEXT, 'Referral Patient Eligibility Check')
    A_EDIT_SERVICE = (By.LINK_TEXT, 'Edit Services')
    A_PLACEMENT = (By.XPATH, '//a[@id="placement-label"]')
    A_PENDING_PLACEMENT_TAB = (By.XPATH, "//a[@id='pending-label']")
    A_PENDING_PLACEMENT_QUEUE = (By.LINK_TEXT, 'Pending Placement Queue (Agency)')
    A_STAFFED = (By.XPATH, "//a[contains(text(),'Staffed')]")
    A_STAFFED_PAGINATION = (By.XPATH,
                            "//div[@id='tbVendorPendingStaffed_paginate']//ul[contains(@class,'pagination')]/li[not(contains(@class,'previous')) and not(contains(@class,'next'))]")
    A_STAFFED_CURRENT_PAGE = (
    By.XPATH, "//div[@id='tbVendorPendingStaffed_paginate']//li[@class='paginate_button current']")
    A_STAFFED_BTN_PAGE_NEXT = (By.ID, "tbVendorPendingStaffed_next")
    A_STAFFED_BTN_PAGE_PREV = (By.ID, "tbVendorPendingStaffed_previous")
    A_ACCEPTED_WITH_TEMP_CAREGIVER = (By.XPATH, "//a[contains(text(),'Accepted with Temp Caregiver')]")
    ACCEPTED_WITH_TEMP_CG_PAGINATION = (By.XPATH,
                                        "//div[@id='tbVendorPendingStaffedCaregiverObj_paginate']//ul[contains(@class,'pagination')]/li[not(contains(@class,'previous')) and not(contains(@class,'next'))]")
    PENDING_PLACEMENT_PAGINATION = (By.XPATH,
                                    "//div[@id='tbVendorPendingPlacement_paginate']//ul[contains(@class,'pagination')]/li[not(contains(@class,'previous')) and not(contains(@class,'next'))]")
    PENDING_PLACEMENT_CURRENT_PAGE = (
    By.XPATH, "//div[@id='tbVendorPendingPlacement_paginate']//li[@class='paginate_button current']")
    PENDING_PLACEMENT_BTN_PAGE_NEXT = (By.ID, "tbVendorPendingPlacement_next")
    PENDING_PLACEMENT_BTN_PAGE_PREV = (By.ID, "tbVendorPendingPlacement_previous")
    ADMISSION_ID_HEADER = (By.XPATH, "//table[@id='tbVendorPendingPlacement']//th[contains(text(),'Admission ID')]")
    ADMISSION_ID_COLUMN = (By.XPATH, "//table[@id='tbVendorPendingPlacement']//tbody/tr/td[2]/a")
    ACCEPTED_TEMP_CG_BTN_PAGE_NEXT = (By.ID, "tbVendorPendingStaffedCaregiverObj_next")
    ACCEPTED_TEMP_CG_BTN_PAGE_PREV = (By.ID, "tbVendorPendingStaffedCaregiverObj_previous")
    ACCEPTED_TEMP_CG_CURRENT_PAGE = (
    By.XPATH, "//div[@id='tbVendorPendingStaffedCaregiverObj_paginate']//li[@class='paginate_button current']")
    A_ACCEPTED_WITH_NO_MASTERWEEK = (By.XPATH, "//a[contains(text(),'Accepted with No Master Week')]")
    NEXT_BTN_ACCEPTED_NO_MASTERWEEK = (By.ID, "tbVendorPendingAcceptedNoMasterweek_next")
    PREV_BTN_ACCEPTED_NO_MASTERWEEK = (By.ID, "tbVendorPendingAcceptedNoMasterweek_previous")
    ACCEPTED_NO_MASTERWEEK_CURRENT_PAGE = (
    By.XPATH, "//div[@id='tbVendorPendingAcceptedNoMasterweek_paginate']//li[@class='paginate_button current']")
    ACCEPTED_NO_MASTERWEEK_PAGINATION = (By.XPATH,
                                         "//div[@id='tbVendorPendingAcceptedNoMasterweek_paginate']//ul[contains(@class,'pagination')]/li[not(contains(@class,'previous')) and not(contains(@class,'next'))]")
    BTN_CLOSE_BENEFICIARY_INFO_POPUP = (By.ID, 'uxbtnClose')
    A_CONFIRM_VISIT = (By.LINK_TEXT, 'Confirm Visits')
    A_COLLECTION = (By.LINK_TEXT, 'Collection')
    A_PTO_APPROVAL = (By.LINK_TEXT, 'PTO Approval')
    A_BROADCAST_DASHBOARD = (By.XPATH, '(//a[normalize-space() = "Broadcast Dashboard"])[2]')
    A_CONTRACT_COMMUNICATION = (By.LINK_TEXT, 'Contract Communications')
    A_CARE_INSIDES_ALERT_DASHBOARD = (
    By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="Care Insights Alert Dashboard"]')
    A_CONFIRM_TIMESHEET = (By.LINK_TEXT, 'Confirm Timesheet')
    A_CAREGIVER_AWAKE_CONFIRMATION_DASHBOARD = (
    By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="Caregiver Awake Confirmation Dashboard"]')
    A_PHYSICIAN_SETUP = (By.LINK_TEXT, 'Physician Setup')
    A_NEW_PHYSICIAN = (By.LINK_TEXT, 'New Physician')
    A_SEARCH_PHYSICIAN = (By.LINK_TEXT, 'Physician Search')
    A_TRAINING_SCHOOL_SETUP = (By.LINK_TEXT, 'Training School Setup')
    A_CARE_INSIGHT = (By.LINK_TEXT, 'Care Insights')
    A_DATA_INSIGHTS = (By.LINK_TEXT, 'Data Insights')
    A_BILLING_REVIEW = (By.LINK_TEXT, 'Billing Review')
    A_PROFILE = (By.XPATH, '//ul[@id="ulMenu"]//a[@title="User Profile Menu"]')
    A_SUPPORT_CENTRE = (By.XPATH, '//ul[@data-id="user-profile"]//li[7]')
    A_CALL_DASHBOARD = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="Call Dashboard"]')

    A_SYSTEM_NOTIFICATIONS = (By.XPATH, '//*[@id="sysNoti-label"]')
    A_CAREGIVER_COMMUNICATION_HISTORY = (By.LINK_TEXT, 'Caregiver Communications History')
    Tab_received = (By.ID, "page1_ah2")
    Receiver_Text = (By.XPATH, "//table[@id='page2_ContentPlaceHolder1_gvReceivedMessages']//tr[2]//td[6]")
    Receiver_Text3 = (By.XPATH, '//*[@id="showrecvmsgboxclick"]/div/div[1]/div[1]/h2')
    A_CHANGE_PASSWORD_ADMIN = (By.XPATH, '//*[@id="ulMenu"]/li[9]/ul/li[6]/a')
    A_EDI_TOOL = (By.LINK_TEXT, 'EDI Tool')
    BUTTON_SEARCH_EDI = (By.XPATH, '//input[@value="Search"]')
    BUTTON_RESET_EDI = (By.XPATH, '//input[@value="Reset"]')

    # Admin
    A_OPERATION_WORKLIST_ADMIN = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="Ops Worklist Setup"]')
    A_DUTY_LIST_SETUP = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="Duty List Setup"]')
    A_COORDINATOR_SETUP = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="Coordinator Setup"]')
    A_NEW_COORDINATOR = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="New Coordinator"]')
    A_SEARCH_COORDINATOR = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="New Coordinator"]')
    A_FORM = (By.LINK_TEXT, 'Forms')
    A_Compliance_Setup = (By.LINK_TEXT, 'Compliance Setup')
    A_IMPORT_FILES = (By.LINK_TEXT, 'Import Files')

    # Popup Menu
    A_USER_MANAGEMENT = (By.LINK_TEXT, 'User Management')
    A_CHANGE_PASSWORD = (By.LINK_TEXT, 'Change Password')
    A_USER_SEARCH = (By.XPATH, '//*[@id="ulMenu"]//a[normalize-space()="User Search"]')
    A_Edit_Roles = (By.XPATH, '//*[@id="ulMenu"]//a[text()=" Edit Roles"]')
    D_ROLE_DROPDOWN = (By.ID, "ddlSection")
    A_ADMIN_SEARCH_USER = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxbtnSearch"]')
    A_AGENCY_PROFILE = (By.LINK_TEXT, 'Agency Profile')
    A_Service_Portal_Management = (By.LINK_TEXT, 'Services Portal Management')

    A_SEARCH_BUTTON_BATCH = (By.XPATH, '//*[@id="btnSearch"]')
    A_BATCH_NUMBER = (By.XPATH, '//*[@id="tblGridPayrollBatch"]/tbody/tr[5]/td[1]/a')
    A_CAREGIVER_CODE = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxTxtAideCode"]')

    # Popup Sub Menu
    A_NEW_USER = (By.LINK_TEXT, 'New User')
    A_REFERRAL_LINK = (By.LINK_TEXT, 'Referral Patient Management')
    A_NEW_REFERRAL_PATIENT = (By.LINK_TEXT, 'New Referral Patient')
    A_Service_Portal_User_Management = (By.LINK_TEXT, 'Services Portal User Management')
    A_Announcements = (By.LINK_TEXT, 'Announcements')
    A_SEARCH_BY_CAREGIVER = (By.LINK_TEXT, 'Search By Caregiver')
    A_INPUT_OLD_PASSWORD_ADMIN = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxtxtOldPassword"]')
    A_INPUT_NEW_PASSWORD_ADMIN = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxtxtPassword"]')
    A_CONFIRM_PASSWORD_ADMIN = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxtxtConfirmPassword"]')
    A_BUTTON_SAVE_PASSWORD = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxbtnSave"]')
    A_DIRECT_MESSAGE = (By.LINK_TEXT, 'Direct Messages')
    A_ADD_MESSAGE = (By.ID, 'page1_ContentPlaceHolder1_lnkNewMessage')
    A_ADD_MESSAGE2 = (By.ID, 'page2_ContentPlaceHolder1_lnkNewMessage')
    A_INTERNAL_MESSAGE = (By.LINK_TEXT, 'Internal Message')
    A_RECEIVED = (By.LINK_TEXT, 'Received')
    A_TASK = (By.LINK_TEXT, 'Tasks')
    A_ADD_TASK = (By.LINK_TEXT, 'Add Task')
    A_BULK_ACTION = (By.LINK_TEXT, 'Bulk Action')
    A_Mobile_USER_MANAGEMENT = (By.LINK_TEXT, 'Mobile User Management')
    A_Mobile_USER_SEARCH = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxbtnSearch"]')
    BUTTON_SEARCH = '#page2_ContentPlaceHolder1_btnSearchReceived'

    BUTTON_SEARCH_TASK = (By.ID, 'page2_ContentPlaceHolder1_btnSearchSent')
    BUTTON_SAVE_AS_READ = (By.XPATH, '//*[@id="btnRead" or normalize-space()="Mark as Read and Close"]')

    IFRAME_MESSAGE = 'ctl00_ContentPlaceHolder1_iframesentmessages'
    IFRAME_TO_DO = 'ctl00_ContentPlaceHolder1_iframesentodo'
    IFRAME_EVENT = 'ctl00_ContentPlaceHolder1_iframeevent'
    IFRAME_EDI_TOOL = 'ctl00_ContentPlaceHolder1_frameEDITool'

    INPUT_FROM_DATE = (By.ID, 'page2_ContentPlaceHolder1_txtFromDateReceived')
    INPUT_TO_DATE = (By.ID, 'page2_ContentPlaceHolder1_txtToDateReceived')
    INPUT_FROM_DATE_SENT = (By.ID, 'page2_ContentPlaceHolder1_txtFromDateSent')
    INPUT_TO_DATE_SENT = (By.ID, 'page2_ContentPlaceHolder1_txtToDateSent')

    SPAN_COUNT = (By.ID, 'page2_ContentPlaceHolder1_lblSearchResult')
    INPUT_PAYROLL_DATE = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxDtPayroll"]')
    PAYROLL_CAREGIVER_SEARCH = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_uxBtnSearch"]')

    # Report
    A_REPORT = (By.LINK_TEXT, 'Report')
    A_VISIT_COUNT = (By.ID, 'tdVisitCaseCountReskin')
    A_ReportingTool = (By.LINK_TEXT, 'Reporting Tool (2.0)')
    # System Notification
    A_SYSTEM_NOTIFICATIONS = (By.XPATH, '//*[@id="sysNoti-label"]')
    A_SYSTEM_NOTIFICATIONS_SEARCH = (By.XPATH, '//div[@id = "sysNoti"]//*[@id = "btnSearch"]')
    A_SELECT_PRIORITY2 = (By.XPATH, '//*[@id="ddlPrioritySent"]/option[2]')
    A_PRIORITY_SORTING = (By.XPATH, '//*[@id="gvRecNotification"]/tbody/tr[1]/th[3]/a')

    IFRAME_SYS_NOTI = 'ctl00_ContentPlaceHolder1_iframesysnoti'
    SYS_NOTI_CHECKBOX = (By.XPATH, '//*[@id="gvRecNotification_ctl04_chkDismiss"]')

    Eligibility_Batch_Review = (By.LINK_TEXT, 'Eligibility Batch Review')
    Eligibility_Batch_Review_Window = 'ctl00_ContentPlaceHolder1_ifrmEligibilityBatchDetails'
    Eligibility_Batch_Review_Search = (By.XPATH, '//input[@id="ctl00_ContentPlaceHolder1_btnSearch"]')

    # File Processing
    A_FILE_PROCESSING = (By.LINK_TEXT, 'File Processing')
    UPR_CONTRACT = 'UPR Contract'
    Select_Contract = (By.ID, "ctl00_ContentPlaceHolder1_ddlContractType")
    Contract_Automation_UPR = (By.XPATH, "(//input[@data-text='Automation_UPR_Payer (India Only) (986)'])[1]")
    Contract_Choice_Dropdown = (By.ID, "contractDdId_choice")
    CLAIM_GRIED_COUNT = "//table[@id='ctl00_ContentPlaceHolder1_gvFiles']//tbody//tr"
    TAB_REMITTANCE = (By.ID, 'tpRemittances-label')
    REMITTANCE_SEARCH_BTN = (By.ID, 'ctl00_ContentPlaceHolder1_uxbtnSearchRemittances')

    # Operational Worklist
    a_hhaexchange = (By.LINK_TEXT, 'HHAeXchange')
    url = 'https://www.hhaexchange.com/'
    a_customer_support = (By.LINK_TEXT, 'Support Center')
    h1_heading = (By.ID, "HHAeXchangeProviderKnowledgeBase")

    BUTTON_CLOSE_PENDO = (By.XPATH, '//*[contains(@id, "pendo-close-guide")]')
    Caregiver_Action = (By.XPATH, '//a[normalize-space() = "Action"]')

    Pagination_Pending_Placement_Previous = (By.ID, 'tbVendorPendingPlacement_previous')
    Pagination_Pending_Placement_Next = (By.ID, 'tbVendorPendingPlacement_next')
    Pagination_Pending_Placement_Current = (By.XPATH,
                                            '//li[@id="tbVendorPendingStaffedCaregiverObj_previous"]/following-sibling::li[@class="paginate_button current"]')
    Pagination_Pending_Placement_Page_2 = (By.XPATH,
                                           '//li[@id="tbVendorPendingStaffedCaregiverObj_previous"]/following-sibling::li[@class="paginate_button" and text()="2"]')
    BTN_CONTINUE = (By.XPATH, '//form[@id="confirm"]//input[@value="Continue"]')
    OLD_ENT_LOGOUT = (By.ID, 'ctl00_LoginStatus1')
    TABLE_ALL_ROWS = (By.XPATH, "//table[contains(@class, 'hhax-table')]//tbody/tr[td]")
    Main_Menu = (By.XPATH, '//button[@class="menu-icon bottom"]')
