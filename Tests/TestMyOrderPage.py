from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestMyOrderPage(BaseTest):
    def test_profile_option_displayed(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_profile_option_displayed()
        assert message is True

    def test_profile_option_clickable(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_prfile_option_clickable()
        assert message is True

    def test_my_account_option_displayed(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_account_option_displayed()
        assert message is True

    def test_my_account_option_cliackable(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_account_option_clickable()
        assert message is True

    def test_my_campaign_option_displayed(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_campaign_option_displayed()
        assert message is True

    def test_my_campaign_option_cliackable(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_campaign_option_clickable()
        assert message is True

    def test_my_cart_option_displayed(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_cart_option_displayed()
        assert message is True

    def test_my_cart_option_cliackable(self):
        self.loginpage= LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.my_cart_option_clickable()
        assert message is True

    def test_content_hub_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.content_hub_option_displayed()
        assert message is True

    def test_content_hub_option_cliackable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.content_hub_option_clickable()
        assert message is True

    def test_logout_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.logout_option_is_displayed()
        assert message is True

    def test_logout_option_cliackable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.logout_option_is_clickable()
        assert message is True

    def test_booking_view_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.booking_view_option_displayed()
        assert message is True

    def test_booking_view_option_cliackable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.booking_view_option_is_clickable()
        assert message is True

    def test_action_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.action_option_displayed()
        assert message is True

    def test_action_option_cliackable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.action_option_clickable()
        assert message is True

    def test_new_campaign_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.new_campaign_option_displayed()
        assert message is True

    def test_new_campaign_action_option_cliackable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.new_campaign_option_clickable()
        assert message is True

    # def test_new_campaign_action_option_cliackable(self):
    #     self.loginpage = LoginPage(self.driver)
    #     myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
    #     myorderpage.new_campaign_click_operation()


    def test_logout_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.logout_operation()
        assert message.__contains__("https://test-bigoutdoor.lmx.ai/login")

    def test_search_campaign(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message =myorderpage.search_campaign("afewf")
        assert message.__contains__("afewf")

    def test_search_campaign(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.reset_search_campaign("afewf")
        assert message.__contains__("")

    def test_sortby_draft(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.sort_by_draft("GENERATED")
        assert message.__contains__("drafts")

    def test_sortby_request(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.sort_by_Request("REQUESTED")
        assert message.__contains__("requested")

    def test_booking_view_is_opened(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.booking_view_option_open()
        assert message is True

    def test_mapview_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.is_mapview_displayed_in_views()
        assert message is True

    def test_Galleryview_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.is_gallery_view_displayed_in_views()
        assert message is True

    def test_mapview_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.is_mapview_clickable_in_views()
        assert message is True

    def test_Galleryview_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.is_gallery_view_clickable_in_views()
        assert message is True

    def test_map_is_displayed_in_mapView(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.map_is_diplayed_in_mapView()
        assert message is True

    def test_Gallery_is_displayed_in_GalleryView(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.gallery_is_diplayed_in_galleryView()
        assert message is True

    def test_close_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.close_button_is_displayed_in_views()
        assert message is True

    def test_close_button_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        message = myorderpage.close_button_is_Clickable_in_views()
        assert message is True

    def test_close_button_is_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        myorderpage.perform_close_button_in_views()





