import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.ContentHub import ContentHub
from PageObjects.CreateCampaign import CreateCampaign
from PageObjects.EditCampaign import EditCampaign


class MyOrderPage(BasePage):

    MY_PROFILE_BUTTON= (By.ID, "navbarDropdown3")
    MY_ACCOUNT = (By.XPATH,"//label[text()=' My Account']")
    MY_CAMPAIGN = (By.XPATH,"//label[text()='My Campaigns ']")
    MY_CART = (By.XPATH, "//label[contains(text(),'My Cart (0) ')]")
    CONTENT_HUB = (By.XPATH,"//label[text()='Content Hub ']")
    LOGOUT=(By.XPATH,"//label[text()='Log out']")
    SORT_BY_ORDERS = (By.XPATH,"//select[@name='currency']")
    CAMPAIGN_NAME =(By.XPATH,"(//tbody[3]/tr/td)[1]")
    CAMPAIGN_STATUS = (By.XPATH,"(//tbody[3]/tr/td)[6]")
    BOOKING_VIEWS = (By.XPATH,"(//tbody[3]/tr/td)[9]")
    ACTION = (By.XPATH,"(//tbody[3]/tr/td)[10]")
    NEW_CAMPAIGN=(By.XPATH, "//button[text()='New Campaign']")
    SEARCH_BAR = (By.XPATH,"//input[@type='text']")
    RESET_SEARCH = (By.XPATH, "//i[@class='fa fa-refresh refresh-icon-right ng-star-inserted']")
    MAP_VIEW= (By.XPATH,"//li[text()=' Map ']")
    GALLERY_VIEW = (By.XPATH, "//li[text()=' Gallery ']")
    CLOSE_BUTTON = (By.XPATH , "//button[text()='Close']")
    MAP = (By.XPATH ,"//img[@crossorigin='Anonymous']")
    GALLERY = (By.XPATH ,"//div[@class='gallery-thumbnail']")


    def __init__(self, driver):
        super().__init__(driver)

    def my_profile_option_displayed(self):
        return self.is_displayed(self.MY_PROFILE_BUTTON)

    def my_prfile_option_clickable(self):
        return self.clickable(self.MY_PROFILE_BUTTON)

    def my_account_option_displayed(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.is_displayed(self.MY_ACCOUNT)

    def my_account_option_clickable(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.clickable(self.MY_ACCOUNT)

    def my_campaign_option_displayed(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.is_displayed(self.MY_CAMPAIGN)

    def my_campaign_option_clickable(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.clickable(self.MY_CAMPAIGN)

    def my_cart_option_displayed(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.is_displayed(self.MY_CART)

    def my_cart_option_clickable(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.clickable(self.MY_CART)

    def content_hub_option_displayed(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.is_displayed(self.CONTENT_HUB)

    def content_hub_option_clickable(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.clickable(self.CONTENT_HUB)

    def content_hub_option_click_operation(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        self.click_button(self.CONTENT_HUB)
        return ContentHub(self.driver)

    def logout_option_is_displayed(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.is_displayed(self.LOGOUT)

    def logout_option_is_clickable(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        return self.clickable(self.LOGOUT)

    def booking_view_option_displayed(self):
        return self.is_displayed(self.BOOKING_VIEWS)

    def booking_view_option_is_clickable(self):
        return self.clickable(self.BOOKING_VIEWS)

    def action_option_displayed(self):
        return self.is_displayed(self.ACTION)

    def action_option_clickable(self):
        return self.clickable(self.ACTION)

    def action_option_operation(self):
        self.click_button(self.ACTION)
        time.sleep(5)
        return EditCampaign(self.driver)


    def new_campaign_option_displayed(self):
        return self.is_displayed(self.NEW_CAMPAIGN)

    def new_campaign_option_clickable(self):
        return self.clickable(self.NEW_CAMPAIGN)

    def new_campaign_click_operation(self):
        self.click_button(self.NEW_CAMPAIGN)
        return CreateCampaign(self.driver)

    def logout_operation(self):
        self.click_button(self.MY_PROFILE_BUTTON)
        self.click_button(self.LOGOUT)
        time.sleep(5)
        return  self.get_current_url()

    def search_campaign(self,campaignname):
        self.text_inputs(self.SEARCH_BAR,campaignname)
        self.press_enter()
        return self.get_text(self.CAMPAIGN_NAME)

    def reset_search_campaign(self,campaignname):
        self.text_inputs(self.SEARCH_BAR, campaignname)
        self.press_enter()
        self.click_button(self.RESET_SEARCH)
        time.sleep(3)
        return self.get_text(self.SEARCH_BAR)

    def sort_by_draft(self,value):
        self.select_dropdown_option_by_value(self.SORT_BY_ORDERS,value)
        time.sleep(3)
        return self.get_text(self.CAMPAIGN_STATUS)

    def sort_by_Request(self,value):
        self.select_dropdown_option_by_value(self.SORT_BY_ORDERS,value)
        time.sleep(3)
        return self.get_text(self.CAMPAIGN_STATUS)

    def booking_view_option_open(self):
        self.click_button(self.BOOKING_VIEWS)
        return self.is_displayed(self.MAP_VIEW)

    def is_mapview_displayed_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        return self.is_displayed(self.MAP_VIEW)

    def is_gallery_view_displayed_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        return self.is_displayed(self.GALLERY_VIEW)

    def is_mapview_clickable_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        return self.clickable(self.MAP_VIEW)

    def is_gallery_view_clickable_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        return self.clickable(self.GALLERY_VIEW)

    def map_is_diplayed_in_mapView(self):
        self.click_button(self.BOOKING_VIEWS)
        time.sleep(5)
        return self.is_displayed(self.MAP)

    def gallery_is_diplayed_in_galleryView(self):
        self.click_button(self.BOOKING_VIEWS)
        self.click_button(self.GALLERY_VIEW)
        time.sleep(5)
        return self.is_displayed(self.GALLERY)

    def close_button_is_displayed_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        self.scroll_into_view(self.CLOSE_BUTTON)
        return self.is_displayed(self.CLOSE_BUTTON)

    def close_button_is_Clickable_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        self.scroll_into_view(self.CLOSE_BUTTON)
        return self.clickable(self.CLOSE_BUTTON)

    def perform_close_button_in_views(self):
        self.click_button(self.BOOKING_VIEWS)
        self.scroll_into_view(self.CLOSE_BUTTON)
        self.click_button(self.CLOSE_BUTTON)
        time.sleep(5)














