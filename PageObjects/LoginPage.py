from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.ForgotPassword import ForgotPassword
from PageObjects.MyOrderPage import MyOrderPage
from PageObjects.Registration import Registration


class LoginPage(BasePage):
    USER_NAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON1 = (By.XPATH, "(//button[@title='Login'])[1]")
    LOGIN_BUTTON2 = (By.XPATH, "(//button[@title='Login'])[2]")
    EXPLORE_BUTTON = (By.XPATH, "//button[@title='Explore']")
    FORGOT_PASSWORD = (By.XPATH, "//a[text()='Forgot password?']")
    REGISTER = (By.XPATH, "//a[text()='Register!']")
    WARN_MESSAGE = (By.XPATH, "//div[@id='toast-container']/div/div[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_title(self):
        return self.get_title()

    def validate_url(self):
        return self.get_current_url()
    def is_LoginPage_displayed(self):
        return self.is_displayed(self.LOGIN_BUTTON2)

    def is_ExploreButton_is_displayed(self):
        return self.is_displayed(self.EXPLORE_BUTTON)

    def is_ExploreButton_is_clickable(self):
        return self.clickable(self.EXPLORE_BUTTON)

    def is_LoginButton_is_enable_before_credential(self):
        return self.is_element_enabled(self.LOGIN_BUTTON2)

    def is_loginButton_is_enable_after_credential(self,username,password):
        self.text_input(self.USER_NAME, username)
        self.text_input(self.PASSWORD, password)
        return self.is_element_enabled(self.LOGIN_BUTTON2)


    def login_with_valid_credential(self, username, password):
        self.text_input(self.USER_NAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_BUTTON2)
        return MyOrderPage(self.driver)

    def login_with_invalid_credential(self, username, password):
        self.text_input(self.USER_NAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_BUTTON2)
        return self.get_text(self.WARN_MESSAGE)

    def is_forgot_password_is_displayed(self):
        return self.is_displayed(self.FORGOT_PASSWORD)

    def is_forgot_Password_is_clickable(self):
        return self.clickable(self.FORGOT_PASSWORD)

    def is_register_option_is_displayed(self):
        return self.is_displayed(self.REGISTER)

    def is_register_option_is_clickable(self):
        return self.clickable(self.REGISTER)

    def click_ForgotPassword(self):
        self.click_button(self.FORGOT_PASSWORD)
        return ForgotPassword(self.driver)

    def click_Register(self):
        self.click_button(self.REGISTER)
        return Registration(self.driver)
