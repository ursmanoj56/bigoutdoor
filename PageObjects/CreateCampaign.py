import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.EditCampaign import EditCampaign


class CreateCampaign(BasePage):
    ENTER_CAMPAIGN_NAME = (By.XPATH,"//input[@formcontrolname='campaigname']")
    CLICK_DATE = (By.XPATH,"//input[@formcontrolname='campaigndate']")
    CURRENT_MONTH1 = (By.XPATH,"//th[@class='month drp-animate']")
    NEXT_CALENDER1 = (By.XPATH,"//th[@class='month']//following::th[1]")
    SELECT_DATE2_TEMPLATE= (By.XPATH,"(//span[text()='21']//parent::td)[1]")
    SELECT_DATE2 = "(//span[text()='{day}']//parent::td)[1]"
    NEXT_BUTTON = (By.XPATH,"//button[text()='Next']")
    DIGITAL_BILLBOARD = (By.XPATH,"//button[text()=' Digital ']")
    CLASSIC_BILLBOARD = (By.XPATH ,"//button[text()=' Classic ']")
    MAP_VIEW_OPTION= (By.XPATH,"//div[contains(@class ,'d-flex filterimag-1')]/div[1]")
    LIST_VIEW= (By.XPATH,"//div[contains(@class ,'d-flex filterimag-1')]/div[2]")
    APPLY_BUTTON = (By.ID,"applyButton")
    RESET_BUTTON = (By.XPATH,"//button[text()='Reset']")
    AVAILABLE_INVENTORY =(By.ID,"available-inventory")
    EDIT_CAMPAIGN_NAME=(By.ID,"campaignname")

    DATE_PICKER = (By.XPATH, "(//input[@placeholder='Campaign Name'])[2]")
    CURRENT_MONTH = (By.XPATH, "(//th[@class='month drp-animate'])[2]")
    NEXT_CALENDER = (By.XPATH, "(//th[@class='next available ng-star-inserted'])[2]")
    SELECT_DATE1 = "(//span[text()='{day}']//parent::td)[3]"
    TOAST_MESSAGE = (By.XPATH,"//div[@role='alertdialog']")
    BILLBOARD_VIEW =(By.XPATH,"(//button[@title='View'])[1]")
    VALIDATE_CLASSIC = (By.XPATH,"//div[text()=' Classic Billboard']")
    VALIDATE_DIGITAL =(By.XPATH,"//div[text()=' Digital Billboard']")
    FIRST_BILLBOARD = (By.XPATH,"(//img[@class='billboard-thumbnail'])[1]")
    MAP_VIEW= (By.XPATH,"//div[@class='map-container']")
    SEARCH_BILLBOARD= (By.ID,"searchbillboards")
    FIRST_BILLBOARD_NAME= (By.XPATH,"(//div[@class='list-img-head']/div)[1]")
    MIN_PRICE = (By.ID,"minValue")
    MAX_PRICE = (By.ID,"maxValue")
    FIRST_BILLBOARD_PRICE =(By.XPATH,"(//div[@class='site-content']/span)[2]")

    STREET_MAP_VIEW = (By.XPATH, "//button[@title ='Show street map']")
    STREET_MAP_TERRAIN = (By.XPATH, "//li[contains(@title,'map with terrain')]")
    SATELLITE_VIEW = (By.XPATH, "//button[contains(@title,'Show satellite ')]")
    SATELLITE_VIEW_LABEL = (By.XPATH, "//li[contains(@title,'Show imagery with street names')]")
    FULL_MAP_VIEW = (By.XPATH, "//button[contains(@title,'Toggle fullscreen view')]")
    MAP_ZOOM_IN = (By.XPATH, "//button[contains(@title,'Zoom in')]")
    MAP_ZOOM_OUT = (By.XPATH, "//button[contains(@title,'Zoom out')]")
    BILLBOARD_LOCATION=(By.XPATH,"(//div[@role='button'])[5]")
    BILLBOARD_IMAGE_IN_MAP = (By.XPATH,"(//div[@class='map-title'])[1]//preceding::img[1]")
    BILLBOARD_NAME_IN_MAP = (By.XPATH,"(//div[@class='map-title'])[1]")
    BILLBOARD_DETAILS = (By.XPATH,"//div[@class='modal-content']")
    INDOOR_CHECKBOX=(By.XPATH,"(//span[contains(@class,'checkbox-venue')])[1]")
    OUTDOOR_CHECKBOX = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[2]")
    DIGITAL = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[3]")
    SMALL_SCREEN_CHECKBOX = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[4]")
    MEDIUM_SCREEN_CHECKBOX = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[5]")
    LARGE_SCREEN_CHECKBOX = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[6]")
    EXTRA_LARGR_SCREEN_CHECKBOX = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[7]")
    LED_TYPE= (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[8]")
    PORTRAIT_TYPE = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[9]")
    FACADE_TYPE = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[10]")
    STANDEE_TYPE = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[11]")
    UNIPOLE_TYPE = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[12]")
    POLLAR_TYPE = (By.XPATH, "(//span[contains(@class,'checkbox-venue')])[13]")
    SELECT_ALL_SUB=(By.XPATH,"(//span[@class='checkmark-checkbox'])[1]")
    BANKS=(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[2]")
    AIRPORTS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    BUSES = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    SUBWAY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    TAXI_RIDE_SHARE_TOP = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    TAXI_RIDE_SHARE_TV = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[6]")
    TRAIN_STATION = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[7]")
    BILLBOARDS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    BUS_SHELTER = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    STREET_FURNITURE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    TOLL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    TRUCK = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[6]")
    URBAN_PANEL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[7]")
    DOCTORS_OFFICE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    VETERNERY_OFFICE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    BARS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    CASUAL_DINING = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    GOLF_CART = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    HOTEL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    MOVIE_THEATER = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[6]")
    QSP = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[7]")
    RECREATIONAL_LOCATION = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[8]")
    SPORTS_ENT = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[9]")
    GYM = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    SALONS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    SPAS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    APARTMENT_BULDING = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    DMVS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    MILATORY_BASES = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    OFFICE_BULDING = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    CONVENCIES_STORE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    DISPENSARIES = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    GAS_STATION = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    GROCERY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    LIQUIOR_STORE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[6]")
    MALL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[7]")
    PARKING_GARAGES = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[8]")
    PHARMACIES = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[9]")
    COLLEGE_UNIVERSITY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[2]")
    SCHOOLS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    FILTER_OPTION = (By.XPATH,"(//div[contains(@class,'filterimag-1')])[1]//child::img")
    FINACIAL_OPTION= (By.XPATH,"//span[text()='Financial']")
    SELECT_ALL_PRODUCTS_FINANCIAL = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[3]")
    ATM = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    ATM123 = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    FINANCIAL_ADDED=(By.XPATH,"//div[text()=' Financial ']")
    BANKS_ADDED = (By.XPATH, "//div[text()=' Banks ']")
    ATM_ADDED = (By.XPATH, "//div[text()=' ATM ']")
    ATM123_ADDED = (By.XPATH, "//div[text()=' atm123 ']")
    SELECT_APP_AIRPORT=(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[8]")
    ARRIVAL_HALL=(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[9]")
    BAGGAGE_CLAIM = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[10]")
    DEPARTMENT_HALL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    FOOD_COURT = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[12]")
    GATE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[13]")
    LOUNGES = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[14]")
    SHOPPING_AREA = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[15]")
    ARRIVAL_HALL_ADDED = (By.XPATH, "//div[text()=' Arrival Hall ']")
    BAGGAGE_CLAIM_ADDED = (By.XPATH, "//div[text()=' Baggage Claim ']")
    DEPARTMENT_HALL_ADDED = (By.XPATH, "//div[text()=' Departures Hall ']")
    FOOD_COURT_ADDED = (By.XPATH, "//div[text()=' Food Court ']")
    GATE_ADDED = (By.XPATH, "//div[text()=' Gates ']")
    LOUNGES_ADDED = (By.XPATH, "//div[text()=' Lounges ']")
    SHOPPING_AREA_ADDED = (By.XPATH, "//div[text()=' Shopping Area ']")
    TRANSIT_ADDED = (By.XPATH, "//div[text()=' Transit ']")
    AIRPORT_ADDED = (By.XPATH, "//div[text()=' Airports ']")
    TRANSIT_OPTION=(By.XPATH,"//span[text()='Transit']")
    SELECT_ALL_BUS_PRODUCTS =(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[8]")
    BUS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[9]")
    BUS_TERMINAL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[10]")
    BUS_ADDED= (By.XPATH,"//div[text()=' Bus ']")
    BUS_TERMINAL_ADDED = (By.XPATH,"//div[text()=' Terminal ']")
    SELECT_ALL_TRANSIT_PRODUCTS = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[8]")
    PLATFORM = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[9]")
    SUBWAY_TRAIN = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[10]")
    SUBWAY_TERMINAL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    PLATFORM_ADDED =(By.XPATH,"//div[text()=' Platform ']")
    SUBWAY_TRAIN_ADDED = (By.XPATH, "//div[text()=' Subway Train ']")
    SUBWAY_TERMINAL_ADDED = (By.XPATH, "//div[text()=' Terminal ']")
    TRAIN_PLATFORM = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[9]")
    TRAIN_TERMINAL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[10]")
    TRAIN = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    TRAIN_PLATFORM_ADDED = (By.XPATH, "//div[text()=' Platform ']")
    TRAIN_TERMINAL_ADDED = (By.XPATH, "//div[text()=' Terminal ']")
    TRAIN_ADDED = (By.XPATH, "//div[text()=' Train ']")
    OUT_DOOR_BILLBOARDS =(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[2]")
    OUT_DOOR_BUS_SHELTER = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[3]")
    OUT_DOOR_STREET_FUNITURE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    OUT_DOOR_TOLL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    OUT_DOOR_TRUCK = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[6]")
    OUT_DOOR_URBAN_PANEL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[7]")
    OUT_DOOR_WALLSCAPE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[8]")
    OUTDOOR_OPTION = (By.XPATH,"//span[text()='Outdoor']")
    SELECT_ALL_OUTDOOR=(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[9]")
    HIGHWAY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[10]")
    ROAD_SIDE = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    SPECTUCAL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[12]")
    HIGHWAY_ADDED = (By.XPATH,"//div[text()=' Highway ']")
    ROAD_SIDE_ADDED = (By.XPATH, "//div[text()=' Roadside ']")
    SPECTUCAL_ADDED = (By.XPATH, "//div[text()=' Spectacular ']")
    CITY_CLOCKS= (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[10]")
    CITY_LIGHT = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    KIOSKS = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[12]")
    OUTDOOR_gym = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[13]")
    STREET_SIGN = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[14]")
    CITY_CLOCKS_ADDED = (By.XPATH, "//div[text()=' City Clocks ']")
    CITY_LIGHT_ADDED = (By.XPATH, "//div[text()=' CityLights ']")
    KIOSKS_ADDED = (By.XPATH, "//div[text()=' Kiosks ']")
    OUTDOOR_gym_ADDED = (By.XPATH, "//div[text()=' Outdoor Gym ']")
    STREET_SIGN_ADDED = (By.XPATH, "//div[text()=' Street Sign ']")
    CABIN = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[10]")
    PANEL = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    CABIN_ADDED = (By.XPATH, "//div[text()=' Cabin ']")
    PANEL_ADDED = (By.XPATH, "//div[text()=' Panel ']")
    POINT_OF_CARE_OPTION = (By.XPATH,"//span[text()='Point of Care']")
    DOCTORS_OFFICE_ADDED= (By.XPATH,"//div[text()=' Doctor’s Offices ']")
    VETERNERY_OFFICE_ADDED = (By.XPATH,"//div[text()=' Veterinary Offices ']")
    ENTERTAINMENT_OPTION = (By.XPATH,"//span[text()='Entertainment']")
    SELECT_ALL_ENTERMENT=(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[10]")
    HOTELS_ELEVATOR = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[11]")
    HOTELS_LOBBY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[12]")
    HOTELS_ELEVATOR_ADDED = (By.XPATH, "//div[text()=' Elevator ']")
    HOTELS_LOBBY_ADDED = (By.XPATH, "//div[text()=' Lobby ']")
    FOOD_COURT_THEATER = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[11]")
    THEATER_LOBBY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[12]")
    FOOD_COURT_THEATER_ADDED = (By.XPATH, "//div[text()=' Food Court ']")
    THEATER_LOBBY_ADDED = (By.XPATH, "//div[text()=' Lobby ']")
    CONCERT_VENUES =(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[11]")
    MUSEUM_GALLERY = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[12]")
    THEME_PART =(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[13]")
    CONCERT_VENUES_ADDED = (By.XPATH, "//div[text()=' Concert Venues ']")
    MUSEUM_GALLERY_ADDED = (By.XPATH, "//div[text()=' Museums and Galleries ']")
    THEME_PART_ADDED = (By.XPATH, "//div[text()=' Theme Parks ']")
    CLUB_HOUSE =(By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[11]")
    SPORT_ARENA = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[12]")
    CLUB_HOUSE_ADDED = (By.XPATH, "//div[text()=' Club House ']")
    SPORT_ARENA_ADDED = (By.XPATH, "//div[text()=' Sport Arena ']")
    HEATH_BEAUTY = (By.XPATH,"//span[text()='Health & Beauty']")
    SELECT_ALL_HEALTH_BEAUTY= (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[5]")
    FITNESS_EQUIPMENT = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[6]")
    HEALTH_LOBBY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[7]")
    FITNESS_EQUIPMENT_ADDED = (By.XPATH, "//div[text()=' Fitness Equipment ']")
    HEALTH_LOBBY_ADDED = (By.XPATH, "//div[text()=' Lobby ']")
    SELECT_ALL_RESIDENTIAL = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[3]")
    RESIDENTIAL_ELEVATOR = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[4]")
    RESIDENTIAL_LOBBY = (By.XPATH, "(//span[contains(@class,'checkmark-checkbox')])[5]")
    RESIDENTIAL_ELEVATOR_ADDED = (By.XPATH, "//div[text()=' Elevator ']")
    RESIDENTIAL_LOBBY_ADDED = (By.XPATH, "//div[text()=' Lobby ']")
    RESIDENTIAL_OPTION = (By.XPATH,"//span[text()='Residential']")
    APPORTMENT_BUILDING = (By.XPATH,"(//span[contains(@class,'checkmark-checkbox')])[2]")






    





    def __init__(self, driver):
        super().__init__(driver)

    def open_date_picker2(self):
        self.click_button(self.CLICK_DATE)
        time.sleep(3)

    def get_current_month_year2(self):
        month_year_text = self.get_text(self.CURRENT_MONTH1)
        return month_year_text

    def navigate_to_month2(self, target_month, target_year):
        month_mapping = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
            'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
            'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        reverse_month_mapping = {v: k for k, v in month_mapping.items()}

        target_year = int(target_year)
        target_month_num = month_mapping[target_month]

        while True:
            current_month_year = self.get_current_month_year2()
            current_month_str, current_year_str = current_month_year.split()
            current_year = int(current_year_str)
            current_month = month_mapping[current_month_str]

            if current_year == target_year and current_month == target_month_num:
                break
            elif current_year > target_year or (current_year == target_year and current_month > target_month_num):
                self.click_button(self.NEXT_CALENDER1)
            else:
                self.click_button(self.NEXT_CALENDER1)

    def select_date2(self,day):
        date_locator1 = (By.XPATH, self.SELECT_DATE2.format(day=day))

        self.click_button(date_locator1)

    def click_next_calender(self):
        self.scroll_to_bottom()
        self.click_button(self.NEXT_CALENDER1)

    def select_date(self):
        self.click_button(self.SELECT_DATE2_TEMPLATE)

    def create_campaign(self, name):
        self.text_inputs(self.ENTER_CAMPAIGN_NAME,name)

    def click_next_button_is_displayed(self):
        return self.is_displayed(self.NEXT_BUTTON)

    def click_next_button_is_clickable(self):
        return self.clickable(self.NEXT_BUTTON)

    def validate_error_messge_when_click_button_without_field(self):
        self.click_button(self.NEXT_BUTTON)
        return self.get_text(self.TOAST_MESSAGE)

    def clik_next_operation(self):
        self.click_button(self.NEXT_BUTTON)
        time.sleep(5)

    def edit_campaign_name(self,name):
        self.text_inputs(self.EDIT_CAMPAIGN_NAME,name)

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

    def is_digible_billboard_option_dispalyed(self):
        return self.is_displayed(self.DIGITAL_BILLBOARD)

    def is_digital_billboard_option_clickable(self):
        return self.clickable(self.DIGITAL_BILLBOARD)

    def is_classic_billboard_option_dispalyed(self):
        return self.is_displayed(self.CLASSIC_BILLBOARD)

    def is_classic_billboard_option_clickable(self):
        return self.clickable(self.CLASSIC_BILLBOARD)

    def is_map_view_is_dispaled(self):
        return self.is_displayed(self.MAP_VIEW_OPTION)

    def is_map_view_clickable(self):
        return self.clickable(self.MAP_VIEW_OPTION)

    def is_list_view_displaed(self):
        return self.is_displayed(self.LIST_VIEW)

    def is_list_view_clickble(self):
        return self.clickable(self.LIST_VIEW)

    def is_available_inventory_option_displayed(self):
        return self.is_displayed(self.AVAILABLE_INVENTORY)

    def is_availale_inventory_option_clickable(self):
        return self.clickable(self.AVAILABLE_INVENTORY)

    def is_availale_inventory_option_click_operaion(self):
        return self.click_button(self.AVAILABLE_INVENTORY)

    def is_billboard_view_option_clickable(self):
        self.move_to_element(self.FIRST_BILLBOARD)
        time.sleep(2)
        self.scroll_into_view(self.BILLBOARD_VIEW)
        return self.clickable(self.BILLBOARD_VIEW)

    def validate_classic_when_click_classic_billboard_option(self):
        self.click_button(self.CLASSIC_BILLBOARD)
        self.move_to_element(self.FIRST_BILLBOARD)
        time.sleep(2)
        self.scroll_into_view(self.BILLBOARD_VIEW)
        self.click_button(self.BILLBOARD_VIEW)
        return self.get_text(self.VALIDATE_CLASSIC)

    def validate_digital_when_click_digital_billboard_option(self):
        self.move_to_element(self.FIRST_BILLBOARD)
        time.sleep(2)
        self.scroll_into_view(self.BILLBOARD_VIEW)
        self.click_button(self.BILLBOARD_VIEW)
        return self.get_text(self.VALIDATE_DIGITAL)

    def validate_when_click_mapview_to_display_mapviewBillborads(self):
        self.click_button(self.MAP_VIEW_OPTION)
        return self.is_displayed(self.MAP_VIEW)

    def validate_when_click_listview_to_display_listviewBillborads(self):
        self.click_button(self.LIST_VIEW)
        return self.is_displayed(self.MAP_VIEW)

    def search_billboards(self,name):
        self.text_input(self.SEARCH_BILLBOARD,name)
        self.press_enter()
        return self.get_text(self.FIRST_BILLBOARD_NAME)

    def apply_button_is_displayd(self):
        return self.is_displayed(self.APPLY_BUTTON)

    def apply_button_is_clickble(self):
        return self.clickable(self.APPLY_BUTTON)

    def reset_button_is_displayed(self):
        return self.is_displayed(self.RESET_BUTTON)

    def reset_button_is_clickable(self):
        return self.clickable(self.RESET_BUTTON)

    def filter_by_Price(self,value1,value2):
        self.text_inputs(self.MIN_PRICE,value1)
        self.text_inputs(self.MAX_PRICE,value2)
        self.click_button(self.APPLY_BUTTON)
        return self.get_text(self.FIRST_BILLBOARD_PRICE)

    def reset_filter_price_operation(self):
        self.click_button(self.RESET_BUTTON)
        return self.get_text(self.MIN_PRICE)

    def street_map_option_is_displaed(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.STREET_MAP_VIEW)

    def street_map_option_is_clickable(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        return self.clickable(self.STREET_MAP_VIEW)

    def street_map_terrain_option_displaed(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.click_button(self.STREET_MAP_VIEW)
        return self.is_displayed(self.STREET_MAP_TERRAIN)

    def street_map_terrain_option_clickable(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.click_button(self.STREET_MAP_VIEW)
        return self.clickable(self.STREET_MAP_TERRAIN)

    def street_map_terrain_option_click_operation(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.click_button(self.STREET_MAP_VIEW)
        self.click_button(self.STREET_MAP_TERRAIN)

    def sattelite_map_option_is_displaed(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        return self.is_displayed(self.SATELLITE_VIEW)

    def sattelite_map_option_is_clickable(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        return self.clickable(self.SATELLITE_VIEW)

    def sattelite_map_label_option_displaed(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.click_button(self.SATELLITE_VIEW)
        return self.is_displayed(self.SATELLITE_VIEW_LABEL)

    def sattelite_map_label_option_clickable(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.click_button(self.SATELLITE_VIEW)
        return self.clickable(self.SATELLITE_VIEW_LABEL)

    def sattelite_map_label_option_click_operation(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.click_button(self.SATELLITE_VIEW)
        self.click_button(self.SATELLITE_VIEW_LABEL)

    def full_map_view_option_displayed(self):
        self.click_button(self.MAP_VIEW_OPTION)
        return self.is_displayed(self.FULL_MAP_VIEW)

    def full_map_view_option_clickable(self):
        time.sleep(2)
        self.click_button(self.MAP_VIEW_OPTION)
        return self.clickable(self.FULL_MAP_VIEW)

    def full_map_view_option_click_operation(self):
        time.sleep(2)
        self.click_button(self.MAP_VIEW_OPTION)
        self.click_button(self.FULL_MAP_VIEW)
        self.press_escape_key()


    def zoom_in_option_is_displaed_in_map(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_to_bottom()
        return self.is_displayed(self.MAP_ZOOM_IN)

    def zoom_in_option_is_clickable_in_map(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_to_bottom()
        return self.clickable(self.MAP_ZOOM_IN)

    def zoom_in_oprion_click_operation(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.MAP_ZOOM_IN)
        time.sleep(2)
        self.click_button(self.MAP_ZOOM_IN)

    def zoom_out_option_is_displaed_in_map(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.MAP_ZOOM_OUT)
        time.sleep(2)
        return self.is_displayed(self.MAP_ZOOM_OUT)

    def zoom_out_option_is_clickable_in_map(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.MAP_ZOOM_OUT)
        time.sleep(2)
        return self.clickable(self.MAP_ZOOM_OUT)

    def zoom_out_oprion_click_operation(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.MAP_ZOOM_OUT)
        time.sleep(2)
        self.click_button(self.MAP_ZOOM_OUT)

    def billboard_location_is_displayed(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.BILLBOARD_LOCATION)
        time.sleep(2)
        return self.is_displayed(self.BILLBOARD_LOCATION)

    def billboard_location_is_clickable(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.BILLBOARD_LOCATION)
        time.sleep(2)
        return self.clickable(self.BILLBOARD_LOCATION)

    def billboard_image_displayed_in_map_when_click_location(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.BILLBOARD_LOCATION)
        time.sleep(2)
        self.click_button(self.BILLBOARD_LOCATION)
        return self.is_displayed(self.BILLBOARD_IMAGE_IN_MAP)

    def billboard_image_is_clickable_in_map_location(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.BILLBOARD_LOCATION)
        time.sleep(2)
        self.click_button(self.BILLBOARD_LOCATION)
        return self.clickable(self.BILLBOARD_IMAGE_IN_MAP)

    def billboard_details_displayed_when_clickimage_clicka_in_map_location(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.BILLBOARD_LOCATION)
        time.sleep(2)
        self.click_button(self.BILLBOARD_LOCATION)
        self.click_button(self.BILLBOARD_IMAGE_IN_MAP)
        return self.is_displayed(self.BILLBOARD_DETAILS)

    def billboard_name_displayed_in_map_when_click_location(self):
        self.click_button(self.MAP_VIEW_OPTION)
        time.sleep(5)
        self.scroll_into_view(self.BILLBOARD_LOCATION)
        time.sleep(2)
        self.click_button(self.BILLBOARD_LOCATION)
        return self.get_text(self.BILLBOARD_NAME_IN_MAP)

    def filter_by_indoor_enviroment_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.INDOOR_CHECKBOX)

    def filter_by_outdoor_enviroment_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.OUTDOOR_CHECKBOX)

    def filter_by_indoor_enviroment_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.INDOOR_CHECKBOX)
    def filter_by_outdoor_enviroment_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_CHECKBOX)

    def filter_by_digital_type_is_selected(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.DIGITAL)
        time.sleep(3)
        self.click_button(self.DIGITAL)
        time.sleep(3)
        return self.is_element_selected(self.DIGITAL)

    # def indooer_is_selected(self):
    #     self.click_button(self.FILTER_OPTION)
    #     self.click_button(self.OUTDOOR_CHECKBOX)
    #     return self.is_element_selected(self.OUTDOOR_CHECKBOX)


    def filter_by_small_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.SMALL_SCREEN_CHECKBOX)

    def filter_by_medium_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.MEDIUM_SCREEN_CHECKBOX)

    def filter_by_large_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.LARGE_SCREEN_CHECKBOX)

    def filter_by_extra_large_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.EXTRA_LARGR_SCREEN_CHECKBOX)

    def filter_by_small_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.SMALL_SCREEN_CHECKBOX)

    def filter_by_medium_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.MEDIUM_SCREEN_CHECKBOX)

    def filter_by_large_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.LARGE_SCREEN_CHECKBOX)

    def filter_by_extra_large_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.EXTRA_LARGR_SCREEN_CHECKBOX)

    def filter_led_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.LED_TYPE)

    def filter_by_portrait_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.PORTRAIT_TYPE)

    def filter_by_fascade_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.FACADE_TYPE)

    def filter_by_standee_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.STANDEE_TYPE)

    def filter_by_unipole_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.UNIPOLE_TYPE)

    def filter_by_pillar_wrap_billboard_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        return self.clickable(self.POLLAR_TYPE)

    def filter_led_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.LED_TYPE)

    def filter_by_portrait_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.PORTRAIT_TYPE)

    def filter_by_fascade_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.FACADE_TYPE)

    def filter_by_standee_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.STANDEE_TYPE)

    def filter_by_unipole_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.UNIPOLE_TYPE)

    def filter_by_pillar_wrap_billboard_is_click_operation(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.POLLAR_TYPE)

    def filter_by_finacial_option_is_clickable(self):
        self.click_button(self.FILTER_OPTION)
        self.scroll_into_view(self.FINACIAL_OPTION)
        return self.clickable(self.FINACIAL_OPTION)

    def filter_display_sub_categaries_when_click_finacial_option(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.FINACIAL_OPTION)
        self.click_button(self.SELECT_ALL_SUB)
        return self.get_css_value_pseudo_element(self.SELECT_ALL_SUB,'display')

    def filter_banks_option_is_selected_when_click_all_sub_categeries(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.FINACIAL_OPTION)
        self.click_button(self.SELECT_ALL_SUB)
        return self.get_css_value_pseudo_element(self.BANKS, 'display')

    def filter_when_click_bank_option_toSelected_child_categeries(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.FINACIAL_OPTION)
        self.click_button(self.BANKS)

    def filter_by_sub_categery_atm_is_selected(self):
        return self.get_css_value_pseudo_element(self.ATM, 'display')

    def filter_by_sub_categery_atm123_is_selected(self):
        return self.get_css_value_pseudo_element(self.ATM123, 'display')

    def filter_by_added_atm_displayed_when_click_Bank_option(self):
        return self.is_displayed(self.ATM_ADDED)

    def filter_by_added_atm123_displayed_when_click_Bank_option(self):
        return self.is_displayed(self.ATM123_ADDED)

    def in_filter_added_items_displayed_when_click_Bank_option(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.FINACIAL_OPTION)
        self.click_button(self.BANKS)

    def in_filter_validate_added_atmItem_is_displayed_when_deselect_ATM(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.FINACIAL_OPTION)
        self.click_button(self.BANKS)
        self.click_button(self.ATM)
        return self.is_displayed(self.ATM_ADDED)

    def in_filter_transit_is_displayed(self):
        return self.is_displayed(self.TRANSIT_OPTION)

    def in_filter_to_check_all_sub_categeries_selectd_when_select_all_categery(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_to_check_all_sub_categeries_selectd_when_not_select_all_categery(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)


    def in_filter_sub_categery_airport_is_selected(self):
        return self.get_css_value_pseudo_element(self.AIRPORTS,'display')

    def in_filter_sub_categery_buses_is_selected(self):
        return self.get_css_value_pseudo_element(self.BUSES, 'display')

    def in_filter_sub_categery_subway_is_selected(self):
        return self.get_css_value_pseudo_element(self.SUBWAY, 'display')

    def in_filter_sub_categery_taxi_rideshare_top_is_selected(self):
        return self.get_css_value_pseudo_element(self.TAXI_RIDE_SHARE_TOP, 'display')

    def in_filter_sub_categery_taxi_rideshare_tv_is_selected(self):
        return self.get_css_value_pseudo_element(self.TAXI_RIDE_SHARE_TV, 'display')

    def in_filter_sub_categery_train_station_is_selected(self):
        return self.get_css_value_pseudo_element(self.TRAIN_STATION, 'display')

    def in_filter_airport_categery_arrival_hall_is_selected(self):
        return self.get_css_value_pseudo_element(self.ARRIVAL_HALL,'display')

    def in_filter_airport_categery_baggage_claim_is_selected(self):
        return self.get_css_value_pseudo_element(self.BAGGAGE_CLAIM, 'display')

    def in_filter_airport_categery_depature_hall_is_selected(self):
        return self.get_css_value_pseudo_element(self.DEPARTMENT_HALL, 'display')

    def in_filter_airport_categery_food_court_is_selected(self):
        return self.get_css_value_pseudo_element(self.FOOD_COURT, 'display')

    def in_filter_airport_categery_gates_is_selected(self):
        return self.get_css_value_pseudo_element(self.GATE, 'display')

    def in_filter_airport_categery_loungs_is_selected(self):
        return self.get_css_value_pseudo_element(self.LOUNGES, 'display')

    def in_filter_airport_categery_shopping_area_is_selected(self):
        return self.get_css_value_pseudo_element(self.SHOPPING_AREA, 'display')

    def in_filter_airport_categery_arrival_hall_is_displayed(self):
        return self.is_displayed(self.ARRIVAL_HALL_ADDED)

    def in_filter_airport_categery_baggage_claim_is_displayed(self):
        return self.is_displayed(self.BAGGAGE_CLAIM_ADDED)

    def in_filter_airport_categery_depature_hall_is_displayed(self):
        return self.is_displayed(self.DEPARTMENT_HALL_ADDED)

    def in_filter_airport_categery_food_court_is_displyed(self):
        return self.is_displayed(self.FOOD_COURT_ADDED)

    def in_filter_airport_categery_gates_is_displayed(self):
        return self.is_displayed(self.GATE_ADDED)

    def in_filter_airport_categery_loungs_is_displayed(self):
        return self.is_displayed(self.LOUNGES_ADDED)

    def in_filter_airport_categery_shopping_area_is_displayed(self):
        return self.is_displayed(self.SHOPPING_AREA_ADDED)

    def in_filter_all_products_are_selected_when_click_airport_categery(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.AIRPORTS)

    def in_filter_check_all_products_are_selected_when_deselect_all_product_option(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.AIRPORTS)
        self.click_button(self.SELECT_APP_AIRPORT)

    def in_filter_all_products_show_added_items_when_click_airport_categery(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.AIRPORTS)

    def in_filter_all_products_show_added_items_when_deselect_all_product_option(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.AIRPORTS)
        self.click_button(self.SELECT_APP_AIRPORT)

    def in_filter_check_products_show_added_items_when_deselect_some_option(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.AIRPORTS)
        self.click_button(self.ARRIVAL_HALL)
        self.click_button(self.GATE)

    def in_filter_buses_categery_bus_is_selected(self):
        return self.get_css_value_pseudo_element(self.BUS, 'display')

    def in_filter_buses_categery_bus_terminal_is_selected(self):
        return self.get_css_value_pseudo_element(self.BUS_TERMINAL, 'display')

    def in_filter_buses_categery_bus_is_displayed(self):
        return self.is_displayed(self.BUS_ADDED)

    def in_filter_buses_categery_bus_terminal_is_displayed(self):
        return self.is_displayed(self.BUS_TERMINAL_ADDED)

    def in_filter_when_click_Buses_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.BUSES)

    def in_filter_when_desect_all_product_option_in_bus_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.BUSES)
        self.click_button(self.SELECT_ALL_BUS_PRODUCTS)

    def in_filter_when_click_buses_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.BUSES)

    def in_filter_when_deselect_buses_option_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.BUSES)
        self.click_button(self.BUS)

    def in_filter_subway_categery_platform_is_selected(self):
        return self.get_css_value_pseudo_element(self.PLATFORM, 'display')

    def in_filter_subway_categery_subway_train_is_selected(self):
        return self.get_css_value_pseudo_element(self.SUBWAY_TRAIN, 'display')

    def in_filter_subway_categery_subway_terminal_is_selected(self):
        return self.get_css_value_pseudo_element(self.SUBWAY_TERMINAL, 'display')

    def in_filter_subway_categery_platform_is_displayed(self):
        return self.is_displayed(self.PLATFORM_ADDED)

    def in_filter_subway_categery_subway_train_is_displayed(self):
        return self.is_displayed(self.SUBWAY_TRAIN_ADDED)

    def in_filter_subway_categery_subway_terminal_is_displayed(self):
        return self.is_displayed(self.SUBWAY_TERMINAL_ADDED)

    def in_filter_when_click_subway_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.SUBWAY)

    def in_filter_when_desect_all_product_option_in_subway_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.SUBWAY)
        self.click_button(self.SELECT_ALL_TRANSIT_PRODUCTS)

    def in_filter_when_click_subway_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.SUBWAY)

    def in_filter_when_deselect_subway_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.SUBWAY)
        self.click_button(self.SUBWAY_TERMINAL)

    def in_filter_train_station_categery_train_platform_is_selected(self):
        return self.get_css_value_pseudo_element(self.TRAIN_PLATFORM, 'display')

    def in_filter_train_station_categery_train_terminal_is_selected(self):
        return self.get_css_value_pseudo_element(self.TRAIN_TERMINAL, 'display')

    def in_filter_train_station_train_is_selected(self):
        return self.get_css_value_pseudo_element(self.TRAIN, 'display')

    def in_filter_train_station_categery_train_platform_is_displayed(self):
        return self.is_displayed(self.TRAIN_PLATFORM_ADDED)

    def in_filter_train_station_categery_train_terminal_is_displayed(self):
        return self.is_displayed(self.TRAIN_TERMINAL_ADDED)

    def in_filter_train_station_train_is_displayed(self):
        return self.is_displayed(self.TRAIN_ADDED)

    def in_filter_when_click_train_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        time.sleep(4)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.TRAIN_STATION)

    def in_filter_when_desect_all_product_option_in_train_station_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.TRAIN_STATION)
        self.click_button(self.SELECT_ALL_TRANSIT_PRODUCTS)

    def in_filter_when_click_train_station_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.TRAIN_STATION)

    def in_filter_when_deselect_train_station_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.TRANSIT_OPTION)
        self.click_button(self.TRAIN_STATION)
        self.click_button(self.TRAIN_TERMINAL)

    def in_filter_outdoor_categery_billboard_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_BILLBOARDS, 'display')

    def in_filter_outdoor_categery_bus_shelter_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_BUS_SHELTER, 'display')

    def in_filter_outdoor_street_structure_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_STREET_FUNITURE, 'display')

    def in_filter_outdoor_categery_toll_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_TOLL, 'display')

    def in_filter_outdoor_categery_truck_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_TRUCK, 'display')

    def in_filter_outdoor_urban_panel_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_URBAN_PANEL, 'display')

    def in_filter_outdoor_wallscape_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUT_DOOR_WALLSCAPE, 'display')

    def in_filter_outdoor_all_categaries_are_selected_when_click_selectAll(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_outdoor_all_categaries_are_selected_when_deselect_selectAll_option(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.SELECT_ALL_SUB)
        time.sleep(1)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_billboard_sub_categery_hignway_is_selected(self):
        return self.get_css_value_pseudo_element(self.HIGHWAY, 'display')

    def in_filter_billboard_sub_categery_roadeside_is_selected(self):
        return self.get_css_value_pseudo_element(self.ROAD_SIDE, 'display')

    def in_filter_billboard_sub_categery_spectucular_is_selected(self):
        return self.get_css_value_pseudo_element(self.SPECTUCAL, 'display')

    def in_filter_billboard_sub_categery_hignway_is_displayed(self):
        return self.is_displayed(self.HIGHWAY_ADDED)

    def in_filter_billboard_sub_categery_roadeside_is_displayed(self):
        return self.is_displayed(self.ROAD_SIDE_ADDED)

    def in_filter_billboard_sub_categery_spectucular_is_displayed(self):
        return self.is_displayed(self.SPECTUCAL_ADDED)

    def in_filter_when_click_billboards_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        time.sleep(4)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_BILLBOARDS)

    def in_filter_when_desect_all_product_option_in_billboards_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_BILLBOARDS)
        self.click_button(self.SELECT_ALL_OUTDOOR)

    def in_filter_when_click_billboards_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_BILLBOARDS)

    def in_filter_when_deselect_billboards_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_BILLBOARDS)
        self.click_button(self.HIGHWAY)
        self.click_button(self.ROAD_SIDE)

    def in_filter_street_furniture_sub_categery_city_clock_is_selected(self):
        return self.get_css_value_pseudo_element(self.CITY_CLOCKS, 'display')

    def in_filter_street_furniture_sub_categery_city_light_is_selected(self):
        return self.get_css_value_pseudo_element(self.CITY_LIGHT, 'display')

    def in_filter_street_furniture_sub_categery_kiosks_is_selected(self):
        return self.get_css_value_pseudo_element(self.KIOSKS, 'display')

    def in_filter_street_furniture_sub_categery_outdoot_gym_is_selected(self):
        return self.get_css_value_pseudo_element(self.OUTDOOR_gym, 'display')

    def in_filter_street_furniture_sub_categery_Street_sign_is_selected(self):
        return self.get_css_value_pseudo_element(self.STREET_SIGN, 'display')

    def in_filter_street_furniture_sub_categery_city_clock_is_displayed(self):
        return self.is_displayed(self.CITY_CLOCKS_ADDED)

    def in_filter_street_furniture_sub_categery_city_light_is_displayed(self):
        return self.is_displayed(self.CITY_LIGHT_ADDED)

    def in_filter_street_furniture_sub_categery_kiosks_is_displayed(self):
        return self.is_displayed(self.KIOSKS_ADDED)

    def in_filter_street_furniture_sub_categery_outdoot_gym_is_displayed(self):
        return self.is_displayed(self.OUTDOOR_gym_ADDED)

    def in_filter_street_furniture_sub_categery_Street_sign_is_displayed(self):
        return self.is_displayed(self.STREET_SIGN_ADDED)

    def in_filter_when_click_street_furniture_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        time.sleep(10)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_STREET_FUNITURE)

    def in_filter_when_desect_all_product_option_in_street_furniture_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_STREET_FUNITURE)
        self.click_button(self.SELECT_ALL_OUTDOOR)

    def in_filter_when_click_street_furniture_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_STREET_FUNITURE)

    def in_filter_when_deselect_street_furniture_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_STREET_FUNITURE)
        self.click_button(self.CITY_LIGHT)
        self.click_button(self.KIOSKS)

    def in_filter_Toll_sub_categery_cabin_is_selected(self):
        return self.get_css_value_pseudo_element(self.CABIN, 'display')

    def in_filter_Toll_sub_categery_panel_is_selected(self):
        return self.get_css_value_pseudo_element(self.PANEL, 'display')

    def in_filter_Toll_sub_categery_cabin_is_displayed(self):
        return self.is_displayed(self.CABIN_ADDED)

    def in_filter_Toll_sub_categery_panel_is_displayed(self):
        return self.is_displayed(self.PANEL_ADDED)

    def in_filter_when_click_toll_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_TOLL)

    def in_filter_when_desect_all_product_option_in_toll_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_TOLL)
        self.click_button(self.SELECT_ALL_OUTDOOR)


    def in_filter_when_click_toll_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_TOLL)

    def in_filter_when_deselect_toll_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.OUTDOOR_OPTION)
        self.click_button(self.OUT_DOOR_TOLL)
        self.click_button(self.PANEL)

    def in_filter_point_of_care_sub_categery_doctor_office_is_selected(self):
        return self.get_css_value_pseudo_element(self.DOCTORS_OFFICE, 'display')

    def in_filter_point_of_care_sub_categery_vetenar_office__is_selected(self):
        return self.get_css_value_pseudo_element(self.VETERNERY_OFFICE, 'display')

    def in_filter_point_of_care_sub_categery_doctor_office_is_displayed(self):
        return self.is_displayed(self.DOCTORS_OFFICE_ADDED)

    def in_filter_point_of_care_sub_categery_vetenar_office_is_displayed(self):
        return self.is_displayed(self.VETERNERY_OFFICE_ADDED)

    def in_filter_when_click_point_of_care_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        time.sleep(9)
        self.click_button(self.POINT_OF_CARE_OPTION)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_when_desect_all_product_option_in_point_of_care_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.POINT_OF_CARE_OPTION)
        self.click_button(self.SELECT_ALL_SUB)
        time.sleep(3)
        self.click_button(self.SELECT_ALL_SUB)


    def in_filter_when_click_point_of_care_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.POINT_OF_CARE_OPTION)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_when_deselect_point_of_care_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.POINT_OF_CARE_OPTION)
        self.click_button(self.VETERNERY_OFFICE)

    def in_filter_entertainment_sub_categery_bars_is_selected(self):
        return self.get_css_value_pseudo_element(self.BARS, 'display')

    def in_filter_entertainment_sub_categery_causal_dining_is_selected(self):
        return self.get_css_value_pseudo_element(self.CASUAL_DINING, 'display')

    def in_filter_entertainment_sub_categery_golf_cart_is_selected(self):
        return self.get_css_value_pseudo_element(self.GOLF_CART, 'display')

    def in_filter_entertainment_sub_categery_hotels_is_selected(self):
        return self.get_css_value_pseudo_element(self.HOTEL, 'display')

    def in_filter_entertainment_sub_categery_movie_theater_is_selected(self):
        return self.get_css_value_pseudo_element(self.MOVIE_THEATER, 'display')

    def in_filter_entertainment_sub_categery_QSR_is_selected(self):
        return self.get_css_value_pseudo_element(self.QSP, 'display')

    def in_filter_entertainment_sub_categery_Recreation_location_is_selected(self):
        return self.get_css_value_pseudo_element(self.RECREATIONAL_LOCATION, 'display')

    def in_filter_when_click_entertainment_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_when_desect_all_product_option_in_entertainment_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.SELECT_ALL_SUB)
        time.sleep(3)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_point_of_hotels_sub_categery_hotels_elevator_is_selected(self):
        return self.get_css_value_pseudo_element(self.HOTELS_ELEVATOR, 'display')

    def in_filter_hotels_sub_categery_hotels_lobby_is_selected(self):
        return self.get_css_value_pseudo_element(self.HOTELS_LOBBY, 'display')

    def in_filter_hotels_sub_categery_hotels_elevator_is_displayed(self):
        return self.is_displayed(self.HOTELS_ELEVATOR_ADDED)

    def in_filter_hotels_sub_categery_hotels_lobby_is_displayed(self):
        return self.is_displayed(self.HOTELS_LOBBY_ADDED)

    def in_filter_when_hotels_toll_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.HOTEL)

    def in_filter_when_desect_all_product_option_in_hotels_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.HOTEL)
        self.click_button(self.SELECT_ALL_ENTERMENT)

    def in_filter_when_click_hotels_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.HOTEL)

    def in_filter_when_deselect_hotels_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.HOTEL)
        self.click_button(self.HOTELS_LOBBY)

    def in_filter_movie_theater_sub_categery_food_court_is_selected(self):
        return self.get_css_value_pseudo_element(self.FOOD_COURT_THEATER, 'display')

    def in_filter_movie_theater_sub_categery_lobby_is_selected(self):
        return self.get_css_value_pseudo_element(self.THEATER_LOBBY, 'display')

    def in_filter_movie_theater_sub_categery_food_court_is_displayed(self):
        return self.is_displayed(self.FOOD_COURT_THEATER_ADDED)

    def in_filter_movie_theater_sub_categery_lobby_is_displayed(self):
        return self.is_displayed(self.THEATER_LOBBY_ADDED)

    def in_filter_when_movie_theater_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.MOVIE_THEATER)

    def in_filter_when_desect_all_product_option_in_movie_theater_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.MOVIE_THEATER)
        self.click_button(self.SELECT_ALL_ENTERMENT)

    def in_filter_when_click_movie_theater_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.MOVIE_THEATER)

    def in_filter_when_deselect_movie_theater_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.MOVIE_THEATER)
        self.click_button(self.THEATER_LOBBY)

    def in_filter_Recreation_location_sub_categery_concert_venues_is_selected(self):
        return self.get_css_value_pseudo_element(self.CONCERT_VENUES, 'display')

    def in_filter_Recreation_location_sub_categery_musium_gallery_is_selected(self):
        return self.get_css_value_pseudo_element(self.MUSEUM_GALLERY, 'display')

    def in_filter_Recreation_location_sub_categery_theme_park_is_selected(self):
        return self.get_css_value_pseudo_element(self.THEME_PART, 'display')

    def in_filter_Recreation_location_sub_categery_concert_venues_is_displayed(self):
        return self.is_displayed(self.CONCERT_VENUES_ADDED)

    def in_filter_Recreation_location_sub_categery_musium_gallery_is_displayed(self):
        return self.is_displayed(self.MUSEUM_GALLERY_ADDED)

    def in_filter_Recreation_location_sub_categery_theme_park_is_displayed(self):
        return self.is_displayed(self.THEME_PART_ADDED)

    def in_filter_when_Recreation_location_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.RECREATIONAL_LOCATION)

    def in_filter_when_desect_all_product_option_in_Recreation_location_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.RECREATIONAL_LOCATION)
        self.click_button(self.SELECT_ALL_ENTERMENT)

    def in_filter_when_click_Recreation_location_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.RECREATIONAL_LOCATION)

    def in_filter_when_deselect_Recreation_location_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.RECREATIONAL_LOCATION)
        self.click_button(self.MUSEUM_GALLERY)

    def in_filter_Rsports_ent_sub_categery_club_house_is_selected(self):
        return self.get_css_value_pseudo_element(self.CLUB_HOUSE, 'display')

    def in_filter_Rsports_ent_sub_categery_sport_arena_is_selected(self):
        return self.get_css_value_pseudo_element(self.SPORT_ARENA, 'display')

    def in_filter_Rsports_ent_sub_categery_club_house_is_displayed(self):
        return self.is_displayed(self.CLUB_HOUSE_ADDED)

    def in_filter_Rsports_ent_sub_categery_sport_arena_is_displayed(self):
        return self.is_displayed(self.SPORT_ARENA_ADDED)

    def in_filter_when_sports_ent_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.SPORTS_ENT)

    def in_filter_when_desect_all_product_option_in_sports_ent_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.SPORTS_ENT)
        self.click_button(self.SELECT_ALL_ENTERMENT)

    def in_filter_when_click_sports_ent_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.SPORTS_ENT)

    def in_filter_when_deselect_sports_ent_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.ENTERTAINMENT_OPTION)
        self.click_button(self.SPORTS_ENT)
        self.click_button(self.CLUB_HOUSE)

    def in_filter_health_beauty_sub_categery_gym_is_selected(self):
        return self.get_css_value_pseudo_element(self.GYM, 'display')

    def in_filter_health_beauty_sub_categery_salone_is_selected(self):
        return self.get_css_value_pseudo_element(self.SALONS, 'display')

    def in_filter_health_beauty_sub_categery_spas_is_selected(self):
        return self.get_css_value_pseudo_element(self.SPAS, 'display')

    def in_filter_when_health_beauty_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.HEATH_BEAUTY)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_when_desect_all_product_option_in_health_beauty_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.HEATH_BEAUTY)
        self.click_button(self.SELECT_ALL_SUB)
        time.sleep(3)
        self.click_button(self.SELECT_ALL_SUB)

    def in_filter_gym_sub_categery_fitness_equipment_is_selected(self):
        return self.get_css_value_pseudo_element(self.FITNESS_EQUIPMENT, 'display')

    def in_filter_gym_sub_categery_lobby_is_selected(self):
        return self.get_css_value_pseudo_element(self.HEALTH_LOBBY, 'display')

    def in_filter_gym_sub_categery_fitness_equipment_is_displayed(self):
        return self.is_displayed(self.FITNESS_EQUIPMENT_ADDED)

    def in_filter_gym_sub_categery_lobby_is_displayed(self):
        return self.is_displayed(self.HEALTH_LOBBY_ADDED)

    def in_filter_when_Gym_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.HEATH_BEAUTY)
        self.click_button(self.GYM)

    def in_filter_when_desect_all_product_option_in_gym_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.HEATH_BEAUTY)
        self.click_button(self.GYM)
        self.click_button(self.SELECT_ALL_HEALTH_BEAUTY)

    def in_filter_when_click_gym_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.HEATH_BEAUTY)
        self.click_button(self.GYM)

    def in_filter_when_deselect_gym_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.HEATH_BEAUTY)
        self.click_button(self.GYM)
        self.click_button(self.FITNESS_EQUIPMENT)

    def in_filter_apportment_building_categery_elevator_is_selected(self):
        return self.get_css_value_pseudo_element(self.RESIDENTIAL_ELEVATOR, 'display')

    def in_filter_apportment_building_sub_categery_lobby_is_selected(self):
        return self.get_css_value_pseudo_element(self.RESIDENTIAL_LOBBY, 'display')

    def in_filter_apportment_building_sub_categery_elevator_is_displayed(self):
        return self.is_displayed(self.RESIDENTIAL_ELEVATOR_ADDED)

    def in_filter_apportment_building_sub_categery_lobby_is_displayed(self):
        return self.is_displayed(self.RESIDENTIAL_LOBBY_ADDED)

    def in_filter_when_apportment_building_to_select_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.RESIDENTIAL_OPTION)
        self.click_button(self.APPORTMENT_BUILDING)

    def in_filter_when_desect_all_product_option_in_apportment_building_to_Deselect_all_sub_categerty(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.RESIDENTIAL_OPTION)
        self.click_button(self.APPORTMENT_BUILDING)
        self.click_button(self.SELECT_ALL_RESIDENTIAL)

    def in_filter_when_click_apportment_building_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.RESIDENTIAL_OPTION)
        self.click_button(self.APPORTMENT_BUILDING)

    def in_filter_when_deselect_apportment_building_options_to_display_added_items(self):
        self.click_button(self.FILTER_OPTION)
        self.click_button(self.RESIDENTIAL_OPTION)
        self.click_button(self.APPORTMENT_BUILDING)
        self.click_button(self.RESIDENTIAL_LOBBY)





































