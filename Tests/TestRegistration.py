import pytest

from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Utilities.ExcelUtilities import get_data_from_excel


class TestRegistration(BaseTest):
    @pytest.mark.parametrize("firstname,lastname,mobilenumber,username,mailid,jobtitle,companyname,country,state,companyAddress,industry,registerID,companyPhone,password,confirmPassword",get_data_from_excel(r"C:\Users\HP\PycharmProjects\SS0\TestFiles\OSS-Registration.xlsx","Register"))
    def test_invalid_registration(self,firstname,lastname,mobilenumber,username,mailid,jobtitle,companyname,country,state,companyAddress,industry,registerID,companyPhone,password,confirmPassword):
        self.loginpage = LoginPage(self.driver)
        registration=self.loginpage.click_Register()
        registration.register_with_invalid_credentials(firstname,lastname,mobilenumber,username,mailid,jobtitle,companyname,country,state,companyAddress,industry,registerID,companyPhone,password,confirmPassword)
        registration.scroll_view()
        message1 = registration.phone_number_error_message()
        message2 = registration.mail_id_error_message()
        message3 = registration.password_length_err_message()
        message4 = registration.password_match_err_message()
        registration.scroll_to_reg_button()
        message5 = registration.is_register_button_is_disable()
        assert((message1.__contains__("Your mobile number should include") or message2.__contains__("* Please enter valid email") or message3.__contains__("Password must be at least 6 characters") or message4.__contains__("Passwords must match")) and (message5 is False) )

    def test_valid_registration(self):
        self.loginpage = LoginPage(self.driver)
        registration = self.loginpage.click_Register()
        registration.register_with_valid_credentials("Manoj", "Endluri", "+9740808574", "usermanoj", "manoj@gmail.com", "testengineer", "vanigama", "India","Andhra Pradesh", "adyar chennai", "it",
                                                       "34566", "345643344", "123456", "123456")

    def test_is_Register_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        registration = self.loginpage.click_Register()
        message = registration.is_register_button_displayed()
        assert message is True

    def test_is_Register_button_is_disabled(self):
        self.loginpage = LoginPage(self.driver)
        registration = self.loginpage.click_Register()
        message = registration.is_register_button_is_disable()
        assert message is False



