from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class ForgotPassword(BasePage):
    EMAIL_BOX = (By.ID,"email")
    SEND_VERIFY_CODE = (By.XPATH ,"(//button)[3]")
    REGISRER_NOW = (By.XPATH , "//a[text()='Register Now!']")
    ALERT_MESSAGE =(By.XPATH, "//div[contains(text(),'Check your email for a link to reset your password')]")
    WARN_MESSAGE =(By.XPATH,"//span[text()=' * Please enter valid email ']")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_url(self):
        return self.get_current_url()

    def is_mail_box_displayed(self):
        return self.is_displayed(self.EMAIL_BOX)

    def is_send_verify_button_is_displayed(self):
        return self.is_displayed(self.SEND_VERIFY_CODE)

    def is_send_verifyCode_buttonEnable_before_enterMail(self):
        return self.is_element_enabled(self.SEND_VERIFY_CODE)

    def is_send_verifyCode_buttonEnable_after_enterMail(self,mail):
        self.text_input(self.EMAIL_BOX,mail)
        return self.is_element_enabled(self.SEND_VERIFY_CODE)

    def validate_with_invalid_mail(self ,mail):
        self.text_input(self.EMAIL_BOX,mail)
        self.click_button(self.SEND_VERIFY_CODE)
        return self.get_text(self.WARN_MESSAGE)

    def validate_with_valid_mailID(self,mail):
        self.text_input(self.EMAIL_BOX, mail)
        self.click_button(self.SEND_VERIFY_CODE)
        return self.get_text(self.ALERT_MESSAGE)

    def is_Regiter_button_is_displayed(self):
        return self.is_displayed(self.REGISRER_NOW)

    def is_Register_button_is_clickable(self):
        return self.clickable(self.REGISRER_NOW)



