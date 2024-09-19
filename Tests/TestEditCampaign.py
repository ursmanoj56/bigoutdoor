from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestEditCampaign(BaseTest):

    def test_select_date(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign =myorderpage.action_option_operation()
        editcampaign.open_date_picker()
        editcampaign.navigate_to_month("Aug", 2024)  # June 2024
        editcampaign.select_date1(21)
        editcampaign.navigate_to_month("Sep", 2024)  # June 2024
        editcampaign.select_date1(21)

    def test_new_billboard_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.add_new_billboard_option_displaed()
        assert message is True

    def test_new_billboard_option_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.add_new_billboard_option_clickable()
        assert message is True

    def test_check_box_available_inventory_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.check_box_available_inventory_is_displaed()
        assert message is True

    def test_check_box_available_inventory_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.check_box_available_inventory_is_Clickale()
        assert message is True

    def test_update_campaign_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.update_campaign_option_is_displayed()
        assert message is True

    def test_update_campaign_option_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.update_campaign_option_is_clickable()
        assert message is True

    def test_map_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.map_is_displaed()
        assert message is True

    def test_street_map_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.street_map_option_is_displaed()
        assert message is True

    def test_street_map_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.street_map_option_is_clickable()
        assert message is True

    def test_street_map_terrain_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.street_map_terrain_option_displaed()
        assert message is True

    def test_street_map_terrain_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.street_map_terrain_option_clickable()
        assert message is True

    def test_street_map_terrain_is_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        editcampaign.street_map_terrain_option_click_operation()

    def test_sattelite_map_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.sattelite_map_option_is_displaed()
        assert message is True

    def test_sattelite_map_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.sattelite_map_option_is_clickable()
        assert message is True

    def test_sattelite_map_label_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.sattelite_map_label_option_displaed()
        assert message is True

    def test_sattelite_map_label_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.sattelite_map_label_option_clickable()
        assert message is True

    def test_sattelite_map_label_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        editcampaign.sattelite_map_label_option_click_operation()

    def test_full_map_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.full_map_view_option_displayed()
        assert message is True

    def test_full_map_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.full_map_view_option_clickable()
        assert message is True

    def test_full_map_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        editcampaign.full_map_view_option_click_operation()

    def test_zoom_in_map_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.zoom_in_option_is_displaed_in_map()
        assert message is True

    def test_zoom_in_map_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.zoom_in_option_is_clickable_in_map()
        assert message is True

    def test_zoom_in_map_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        editcampaign.full_map_view_option_click_operation()

    def test_zoom_out_map_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.zoom_out_option_is_displaed_in_map()
        assert message is True

    def test_zoom_out_map_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.zoom_out_option_is_clickable_in_map()
        assert message is True

    def test_zoom_out_map_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        editcampaign.zoom_out_oprion_click_operation()

    def test_billboard_location_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.billboard_location_displayed_in_map()
        assert message is True

    def test_billboard_location_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        message = editcampaign.billboard_location_clickable_in_map()
        assert message is True

    def test_billboard_is_displayed_when_click_Map_bill_location(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        editcampaign = myorderpage.action_option_operation()
        editcampaign.billboard_is_displaed_when_click_bill_location()



