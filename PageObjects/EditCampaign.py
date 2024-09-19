import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class EditCampaign(BasePage):
    DATE_PICKER= (By.XPATH,"(//input[@placeholder='Campaign Name'])[2]")
    CURRENT_MONTH = (By.XPATH,"(//th[@class='month drp-animate'])[2]")
    NEXT_CALENDER = (By.XPATH, "(//th[@class='next available ng-star-inserted'])[2]")
    SELECT_DATE1 = "(//span[text()='{day}']//parent::td)[3]"
    EDIT_CAMPAIGN_NAME = (By.XPATH,"//input[@id='campaignname']")
    CHECK_BOX_AVAILABLE_INVENTORY = (By.ID,"available-inventory")
    BILLBOARD_NAME_DRAFT = (By.XPATH,"(//tbody[@class='rowtables']/tr/td[2])[2]")
    DELETE_BILLBOARD = (By.XPATH,"(//tbody[@class='rowtables']/tr/td[6])[2]")
    UPDATE_CAMPAIGN = (By.ID,"updateCampaignButton")
    ADD_NEW_BILLBOARD = (By.XPATH,"//button[text()='Add New Billboards']")
    APPLY_BUTTON = (By.ID,"applyButton")
    RESET_BUTTON = (By.XPATH,"//button[text()='Reset']")
    VIEW_LIST_EDIT = (By.XPATH,"//button[text()='View Lists']")
    DIGITAL_LIST = (By.XPATH,"//button[text()=' Digital ']")
    CLASSICAL_LIST = (By.XPATH,"//button[text()=' Classic ']")
    MAP_VIEW = (By.XPATH,"//div[@class='map-container']")
    STREET_MAP_VIEW=(By.XPATH, "//button[@title ='Show street map']")
    STREET_MAP_TERRAIN = (By.XPATH,"//li[contains(@title,'map with terrain')]")
    SATELLITE_VIEW = (By.XPATH,"//button[contains(@title,'Show satellite ')]")
    SATELLITE_VIEW_LABEL = (By.XPATH,"//li[contains(@title,'Show imagery with street names')]")
    FULL_MAP_VIEW = (By.XPATH,"//button[contains(@title,'Toggle fullscreen view')]")
    MAP_ZOOM_IN =(By.XPATH,"//button[contains(@title,'Zoom in')]")
    MAP_ZOOM_OUT = (By.XPATH,"//button[contains(@title,'Zoom out')]")
    MIN_PRICE_BOX = (By.ID,"minValue")
    MAX_PRICE_BOX =(By.ID,"maxValue")
    BILLBOAD_LOCATION = (By.XPATH,"//area[@title='Queen Victoria Market']")
    IMAGE_IN_MAP = (By.XPATH,"//img[@class='map-thumbnail']")





    def __init__(self, driver):
        super().__init__(driver)

    def open_date_picker(self):
        self.click_button(self.DATE_PICKER)
        time.sleep(3)

    def get_current_month_year(self):
        month_year_text = self.get_text(self.CURRENT_MONTH)
        return month_year_text

    def navigate_to_month(self, target_month, target_year):
        month_mapping = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
            'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
            'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        reverse_month_mapping = {v: k for k, v in month_mapping.items()}

        target_year = int(target_year)
        target_month_num = month_mapping[target_month]

        while True:
            current_month_year = self.get_current_month_year()
            current_month_str, current_year_str = current_month_year.split()
            current_year = int(current_year_str)
            current_month = month_mapping[current_month_str]

            if current_year == target_year and current_month == target_month_num:
                break
            elif current_year > target_year or (current_year == target_year and current_month > target_month_num):
                self.click_button(self.NEXT_CALENDER)
            else:
                self.click_button(self.NEXT_CALENDER)

    def select_date1(self, day):
        date_locator1 = (By.XPATH, self.SELECT_DATE1.format(day=day))

        self.click_button(date_locator1)

    def add_new_billboard_option_displaed(self):
        return self.is_displayed(self.ADD_NEW_BILLBOARD)

    def add_new_billboard_option_clickable(self):
        return self.clickable(self.ADD_NEW_BILLBOARD)

    def check_box_available_inventory_is_displaed(self):
        return self.is_displayed(self.CHECK_BOX_AVAILABLE_INVENTORY)

    def check_box_available_inventory_is_Clickale(self):
        return self.clickable(self.CHECK_BOX_AVAILABLE_INVENTORY)

    def update_campaign_option_is_displayed(self):
        self.scroll_into_view(self.UPDATE_CAMPAIGN)
        return self.is_displayed(self.UPDATE_CAMPAIGN)

    def update_campaign_option_is_clickable(self):
        self.scroll_into_view(self.UPDATE_CAMPAIGN)
        return self.clickable(self.UPDATE_CAMPAIGN)

    def map_is_displaed(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.MAP_VIEW)

    def street_map_option_is_displaed(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.STREET_MAP_VIEW)

    def street_map_option_is_clickable(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.clickable(self.STREET_MAP_VIEW)

    def street_map_terrain_option_displaed(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.STREET_MAP_VIEW)
        return self.is_displayed(self.STREET_MAP_TERRAIN)

    def street_map_terrain_option_clickable(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.STREET_MAP_VIEW)
        return self.clickable(self.STREET_MAP_TERRAIN)

    def street_map_terrain_option_click_operation(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.STREET_MAP_VIEW)
        self.click_button(self.STREET_MAP_TERRAIN)

    def sattelite_map_option_is_displaed(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.SATELLITE_VIEW)

    def sattelite_map_option_is_clickable(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.clickable(self.SATELLITE_VIEW)

    def sattelite_map_label_option_displaed(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.SATELLITE_VIEW)
        return self.is_displayed(self.SATELLITE_VIEW_LABEL)

    def sattelite_map_label_option_clickable(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.SATELLITE_VIEW)
        return self.clickable(self.SATELLITE_VIEW_LABEL)

    def sattelite_map_label_option_click_operation(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.SATELLITE_VIEW)
        self.click_button(self.SATELLITE_VIEW_LABEL)

    def full_map_view_option_displayed(self):
        return self.is_displayed(self.FULL_MAP_VIEW)

    def full_map_view_option_clickable(self):
        return self.clickable(self.FULL_MAP_VIEW)

    def full_map_view_option_click_operation(self):
        self.click_button(self.FULL_MAP_VIEW)
        self.press_escape_key()


    def zoom_in_option_is_displaed_in_map(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.MAP_ZOOM_IN)

    def zoom_in_option_is_clickable_in_map(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.clickable(self.MAP_ZOOM_IN)

    def zoom_in_oprion_click_operation(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.MAP_ZOOM_IN)

    def zoom_out_option_is_displaed_in_map(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.MAP_ZOOM_OUT)

    def zoom_out_option_is_clickable_in_map(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.clickable(self.MAP_ZOOM_OUT)

    def zoom_out_oprion_click_operation(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.MAP_ZOOM_OUT)

    def billboard_location_displayed_in_map(self):
        # self.scroll_into_view(self.BILLBOAD_LOCATION)
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.BILLBOAD_LOCATION)

    def billboard_location_clickable_in_map(self):
        time.sleep(5)
        self.scroll_to_bottom()
        return self.clickable(self.BILLBOAD_LOCATION)

    def billboard_is_displaed_when_click_bill_location(self):
        time.sleep(5)
        self.scroll_to_bottom()
        self.click_button(self.BILLBOAD_LOCATION)
        time.sleep(2)
        # return self.is_displayed(self.IMAGE_IN_MAP)

    def delete_billboard_option_displaed(self):
        return self.is_displayed(self.DELETE_BILLBOARD)

