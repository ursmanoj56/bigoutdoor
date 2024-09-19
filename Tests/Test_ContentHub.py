from PageObjects.ContentHub import ContentHub
from PageObjects.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestContentHub(BaseTest):
    def test_upload_button_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub=myorderpage.content_hub_option_click_operation()
        message = contenthub.upload_button_is_displayed()
        assert message is True

    def test_upload_button_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub=myorderpage.content_hub_option_click_operation()
        message = contenthub.upload_button_clickable()
        assert message is True

    def test_back_button_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub=myorderpage.content_hub_option_click_operation()
        message = contenthub.back_button_is_displayed()
        assert message is True

    def test_back_button_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub=myorderpage.content_hub_option_click_operation()
        message = contenthub.back_button_is_clickable()
        assert message is True

    def test_back_button_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.back_button_click_operation()
        assert message.__contains__("https://test-bigoutdoor.lmx.ai/page")

    def test_search_bar_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.search_bar_is_displayed()
        assert message is True

    def test_search_bar_is_enterable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.search_bar_is_enterable("manoj")

    def test_validate_search_items(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.validate_search_item("1606.jpg")
        assert message.__contains__("1606.jpg")

    def test_filter_option_is_diaplayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.filter_option_is_displayed()
        assert message is True

    def test_filter_option_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.filter_option_clickable()
        assert message is True

    def test_resolution_width_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.resolution_width_option_displayed()
        assert message is True

    def test_resolution_height_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.resolution_height_option_displayed()
        assert message is True

    def test_resolution_width_option_enterable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.resolution_width_option_enterable(234)


    def test_resolution_height_option_enterable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.resolution_height_option_enterable(432)

    def test_png_image_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.png_image_option_displayed()
        assert message is True

    def test_jpeg_image_option_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.jpeg_image_option_displayed()
        assert message is True

    def test_video_option_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message= contenthub.video_option_is_displayed()
        assert message is True

    def test_png_image_option_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.png_image_option_clickable()
        assert message is True

    def test_jpeg_image_option_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.jpeg_image_option_clickable()
        assert message is True

    def test_video_option_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.video_option_is_clickable()
        assert message is True

    def test_close_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.close_button_is_displayed()
        assert message is True

    def test_apply_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.apply_button_is_displayed()
        assert message is True

    def test_close_button_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.close_button_is_clickable()
        assert message is True

    def test_apply_button_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.apply_button_is_clickable()
        assert message is True

    def test_next_page_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.next_page_is_displayed()
        assert message is True

    def test_previous_page_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.previous_page_is_displayed()
        assert message is True

    def test_next_page_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.next_page_is_clickable()
        assert message is True

    def test_previous_page_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.previous_page_is_clickable()
        assert message is True

    def test_next_page_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.next_page_click_operation()


    def test_prevoius_page_click_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.prevoius_page_click_operation()

    def test_go_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.go_button_is_displayed()
        assert message is True

    def test_go_button_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.go_button_is_clickable()
        assert message is True

    def test_performance_of_input_go_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.performance_of_input_go_operation(2)

    def test_filter_by_jpeg_image(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.filter_by_jpeg_image()
        assert message.__contains__("Image/jpeg")

    def test_filter_by_png_image(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.filter_by_png_image()
        assert message.__contains__("Image/png")

    def test_filter_by_mp4_video(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.filter_by_mp4_video()
        assert message.__contains__("Video/mp4")

    def test_thubnails_is_displayed_in_table(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.thubnails_is_displayed_in_table()
        assert message is True

    def test_creative_name_is_displayed_in_table(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.creative_name_is_displayed_in_table()
        assert message is True

    def test_creative_type_displayed_in_table(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.creative_type_displayed_in_table()
        assert message is True

    def test_resolution_is_displayed_in_table(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.resolution_is_displayed_in_table()
        assert message is True

    def test_delete_option_is_displayed_in_table(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.delete_option_is_displayed_in_table()
        assert message is True

    def test_filter_by_resolution(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.filter_by_resolution(1920,1080)
        assert message.__contains__("1920x1080")

    def test_reset_filter_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.reset_filter_is_displayed()
        assert message is True

    def test_reset_filter_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.reset_filter_is_clickable()
        assert message is True

    def test_reset_filter_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.reset_filter_operation()

    def test_close_button_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.close_button_operation()
        assert message is False

    def test_no_option_in_delete_creatives_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.no_option_in_delete_creatives_is_displayed()
        assert message is True

    def test_yes_option_in_delete_creatives_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.yes_option_in_delete_creatives_is_displayed()
        assert message is True

    def test_no_option_in_delete_creatives_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.no_option_in_delete_creatives_is_clickable()
        assert message is True

    def test_yes_option_in_delete_creatives_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.yes_option_in_delete_creatives_is_clickable()
        assert message is True

    def test_no_option_in_delete_creatives_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.no_option_in_delete_creatives_operation()

    def test_yes_option_in_delete_creatives_operation(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.yes_option_in_delete_creatives_operation()
        assert (message !="pngegg.png")

    def test_upload_file_button_is_displayed(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.upload_file_button_is_displayed()
        assert message is True

    def test_upload_file_button_is_clickable(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        message = contenthub.upload_file_button_is_clickable()
        assert message is True

    def test_upload_file(self):
        self.loginpage = LoginPage(self.driver)
        myorderpage = self.loginpage.login_with_valid_credential("surrendar_bigoutdoor", "Test123")
        contenthub = myorderpage.content_hub_option_click_operation()
        contenthub.validate_upload_file(r"C:\Users\HP\PycharmProjects\SS0\TestFiles\pngegg.png")
        # assert message.__contains__("pngegg.png")














