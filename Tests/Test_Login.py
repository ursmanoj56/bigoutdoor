import pytest

from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtilities import get_data_from_excel


class TestLogin(BaseTest):

    def test_validate_title(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.validate_title()
        assert message.__contains__("Online Self Serve Platform")

    def test_validate_url(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.validate_url()
        assert message.__contains__("https://test-bigoutdoor.lmx.ai/login")



    def test_display_loginpage(self):
        self.loginpage=LoginPage(self.driver)
        message =self.loginpage.is_LoginPage_displayed()
        assert message is True

    def test_explore_button_is_displayed(self):
        self.loginpage=LoginPage(self.driver)
        message =self.loginpage.is_ExploreButton_is_displayed()
        assert  message is True

    def test_explore_button_is_clickable(self):
        self.loginpage=LoginPage(self.driver)
        message =self.loginpage.is_ExploreButton_is_clickable()
        assert message is True

    def test_forgot_password_option_displayed(self):
         self.loginpage = LoginPage(self.driver)
         message = self.loginpage.is_forgot_password_is_displayed()
         assert message is True

    def test_forgot_password_option_Clickable(self):
         self.loginpage = LoginPage(self.driver)
         message = self.loginpage.is_forgot_Password_is_clickable()
         assert message is True

    def test_Register_option_displayed(self):
         self.loginpage = LoginPage(self.driver)
         message = self.loginpage.is_register_option_is_displayed()
         assert message is True

    def test_Register_option_option_clickable(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.is_register_option_is_clickable()
        assert message is True

    def test_login_button_enable_before_credential(self):
         self.loginpage=LoginPage(self.driver)
         message =self.loginpage.is_LoginButton_is_enable_before_credential()
         assert message is False

    def test_login_button_enable_after_credential(self):
        self.loginpage = LoginPage(self.driver)
        message=self.loginpage.is_loginButton_is_enable_after_credential("surrendar_bigoutdoor", "Test123")
        assert message is True


    def test_valid_login(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")

    @pytest.mark.parametrize("username,password",get_data_from_excel(r"C:\Users\HP\PycharmProjects\SS0\TestFiles\OSS2-Login.xlsx",  "LoginTest"))
    def test_invalid_login(self, username, password):
        self.loginpage = LoginPage(self.driver)
        message=self.loginpage.login_with_invalid_credential(username, password)
        assert message.__contains__("unauthorized login attempt!")





