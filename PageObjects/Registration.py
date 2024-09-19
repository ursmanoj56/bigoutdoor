from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class Registration(BasePage):
    FIRST_NAME=(By.XPATH ,"//input[@placeholder='First Name']")
    LAST_NAME=(By.XPATH,"//input[@placeholder='Last Name']")
    PHONE_NUMBER =(By.XPATH ,"//input[@placeholder='Phone Number']")
    PHONE_NUM_ERROR_MESSGAE =(By.XPATH,"//small[contains(text(),'Your mobile number should include')]")
    USER_NAME = (By.XPATH ,"//input[@placeholder='User Name']")
    MAIL_ADDRESS = (By.XPATH, "//input[@placeholder='Email Address']")
    MAIL_ERROR_MESSAGE = (By.XPATH ,"//small[contains(text(),' * Please enter valid email ')]")
    JOB_TITLE = (By.XPATH ,"//input[@placeholder='Job Title']")
    COMPANY_NAME = (By.XPATH ,"//input[@placeholder='Full Company Name']")
    COMPANY_ADDRESS = (By.XPATH ,"//input[@placeholder='Company Address']")
    INDUSTRY = (By.XPATH ,"//input[@placeholder='Industry']")
    REGISTRATION_ID =(By.XPATH ,"//input[@placeholder='Registration ID']")
    COMPANY_PHONE_NUM = (By.XPATH, "//input[@placeholder='Company Phone Number']")
    PASSWORD =(By.XPATH ,"//input[@placeholder='Password']")
    PASSWORD_LENGTH_ERROR = (By.XPATH ,"//div[contains(text(),'Password must be at least 6 characters')]")
    CONFIRM_PASSWORD = (By.XPATH , "//input[@placeholder='Confirm Password']")
    PASSWORD_MISMATCH_ERROR = (By.XPATH ,"//div[contains(text(),'Passwords must match')]")
    SELECT_COUNTRY =(By.XPATH, "//select[@formcontrolname='userCountry']")
    SELECT_STATE =(By.XPATH ,"//select[@formcontrolname='userState']")

    REGISTER_BUTTON =(By.XPATH, "//button[text()='Register']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_register_button_displayed(self):
        return self.is_displayed(self.REGISTER_BUTTON)

    def is_register_button_is_disable(self):
        return self.is_element_enabled(self.REGISTER_BUTTON)

    def register_with_invalid_credentials(self,firstname,lastname,mobilenumber,username,mailid,jobtitle,companyname,country,state,companyAddress,industry,registerID,companyPhone,password,confirmPassword):
        self.text_inputs(self.FIRST_NAME,firstname)
        self.text_inputs(self.LAST_NAME, lastname)
        self.text_inputs(self.PHONE_NUMBER, mobilenumber)
        self.text_inputs(self.USER_NAME, username)
        self.text_inputs(self.MAIL_ADDRESS, mailid)
        self.text_inputs(self.JOB_TITLE, jobtitle)
        self.text_inputs(self.COMPANY_NAME, companyname)
        self.select_dropdown_option_by_value(self.SELECT_COUNTRY,country)
        self.select_dropdown_option_by_value(self.SELECT_STATE,state)
        self.text_inputs(self.COMPANY_ADDRESS, companyAddress)
        self.text_inputs(self.INDUSTRY, industry)
        self.text_inputs(self.REGISTRATION_ID, registerID)
        self.text_inputs(self.COMPANY_PHONE_NUM, companyPhone)
        self.text_inputs(self.PASSWORD, password)
        self.text_inputs(self.CONFIRM_PASSWORD, confirmPassword)
        self.scroll_into_view(self.REGISTER_BUTTON)
        return self.is_element_enabled(self.REGISTER_BUTTON)

    def register_with_valid_credentials(self,firstname,lastname,mobilenumber,username,mailid,jobtitle,companyname,country,state,companyAddress,industry,registerID,companyPhone,password,confirmPassword):
        self.text_inputs(self.FIRST_NAME,firstname)
        self.text_inputs(self.LAST_NAME, lastname)
        self.text_inputs(self.PHONE_NUMBER, mobilenumber)
        self.text_inputs(self.USER_NAME, username)
        self.text_inputs(self.MAIL_ADDRESS, mailid)
        self.text_inputs(self.JOB_TITLE, jobtitle)
        self.text_inputs(self.COMPANY_NAME, companyname)
        self.select_dropdown_option_by_value(self.SELECT_COUNTRY,country)
        self.select_dropdown_option_by_value(self.SELECT_STATE,state)
        self.text_inputs(self.COMPANY_ADDRESS, companyAddress)
        self.text_inputs(self.INDUSTRY, industry)
        self.text_inputs(self.REGISTRATION_ID, registerID)
        self.text_inputs(self.COMPANY_PHONE_NUM, companyPhone)
        self.text_inputs(self.PASSWORD, password)
        self.text_inputs(self.CONFIRM_PASSWORD, confirmPassword)
        self.scroll_into_view(self.REGISTER_BUTTON)
        self.click_button(self.REGISTER_BUTTON)

    def phone_number_error_message(self):
        return self.get_text(self.PHONE_NUM_ERROR_MESSGAE)

    def mail_id_error_message(self):
        return self.get_text(self.MAIL_ERROR_MESSAGE)

    def password_length_err_message(self):
        return self.get_text(self.PASSWORD_LENGTH_ERROR)

    def password_length_err_message(self):
        return self.get_text(self.PASSWORD_LENGTH_ERROR)

    def password_match_err_message(self):
        return self.get_text(self.PASSWORD_MISMATCH_ERROR)

    def scroll_view(self):
        self.scroll_up()

    def scroll_to_reg_button(self):
        self.scroll_into_view(self.REGISTER_BUTTON)




