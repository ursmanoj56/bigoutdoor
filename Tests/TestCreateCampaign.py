from PageObjects.CreateCampaign import CreateCampaign
from PageObjects.EditCampaign import EditCampaign
from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestCreateCampaign(BaseTest):

    def test_get_current_month(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.open_date_picker2()
        message =createcampaign.get_current_month_year2()
        assert message.__contains__('Jun 2024')

    def test_next_calender_button(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.open_date_picker2()
        createcampaign.click_next_calender()

    def test_select_date(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.open_date_picker2()
        createcampaign.select_date2(21)



    def test_select_date_duration(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.open_date_picker2()
        createcampaign.navigate_to_month2("Aug", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.navigate_to_month2("Sep", 2024)  # June 2024
        createcampaign.select_date2(21)


    def test_start_create_campaign(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.create_campaign("manoj")
        createcampaign.open_date_picker2()
        createcampaign.navigate_to_month2("Aug", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.navigate_to_month2("Sep", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.clik_next_operation()

    def test_next_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        message = createcampaign.click_next_button_is_displayed()
        assert message is True

    def test_next_button_is_clickabke(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        message = createcampaign.click_next_button_is_clickable()
        assert message is True

    def test_validate_error_messge_when_click_button_without_field(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        message = createcampaign.validate_error_messge_when_click_button_without_field()
        assert message.__contains__("Form Fields are should not be empty")




    def test_edit_campaign_name(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.create_campaign("manoj")
        createcampaign.open_date_picker2()
        createcampaign.navigate_to_month2("Aug", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.navigate_to_month2("Sep", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.clik_next_operation()
        createcampaign.edit_campaign_name("manojkumar")

    def test_edit_calender_date(self):
        self.loginpage = LoginPage(self.driver)

        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        createcampaign = myorderpage.new_campaign_click_operation()
        createcampaign.create_campaign("manoj")
        createcampaign.open_date_picker2()
        createcampaign.navigate_to_month2("Aug", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.navigate_to_month2("Sep", 2024)  # June 2024
        createcampaign.select_date2(21)
        createcampaign.clik_next_operation()
        createcampaign.edit_campaign_name("manojkumar")
        createcampaign.open_date_picker()
        createcampaign.navigate_to_month("Sep", 2024)
        createcampaign.select_date1(21)
        createcampaign.navigate_to_month("Oct", 2024)
        createcampaign.select_date1(21)

    def test_digital_billboard_is_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_digible_billboard_option_dispalyed()
        assert message is True

    def test_digital_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_digital_billboard_option_clickable()
        assert message is True

    def test_classical_billboard_is_displyed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_classic_billboard_option_dispalyed()
        assert message is True

    def test_classical_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_classic_billboard_option_clickable()
        assert message is True

    def test_map_view_is_displyed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_map_view_is_dispaled()
        assert message is True

    def test_map_view_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_map_view_clickable()
        assert message is True

    def test_available_inventory_is_displyed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_available_inventory_option_displayed()
        assert message is True

    def test_available_inventory_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.is_availale_inventory_option_clickable()
        assert message is True

    def test_available_inventory_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.is_availale_inventory_option_click_operaion()

    def test_billbord_views_option_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message =self.createcampaign.is_billboard_view_option_clickable()
        assert message is True

    def test_validate_classic_when_click_classic_billboard_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.validate_classic_when_click_classic_billboard_option()
        assert message.__contains__("Classic Billboard")

    def test_validate_digital_when_click_digital_billboard_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.validate_digital_when_click_digital_billboard_option()
        assert message.__contains__("Digital Billboard")

    def test_validate_when_click_mapview_to_display_mapviewBillborads(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.validate_when_click_mapview_to_display_mapviewBillborads()
        assert message is True

    def test_validate_when_click_list_view_to_display_listviewBillborads(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.validate_when_click_listview_to_display_listviewBillborads()
        assert message is False

    def test_search_billboards(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.search_billboards(" Sydney Harbour Bridge ")
        assert message.__contains__(" Sydney Harbour Bridge ")

    def test_apply_button_is_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.apply_button_is_displayd()
        assert message is True

    def test_apply_button_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.apply_button_is_clickble()
        assert message is True

    def test_reset_button_is_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.reset_button_is_displayed()
        assert message is True

    def test_reset_button_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.reset_button_is_clickable()
        assert message is True

    def test_filter_by_price(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_Price(1000,50000)
        message = int(message.replace(',', ''))
        assert(message <=50,000 and message >=1000)

    def test_reset_filter_by_price(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_filter_by_price()
        message = self.createcampaign.reset_filter_price_operation()
        assert message.__contains__("")

    def test_street_map_option_is_displaed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.street_map_option_is_displaed()
        assert message is True

    def test_street_map_option_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.street_map_option_is_clickable()
        assert message is True

    def test_street_map_terrain_option_displaed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.street_map_terrain_option_displaed()
        assert message is True

    def test_street_map_terrain_option_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.street_map_terrain_option_clickable()
        assert message is True

    def test_street_map_terrain_option_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.street_map_terrain_option_click_operation()

    def test_sattelite_map_option_is_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.sattelite_map_label_option_displaed()
        assert message is True

    def test_sattelite_map_option_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.sattelite_map_option_is_clickable()
        assert message is True

    def test_sattelite_map_label_option_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.sattelite_map_label_option_displaed()
        assert message is True

    def test_sattelite_map_label_option_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.sattelite_map_label_option_clickable()
        assert message is True

    def test_sattelite_map_label_option_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.sattelite_map_label_option_click_operation()

    def test_full_map_view_option_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.full_map_view_option_displayed()
        assert message is True

    def test_full_map_view_option_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.full_map_view_option_clickable()
        assert message is True

    def test_full_map_view_option_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.full_map_view_option_click_operation()

    def test_zoom_in_option_is_displayed_in_map(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.zoom_in_option_is_displaed_in_map()
        assert message is True

    def test_zoom_in_option_is_clickable_in_map(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.zoom_in_option_is_clickable_in_map()
        assert message is True

    def test_zoom_in_oprion_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.zoom_in_oprion_click_operation()

    def test_zoom_out_option_is_displayed_in_map(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.zoom_out_option_is_displaed_in_map()
        assert message is True

    def test_zoom_out_option_is_clickable_in_map(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.zoom_out_option_is_clickable_in_map()
        assert message is True

    def test_zoom_out_oprion_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.zoom_out_oprion_click_operation()

    def test_billboard_location_is_displayed(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.billboard_location_is_displayed()
        assert message is True

    def test_billboard_location_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.billboard_location_is_clickable()
        assert message is True

    def test_billboard_image_displayed_in_map_when_click_location(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.billboard_image_displayed_in_map_when_click_location()
        assert message is True

    def test_billboard_name_displayed_in_map_when_click_location(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.billboard_name_displayed_in_map_when_click_location()
        assert message.__contains__("Melbourne VIC")

    def test_billboard_image_is_clickable_in_map_location(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.billboard_image_is_clickable_in_map_location()
        assert message is True

    def test_billboard_details_displayed_when_clickimage_clicka_in_map_location(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.billboard_details_displayed_when_clickimage_clicka_in_map_location()
        assert message is True

    def test_filter_by_indoor_enviroment_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_indoor_enviroment_is_clickable()
        assert message is True

    def test_filter_by_outdoor_enviroment_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_outdoor_enviroment_is_clickable()
        assert message is True

    def test_filter_by_indoor_enviroment_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_indoor_enviroment_is_click_operation()

    def test_filter_by_outdoor_enviroment_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_outdoor_enviroment_is_click_operation()

    def test_filter_by_digital_type_is_selected(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_digital_type_is_selected()
        assert message is True

    # def test_indooer_is_selected(self):
    #     self.createcampaign = CreateCampaign(self.driver)
    #     self.test_start_create_campaign()
    #     message = self.createcampaign.indooer_is_selected()
    #     assert message is True

    def test_filter_by_small_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_small_billboard_is_clickable()
        assert message is True

    def test_filter_by_medium_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_medium_billboard_is_clickable()
        assert message is True

    def test_filter_by_large_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_large_billboard_is_clickable()
        assert message is True

    def test_filter_by_extra_large_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_extra_large_billboard_is_clickable()
        assert message is True

    def test_filter_by_small_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_small_billboard_is_click_operation()

    def test_filter_by_medium_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_medium_billboard_is_click_operation()

    def test_filter_by_large_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_large_billboard_is_click_operation()

    def test_filter_by_extra_large_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_extra_large_is_click_operation()

    def test_filter_led_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_led_billboard_is_clickable()
        assert message is True

    def test_filter_by_portrait_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_portrait_billboard_is_clickable()
        assert message is True

    def test_filter_by_fascade_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_fascade_billboard_is_clickable()
        assert message is True

    def test_filter_by_standee_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_standee_billboard_is_clickable()
        assert message is True

    def test_filter_by_unipole_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_unipole_billboard_is_clickable()
        assert message is True

    def test_filter_by_pillar_wrap_billboard_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_pillar_wrap_billboard_is_clickable()
        assert message is True

    def test_filter_led_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_led_billboard_is_click_operation()

    def test_filter_by_portrait_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_portrait_billboard_is_click_operation()

    def test_filter_by_fascade_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_fascade_billboard_is_click_operation()

    def test_filter_by_standee_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_standee_billboard_is_click_operation()

    def test_filter_by_unipole_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_unipole_billboard_is_click_operation()

    def test_filter_by_pillar_wrap_billboard_is_click_operation(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_by_pillar_wrap_billboard_is_click_operation()

    def test_filter_by_finacial_option_is_clickable(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_by_finacial_option_is_clickable()
        assert message is True

    def test_filter_display_categeries_when_click_finacial_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_display_categeries_when_click_finacial_option()
        assert message.__contains__("block")

    def test_filter_banks_option_is_selected_when_click_all_sub_categeries(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.filter_banks_option_is_selected_when_click_all_sub_categeries()
        assert message.__contains__("block")

    def test_filter_when_click_bank_option_toSelected_child_categeries(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.filter_when_click_bank_option_toSelected_child_categeries()
        message =self.createcampaign.filter_by_sub_categery_atm_is_selected()
        message1 =self.createcampaign.filter_by_sub_categery_atm123_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_added_items_displayed_when_click_Bank_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_added_items_displayed_when_click_Bank_option()
        message = self.createcampaign.filter_by_added_atm_displayed_when_click_Bank_option()
        message1 = self.createcampaign.filter_by_added_atm123_displayed_when_click_Bank_option()
        assert (message is True and message1 is True)

    def test_in_filter_validate_added_atmItem_is_displayed_when_deselect_ATM(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        message = self.createcampaign.in_filter_validate_added_atmItem_is_displayed_when_deselect_ATM()
        assert message is False

    def test_in_filter_to_check_all_sub_categeries_selectd_when_select_all_categery(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_to_check_all_sub_categeries_selectd_when_select_all_categery()
        message=self.createcampaign.in_filter_sub_categery_airport_is_selected()
        message1 = self.createcampaign.in_filter_sub_categery_buses_is_selected()
        message2 = self.createcampaign.in_filter_sub_categery_subway_is_selected()
        message3 = self.createcampaign.in_filter_sub_categery_taxi_rideshare_top_is_selected()
        message4 = self.createcampaign.in_filter_sub_categery_taxi_rideshare_tv_is_selected()
        message5 = self.createcampaign.in_filter_sub_categery_train_station_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block") and message3.__contains__("block") and message4.__contains__("block") and message5.__contains__("block") )

    def test_in_filter_to_check_all_sub_categeries_selectd_when_not_select_all_categery(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_to_check_all_sub_categeries_selectd_when_not_select_all_categery()
        message=self.createcampaign.in_filter_sub_categery_airport_is_selected()
        message1 = self.createcampaign.in_filter_sub_categery_buses_is_selected()
        message2 = self.createcampaign.in_filter_sub_categery_subway_is_selected()
        message3 = self.createcampaign.in_filter_sub_categery_taxi_rideshare_top_is_selected()
        message4 = self.createcampaign.in_filter_sub_categery_taxi_rideshare_tv_is_selected()
        message5 = self.createcampaign.in_filter_sub_categery_train_station_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none") and message3.__contains__("none") and message4.__contains__("none") and message5.__contains__("none") )

    def test_in_filter_all_products_selected_when_click_airport_categery(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_all_products_are_selected_when_click_airport_categery()
        message=self.createcampaign.in_filter_airport_categery_arrival_hall_is_selected()
        message1 = self.createcampaign.in_filter_airport_categery_baggage_claim_is_selected()
        message2 = self.createcampaign.in_filter_airport_categery_depature_hall_is_selected()
        message3 = self.createcampaign.in_filter_airport_categery_food_court_is_selected()
        message4 = self.createcampaign.in_filter_airport_categery_gates_is_selected()
        message5 = self.createcampaign.in_filter_airport_categery_loungs_is_selected()
        message6 = self.createcampaign.in_filter_airport_categery_shopping_area_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block") and message3.__contains__("block") and message4.__contains__("block") and message5.__contains__("block") and message6.__contains__("block"))

    def test_in_filter_check_all_products_are_selected_when_deselect_all_product_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_check_all_products_are_selected_when_deselect_all_product_option()
        message=self.createcampaign.in_filter_airport_categery_arrival_hall_is_selected()
        message1 = self.createcampaign.in_filter_airport_categery_baggage_claim_is_selected()
        message2 = self.createcampaign.in_filter_airport_categery_depature_hall_is_selected()
        message3 = self.createcampaign.in_filter_airport_categery_food_court_is_selected()
        message4 = self.createcampaign.in_filter_airport_categery_gates_is_selected()
        message5 = self.createcampaign.in_filter_airport_categery_loungs_is_selected()
        message6 = self.createcampaign.in_filter_airport_categery_shopping_area_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none") and message3.__contains__("none") and message4.__contains__("none") and message5.__contains__("none") and message6.__contains__("none"))

    def test_in_filter_all_products_show_added_items_when_click_airport_categery(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_all_products_show_added_items_when_click_airport_categery()
        message=self.createcampaign.in_filter_airport_categery_arrival_hall_is_displayed()
        message1 = self.createcampaign.in_filter_airport_categery_baggage_claim_is_displayed()
        message2 = self.createcampaign.in_filter_airport_categery_depature_hall_is_displayed()
        message3 = self.createcampaign.in_filter_airport_categery_food_court_is_displyed()
        message4 = self.createcampaign.in_filter_airport_categery_gates_is_displayed()
        message5 = self.createcampaign.in_filter_airport_categery_loungs_is_displayed()
        message6 = self.createcampaign.in_filter_airport_categery_shopping_area_is_displayed()
        assert (message is True and message1 is True and message2 is True and message3 is True and message4 is True and message5 is True and message6 is True)

    def test_in_filter_all_products_show_added_items_when_deselect_all_product_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_all_products_show_added_items_when_deselect_all_product_option()
        message=self.createcampaign.in_filter_airport_categery_arrival_hall_is_displayed()
        message1 = self.createcampaign.in_filter_airport_categery_baggage_claim_is_displayed()
        message2 = self.createcampaign.in_filter_airport_categery_depature_hall_is_displayed()
        message3 = self.createcampaign.in_filter_airport_categery_food_court_is_displyed()
        message4 = self.createcampaign.in_filter_airport_categery_gates_is_displayed()
        message5 = self.createcampaign.in_filter_airport_categery_loungs_is_displayed()
        message6 = self.createcampaign.in_filter_airport_categery_shopping_area_is_displayed()
        assert (message is False and message1 is False and message2 is False and message3 is False and message4 is False and message5 is False and message6 is False)

    def test_in_filter_check_products_show_added_items_when_deselect_some_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_check_products_show_added_items_when_deselect_some_option()
        message = self.createcampaign.in_filter_airport_categery_arrival_hall_is_displayed()
        message1 = self.createcampaign.in_filter_airport_categery_baggage_claim_is_displayed()
        message2 = self.createcampaign.in_filter_airport_categery_depature_hall_is_displayed()
        message3 = self.createcampaign.in_filter_airport_categery_food_court_is_displyed()
        message4 = self.createcampaign.in_filter_airport_categery_gates_is_displayed()
        message5 = self.createcampaign.in_filter_airport_categery_loungs_is_displayed()
        message6 = self.createcampaign.in_filter_airport_categery_shopping_area_is_displayed()
        assert (message is False and message1 is True and message2 is True and message3 is True and message4 is False and message5 is True and message6 is True)

    def test_in_filter_when_click_Buses_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_Buses_to_select_all_sub_categerty()
        message=self.createcampaign.in_filter_buses_categery_bus_is_selected()
        message1 = self.createcampaign.in_filter_buses_categery_bus_terminal_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_bus_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_bus_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_buses_categery_bus_is_selected()
        message1 = self.createcampaign.in_filter_buses_categery_bus_terminal_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_buses_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_buses_to_display_added_items()
        message=self.createcampaign.in_filter_buses_categery_bus_is_displayed()
        message1 = self.createcampaign.in_filter_buses_categery_bus_terminal_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_buses_option_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_buses_option_to_display_added_items()
        message=self.createcampaign.in_filter_buses_categery_bus_is_displayed()
        message1 = self.createcampaign.in_filter_buses_categery_bus_terminal_is_displayed()
        assert (message is False and message1 is True)

    def test_in_filter_when_click_subway_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_subway_to_select_all_sub_categerty()
        message=self.createcampaign.in_filter_subway_categery_platform_is_selected()
        message1 = self.createcampaign.in_filter_subway_categery_subway_train_is_selected()
        message2 = self.createcampaign.in_filter_subway_categery_subway_terminal_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_subway_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_subway_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_subway_categery_platform_is_selected()
        message1 = self.createcampaign.in_filter_subway_categery_subway_train_is_selected()
        message2 = self.createcampaign.in_filter_subway_categery_subway_terminal_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none"))

    def test_in_filter_when_click_subway_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_subway_to_display_added_items()
        message=self.createcampaign.in_filter_subway_categery_platform_is_displayed()
        message1 = self.createcampaign.in_filter_subway_categery_subway_train_is_displayed()
        message2 = self.createcampaign.in_filter_subway_categery_subway_terminal_is_displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_in_filter_when_deselect_subway_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_subway_options_to_display_added_items()
        message = self.createcampaign.in_filter_subway_categery_platform_is_displayed()
        message1 = self.createcampaign.in_filter_subway_categery_subway_train_is_displayed()
        message2 = self.createcampaign.in_filter_subway_categery_subway_terminal_is_displayed()
        assert (message is True and message1 is True and message2 is False)

    def test_in_filter_when_click_train_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_train_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_train_station_categery_train_platform_is_selected()
        message1 = self.createcampaign.in_filter_train_station_categery_train_terminal_is_selected()
        message2 = self.createcampaign.in_filter_train_station_train_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_train_station_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_train_station_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_train_station_categery_train_platform_is_selected()
        message1 = self.createcampaign.in_filter_train_station_categery_train_terminal_is_selected()
        message2 = self.createcampaign.in_filter_train_station_train_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none"))

    def test_in_filter_when_click_train_station_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_train_station_to_display_added_items()
        message = self.createcampaign.in_filter_train_station_categery_train_platform_is_displayed()
        message1 = self.createcampaign.in_filter_train_station_categery_train_terminal_is_displayed()
        message2 = self.createcampaign.in_filter_train_station_train_is_displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_in_filter_when_deselect_train_station_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_train_station_options_to_display_added_items()
        message = self.createcampaign.in_filter_train_station_categery_train_platform_is_displayed()
        message1 = self.createcampaign.in_filter_train_station_categery_train_terminal_is_displayed()
        message2 = self.createcampaign.in_filter_train_station_train_is_displayed()
        assert (message is True and message1 is False and message2 is True)

    def test_in_filter_outdoor_all_categaries_are_selected_when_click_selectAll(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_outdoor_all_categaries_are_selected_when_click_selectAll()
        message = self.createcampaign.in_filter_outdoor_categery_billboard_is_selected()
        message1 = self.createcampaign.in_filter_outdoor_categery_bus_shelter_is_selected()
        message2 = self.createcampaign.in_filter_outdoor_street_structure_is_selected()
        message3 = self.createcampaign.in_filter_outdoor_categery_toll_is_selected()
        message4 = self.createcampaign.in_filter_outdoor_categery_truck_is_selected()
        message5 = self.createcampaign.in_filter_outdoor_urban_panel_is_selected()
        message6 = self.createcampaign.in_filter_outdoor_wallscape_is_selected()

        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block") and message3.__contains__("block") and message4.__contains__("block") and message5.__contains__("block") and message6.__contains__("block"))

    def test_in_filter_outdoor_all_categaries_are_selected_when_deselect_selectAll_option(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_outdoor_all_categaries_are_selected_when_deselect_selectAll_option()
        message = self.createcampaign.in_filter_outdoor_categery_billboard_is_selected()
        message1 = self.createcampaign.in_filter_outdoor_categery_bus_shelter_is_selected()
        message2 = self.createcampaign.in_filter_outdoor_street_structure_is_selected()
        message3 = self.createcampaign.in_filter_outdoor_categery_toll_is_selected()
        message4 = self.createcampaign.in_filter_outdoor_categery_truck_is_selected()
        message5 = self.createcampaign.in_filter_outdoor_urban_panel_is_selected()
        message6 = self.createcampaign.in_filter_outdoor_wallscape_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__( "none") and message3.__contains__("none") and message4.__contains__("none") and message5.__contains__( "none") and message6.__contains__("none"))



    def test_in_filter_when_click_billboards_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_billboards_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_billboard_sub_categery_hignway_is_selected()
        message1 = self.createcampaign.in_filter_billboard_sub_categery_roadeside_is_selected()
        message2 = self.createcampaign.in_filter_billboard_sub_categery_spectucular_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_billboards_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_billboards_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_billboard_sub_categery_hignway_is_selected()
        message1 = self.createcampaign.in_filter_billboard_sub_categery_roadeside_is_selected()
        message2 = self.createcampaign.in_filter_billboard_sub_categery_spectucular_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none"))

    def test_in_filter_when_click_billboards_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_billboards_to_display_added_items()
        message = self.createcampaign.in_filter_billboard_sub_categery_hignway_is_displayed()
        message1 = self.createcampaign.in_filter_billboard_sub_categery_roadeside_is_displayed()
        message2 = self.createcampaign.in_filter_billboard_sub_categery_spectucular_is_displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_in_filter_when_deselect_billboards_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_billboards_options_to_display_added_items()
        message = self.createcampaign.in_filter_billboard_sub_categery_hignway_is_displayed()
        message1 = self.createcampaign.in_filter_billboard_sub_categery_roadeside_is_displayed()
        message2 = self.createcampaign.in_filter_billboard_sub_categery_spectucular_is_displayed()
        assert (message is False and message1 is False and message2 is True)

    def test_in_filter_when_click_street_furniture_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_street_furniture_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_street_furniture_sub_categery_city_clock_is_selected()
        message1 = self.createcampaign.in_filter_street_furniture_sub_categery_city_light_is_selected()
        message2 = self.createcampaign.in_filter_street_furniture_sub_categery_kiosks_is_selected()
        message3 = self.createcampaign.in_filter_street_furniture_sub_categery_outdoot_gym_is_selected()
        message4 = self.createcampaign.in_filter_street_furniture_sub_categery_Street_sign_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block") and message3.__contains__("block") and message4.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_street_furniture_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_street_furniture_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_street_furniture_sub_categery_city_clock_is_selected()
        message1 = self.createcampaign.in_filter_street_furniture_sub_categery_city_light_is_selected()
        message2 = self.createcampaign.in_filter_street_furniture_sub_categery_kiosks_is_selected()
        message3 = self.createcampaign.in_filter_street_furniture_sub_categery_outdoot_gym_is_selected()
        message4 = self.createcampaign.in_filter_street_furniture_sub_categery_Street_sign_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none") and message3.__contains__("none") and message4.__contains__("none"))

    def test_in_filter_when_click_street_furniture_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_street_furniture_to_display_added_items()
        message = self.createcampaign.in_filter_street_furniture_sub_categery_city_clock_is_displayed()
        message1 = self.createcampaign.in_filter_street_furniture_sub_categery_city_light_is_displayed()
        message2 = self.createcampaign.in_filter_street_furniture_sub_categery_kiosks_is_displayed()
        message3 = self.createcampaign.in_filter_street_furniture_sub_categery_outdoot_gym_is_displayed()
        message4 = self.createcampaign.in_filter_street_furniture_sub_categery_Street_sign_is_displayed()
        assert (message is True and message1 is True and message2 is True and message3 is True and message4 is True)

    def test_in_filter_when_deselect_street_furniture_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_street_furniture_options_to_display_added_items()
        message = self.createcampaign.in_filter_street_furniture_sub_categery_city_clock_is_displayed()
        message1 = self.createcampaign.in_filter_street_furniture_sub_categery_city_light_is_displayed()
        message2 = self.createcampaign.in_filter_street_furniture_sub_categery_kiosks_is_displayed()
        message3 = self.createcampaign.in_filter_street_furniture_sub_categery_outdoot_gym_is_displayed()
        message4 = self.createcampaign.in_filter_street_furniture_sub_categery_Street_sign_is_displayed()
        assert (message is True and message1 is False and message2 is False and message3 is True and message4 is True)

    def test_in_filter_when_click_toll_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_toll_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_Toll_sub_categery_cabin_is_selected()
        message1 = self.createcampaign.in_filter_Toll_sub_categery_panel_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_toll_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_toll_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_Toll_sub_categery_cabin_is_selected()
        message1 = self.createcampaign.in_filter_Toll_sub_categery_panel_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_toll_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_toll_to_display_added_items()
        message = self.createcampaign.in_filter_Toll_sub_categery_cabin_is_displayed()
        message1 = self.createcampaign.in_filter_Toll_sub_categery_panel_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_toll_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_toll_options_to_display_added_items()
        message = self.createcampaign.in_filter_Toll_sub_categery_cabin_is_displayed()
        message1 = self.createcampaign.in_filter_Toll_sub_categery_panel_is_displayed()
        assert (message is True and message1 is False)

    def test_in_filter_when_click_point_of_care_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_point_of_care_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_point_of_care_sub_categery_doctor_office_is_selected()
        message1 = self.createcampaign.in_filter_point_of_care_sub_categery_vetenar_office__is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_point_of_care_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_point_of_care_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_point_of_care_sub_categery_doctor_office_is_selected()
        message1 = self.createcampaign.in_filter_point_of_care_sub_categery_vetenar_office__is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_point_of_care_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_point_of_care_to_display_added_items()
        message = self.createcampaign.in_filter_point_of_care_sub_categery_doctor_office_is_displayed()
        message1 = self.createcampaign.in_filter_point_of_care_sub_categery_vetenar_office_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_point_of_care_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_point_of_care_options_to_display_added_items()
        message = self.createcampaign.in_filter_point_of_care_sub_categery_doctor_office_is_displayed()
        message1 = self.createcampaign.in_filter_point_of_care_sub_categery_vetenar_office_is_displayed()
        assert (message is False and message1 is True)


    def test_in_filter_when_click_entertainment_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_entertainment_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_entertainment_sub_categery_bars_is_selected()
        message1 = self.createcampaign.in_filter_entertainment_sub_categery_causal_dining_is_selected()
        message2 = self.createcampaign.in_filter_entertainment_sub_categery_golf_cart_is_selected()
        message3 = self.createcampaign.in_filter_entertainment_sub_categery_hotels_is_selected()
        message4 = self.createcampaign.in_filter_entertainment_sub_categery_movie_theater_is_selected()
        message5 = self.createcampaign.in_filter_entertainment_sub_categery_QSR_is_selected()
        message6 = self.createcampaign.in_filter_entertainment_sub_categery_Recreation_location_is_selected()

        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block") and message3.__contains__("block") and message4.__contains__("block") and message5.__contains__("block") and message6.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_entertainment_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_entertainment_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_entertainment_sub_categery_bars_is_selected()
        message1 = self.createcampaign.in_filter_entertainment_sub_categery_causal_dining_is_selected()
        message2 = self.createcampaign.in_filter_entertainment_sub_categery_golf_cart_is_selected()
        message3 = self.createcampaign.in_filter_entertainment_sub_categery_hotels_is_selected()
        message4 = self.createcampaign.in_filter_entertainment_sub_categery_movie_theater_is_selected()
        message5 = self.createcampaign.in_filter_entertainment_sub_categery_QSR_is_selected()
        message6 = self.createcampaign.in_filter_entertainment_sub_categery_Recreation_location_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none") and message3.__contains__("none") and message4.__contains__("none") and message5.__contains__("none") and message6.__contains__("none"))

    def test_in_filter_when_hotels_toll_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_hotels_toll_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_point_of_hotels_sub_categery_hotels_elevator_is_selected()
        message1 = self.createcampaign.in_filter_hotels_sub_categery_hotels_lobby_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_hotels_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_hotels_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_point_of_hotels_sub_categery_hotels_elevator_is_selected()
        message1 = self.createcampaign.in_filter_hotels_sub_categery_hotels_lobby_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_hotels_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_hotels_to_display_added_items()
        message = self.createcampaign.in_filter_hotels_sub_categery_hotels_elevator_is_displayed()
        message1 = self.createcampaign.in_filter_hotels_sub_categery_hotels_lobby_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_hotels_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_hotels_options_to_display_added_items()
        message = self.createcampaign.in_filter_hotels_sub_categery_hotels_elevator_is_displayed()
        message1 = self.createcampaign.in_filter_hotels_sub_categery_hotels_lobby_is_displayed()
        assert (message is True and message1 is False)

    def test_in_filter_when_movie_theater_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_movie_theater_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_movie_theater_sub_categery_food_court_is_selected()
        message1 = self.createcampaign.in_filter_movie_theater_sub_categery_lobby_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_movie_theater_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_movie_theater_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_movie_theater_sub_categery_food_court_is_selected()
        message1 = self.createcampaign.in_filter_movie_theater_sub_categery_lobby_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_movie_theater_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_movie_theater_to_display_added_items()
        message = self.createcampaign.in_filter_movie_theater_sub_categery_food_court_is_displayed()
        message1 = self.createcampaign.in_filter_movie_theater_sub_categery_lobby_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_movie_theater_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_movie_theater_options_to_display_added_items()
        message = self.createcampaign.in_filter_movie_theater_sub_categery_food_court_is_displayed()
        message1 = self.createcampaign.in_filter_movie_theater_sub_categery_lobby_is_displayed()
        assert (message is True and message1 is False)

    def test_in_filter_when_Recreation_location_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_Recreation_location_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_Recreation_location_sub_categery_concert_venues_is_selected()
        message1 = self.createcampaign.in_filter_Recreation_location_sub_categery_musium_gallery_is_selected()
        message2 = self.createcampaign.in_filter_Recreation_location_sub_categery_theme_park_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_Recreation_location_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_Recreation_location_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_Recreation_location_sub_categery_concert_venues_is_selected()
        message1 = self.createcampaign.in_filter_Recreation_location_sub_categery_musium_gallery_is_selected()
        message2 = self.createcampaign.in_filter_Recreation_location_sub_categery_theme_park_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none"))

    def test_in_filter_when_click_Recreation_location_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_Recreation_location_to_display_added_items()
        message = self.createcampaign.in_filter_Recreation_location_sub_categery_concert_venues_is_displayed()
        message1 = self.createcampaign.in_filter_Recreation_location_sub_categery_musium_gallery_is_displayed()
        message2 = self.createcampaign.in_filter_Recreation_location_sub_categery_theme_park_is_displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_in_filter_when_deselect_Recreation_location_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_Recreation_location_options_to_display_added_items()
        message = self.createcampaign.in_filter_Recreation_location_sub_categery_concert_venues_is_displayed()
        message1 = self.createcampaign.in_filter_Recreation_location_sub_categery_musium_gallery_is_displayed()
        message2 = self.createcampaign.in_filter_Recreation_location_sub_categery_theme_park_is_displayed()
        assert (message is True and message1 is False and message2 is True)

    def test_in_filter_when_sports_ent_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_sports_ent_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_Rsports_ent_sub_categery_club_house_is_selected()
        message1 = self.createcampaign.in_filter_Rsports_ent_sub_categery_sport_arena_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_sports_ent_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_sports_ent_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_Rsports_ent_sub_categery_club_house_is_selected()
        message1 = self.createcampaign.in_filter_Rsports_ent_sub_categery_sport_arena_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_sports_ent_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_sports_ent_to_display_added_items()
        message = self.createcampaign.in_filter_Rsports_ent_sub_categery_club_house_is_displayed()
        message1 = self.createcampaign.in_filter_Rsports_ent_sub_categery_sport_arena_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_sports_ent_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_sports_ent_options_to_display_added_items()
        message = self.createcampaign.in_filter_Rsports_ent_sub_categery_club_house_is_displayed()
        message1 = self.createcampaign.in_filter_Rsports_ent_sub_categery_sport_arena_is_displayed()
        assert (message is False and message1 is True)

    def test_in_filter_when_health_beauty_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_health_beauty_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_health_beauty_sub_categery_gym_is_selected()
        message1 = self.createcampaign.in_filter_health_beauty_sub_categery_salone_is_selected()
        message2 = self.createcampaign.in_filter_health_beauty_sub_categery_spas_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block") and message2.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_health_beauty_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_health_beauty_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_health_beauty_sub_categery_gym_is_selected()
        message1 = self.createcampaign.in_filter_health_beauty_sub_categery_salone_is_selected()
        message2 = self.createcampaign.in_filter_health_beauty_sub_categery_spas_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none") and message2.__contains__("none"))

    def test_in_filter_when_Gym_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_Gym_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_gym_sub_categery_fitness_equipment_is_selected()
        message1 = self.createcampaign.in_filter_gym_sub_categery_lobby_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_gym_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_gym_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_gym_sub_categery_fitness_equipment_is_selected()
        message1 = self.createcampaign.in_filter_gym_sub_categery_lobby_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_gym_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_gym_to_display_added_items()
        message = self.createcampaign.in_filter_gym_sub_categery_fitness_equipment_is_displayed()
        message1 = self.createcampaign.in_filter_gym_sub_categery_lobby_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_gym_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_gym_options_to_display_added_items()
        message = self.createcampaign.in_filter_gym_sub_categery_fitness_equipment_is_displayed()
        message1 = self.createcampaign.in_filter_gym_sub_categery_lobby_is_displayed()
        assert (message is False and message1 is True)

    def test_in_filter_when_apportment_building_to_select_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_apportment_building_to_select_all_sub_categerty()
        message = self.createcampaign.in_filter_apportment_building_categery_elevator_is_selected()
        message1 = self.createcampaign.in_filter_apportment_building_sub_categery_lobby_is_selected()
        assert (message.__contains__("block") and message1.__contains__("block"))

    def test_in_filter_when_desect_all_product_option_in_apportment_building_to_Deselect_all_sub_categerty(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_desect_all_product_option_in_apportment_building_to_Deselect_all_sub_categerty()
        message = self.createcampaign.in_filter_apportment_building_categery_elevator_is_selected()
        message1 = self.createcampaign.in_filter_apportment_building_sub_categery_lobby_is_selected()
        assert (message.__contains__("none") and message1.__contains__("none"))

    def test_in_filter_when_click_apportment_building_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_click_apportment_building_to_display_added_items()
        message = self.createcampaign.in_filter_apportment_building_sub_categery_elevator_is_displayed()
        message1 = self.createcampaign.in_filter_apportment_building_sub_categery_lobby_is_displayed()
        assert (message is True and message1 is True)

    def test_in_filter_when_deselect_apportment_building_options_to_display_added_items(self):
        self.createcampaign = CreateCampaign(self.driver)
        self.test_start_create_campaign()
        self.createcampaign.in_filter_when_deselect_apportment_building_options_to_display_added_items()
        message = self.createcampaign.in_filter_apportment_building_sub_categery_elevator_is_displayed()
        message1 = self.createcampaign.in_filter_apportment_building_sub_categery_lobby_is_displayed()
        assert (message is True and message1 is False)




















































