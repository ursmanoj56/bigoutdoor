from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestForgotPassWord(BaseTest):

    def test_validate_url(self):
        self.loginpage=LoginPage(self.driver)
        self.forgotpassword=self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.validate_url()
        assert message.__contains__("https://test-bigoutdoor.lmx.ai/forgot-password")

    def test_is_mailBox_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.is_mail_box_displayed()
        assert message is True

    def test_is_sendVerifyCode_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.is_send_verify_button_is_displayed()
        assert message is True

    def test_sendButton_is_enable_before_credential(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.is_send_verifyCode_buttonEnable_before_enterMail()
        assert message is False

    def test_sendButton_is_enable_before_credential(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.is_send_verifyCode_buttonEnable_after_enterMail("manoj@gmail.com")
        assert message is True

    def test_error_message_with_invalid_mailID(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.validate_with_invalid_mail("manoj")
        assert message.__contains__("* This field is required.")

    def test_error_message_with_invalid_mailID(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.validate_with_valid_mailID("manoj.endluri@gmail.com")
        assert message.__contains__("Check your email for a link to reset your password")

    def test_regiter_button_is_displayd(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.is_Regiter_button_is_displayed()
        assert message is True

    def test_regiter_button_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        self.forgotpassword = self.loginpage.click_ForgotPassword()
        message = self.forgotpassword.is_Register_button_is_clickable()
        assert message is True






